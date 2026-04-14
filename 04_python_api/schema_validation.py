"""
ETL Pipeline with Pydantic Validation
======================================
Tables : users, products, orders
Flow   : Source DB → SQLAlchemy query → Python list
         → Pydantic validation → clean list
         → Insert into destination DB
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator

from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# ─────────────────────────────────────────────
# 0.  ENGINE SETUP
# ─────────────────────────────────────────────

SOURCE_DB_URL = "sqlite:///source.db"   # ← your source DB
DEST_DB_URL   = "sqlite:///clean.db"    # ← your destination DB

source_engine = create_engine(SOURCE_DB_URL, echo=False)
dest_engine   = create_engine(DEST_DB_URL,   echo=False)


# ─────────────────────────────────────────────
# 1.  SQLALCHEMY ORM MODELS
# ─────────────────────────────────────────────

class SourceBase(DeclarativeBase):
    pass

class DestBase(DeclarativeBase):
    pass


# ── Source models (raw / nullable) ──────────

class SrcUser(SourceBase):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String)
    age   = Column(Integer)
    city  = Column(String)
    email = Column(String)

class SrcProduct(SourceBase):
    __tablename__ = "products"
    id       = Column(Integer, primary_key=True)
    name     = Column(String)
    price    = Column(Float)
    category = Column(String)
    stock    = Column(Integer)

class SrcOrder(SourceBase):
    __tablename__ = "orders"
    order_id    = Column(Integer, primary_key=True)
    user_id     = Column(Integer)
    product     = Column(String)
    quantity    = Column(Integer)
    total_price = Column(Float)
    status      = Column(String)


# ── Destination models (clean, NOT NULL) ─────

class CleanUser(DestBase):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String,  nullable=False)
    age   = Column(Integer, nullable=False)
    city  = Column(String,  nullable=False)
    email = Column(String,  nullable=False, unique=True)

class CleanProduct(DestBase):
    __tablename__ = "products"
    id       = Column(Integer, primary_key=True)
    name     = Column(String,  nullable=False)
    price    = Column(Float,   nullable=False)
    category = Column(String,  nullable=False)
    stock    = Column(Integer, nullable=False)

class CleanOrder(DestBase):
    __tablename__ = "orders"
    order_id    = Column(Integer, primary_key=True)
    user_id     = Column(Integer, nullable=False)
    product     = Column(String,  nullable=False)
    quantity    = Column(Integer, nullable=False)
    total_price = Column(Float,   nullable=False)
    status      = Column(String,  nullable=False)


DestBase.metadata.create_all(dest_engine)


# ─────────────────────────────────────────────
# 2.  PYDANTIC SCHEMAS  (validation lives here)
# ─────────────────────────────────────────────

VALID_STATUSES = {"pending", "processing", "shipped", "delivered"}


class UserSchema(BaseModel):
    id   : int
    name : str   = Field(..., min_length=1)
    age  : int   = Field(..., gt=0, lt=120)
    city : str   = Field(..., min_length=1)
    email: EmailStr                             # built-in format + MX check

    @field_validator("name", "city", mode="before")
    @classmethod
    def strip_and_reject_blank(cls, v: object) -> str:
        if v is None or str(v).strip() == "":
            raise ValueError("field must not be null or blank")
        return str(v).strip()

    @field_validator("email", mode="before")
    @classmethod
    def normalise_email(cls, v: object) -> str:
        if v is None:
            raise ValueError("email must not be null")
        return str(v).strip().lower()


class ProductSchema(BaseModel):
    id      : int
    name    : str   = Field(..., min_length=1)
    price   : float = Field(..., ge=0)
    category: str   = Field(..., min_length=1)
    stock   : int   = Field(..., ge=0)

    @field_validator("name", "category", mode="before")
    @classmethod
    def strip_and_reject_blank(cls, v: object) -> str:
        if v is None or str(v).strip() == "":
            raise ValueError("field must not be null or blank")
        return str(v).strip()


class OrderSchema(BaseModel):
    order_id   : int
    user_id    : int
    product    : str   = Field(..., min_length=1)
    quantity   : int   = Field(..., gt=0)
    total_price: float = Field(..., ge=0)
    status     : str

    @field_validator("product", mode="before")
    @classmethod
    def strip_and_reject_blank(cls, v: object) -> str:
        if v is None or str(v).strip() == "":
            raise ValueError("field must not be null or blank")
        return str(v).strip()

    @field_validator("status", mode="before")
    @classmethod
    def normalise_status(cls, v: object) -> str:
        if v is None:
            raise ValueError("status must not be null")
        cleaned = str(v).strip().lower()
        if cleaned not in VALID_STATUSES:
            raise ValueError(
                f"invalid status {v!r}; must be one of {VALID_STATUSES}"
            )
        return cleaned

    @field_validator("total_price", "quantity", mode="before")
    @classmethod
    def reject_none_numeric(cls, v: object) -> object:
        if v is None:
            raise ValueError("field must not be null")
        return v


# ─────────────────────────────────────────────
# 3.  QUERY SOURCE DB → PYTHON LISTS
# ─────────────────────────────────────────────

def fetch_all_source_data() -> tuple[list, list, list]:
    with Session(source_engine) as session:
        users    = session.query(SrcUser).all()
        products = session.query(SrcProduct).all()
        orders   = session.query(SrcOrder).all()
        session.expunge_all()
    return users, products, orders


# ─────────────────────────────────────────────
# 4.  VALIDATE WITH PYDANTIC
# ─────────────────────────────────────────────

@dataclass
class ValidationResult:
    clean_users:    list[UserSchema]    = field(default_factory=list)
    clean_products: list[ProductSchema] = field(default_factory=list)
    clean_orders:   list[OrderSchema]   = field(default_factory=list)

    rejected_users:    list[tuple] = field(default_factory=list)  # (raw_obj, errors_str)
    rejected_products: list[tuple] = field(default_factory=list)
    rejected_orders:   list[tuple] = field(default_factory=list)


def _orm_to_dict(obj) -> dict:
    """Convert a SQLAlchemy ORM row to a plain dict (skip internal keys)."""
    return {
        k: v for k, v in obj.__dict__.items()
        if not k.startswith("_")
    }


def run_validation(
    users:    list[SrcUser],
    products: list[SrcProduct],
    orders:   list[SrcOrder],
) -> ValidationResult:
    from pydantic import ValidationError

    result = ValidationResult()

    # ── Users ──
    for u in users:
        try:
            result.clean_users.append(UserSchema(**_orm_to_dict(u)))
        except ValidationError as e:
            errors = "; ".join(
                f"{err['loc'][0]}: {err['msg']}" for err in e.errors()
            )
            result.rejected_users.append((u, errors))

    # ── Products ──
    for p in products:
        try:
            result.clean_products.append(ProductSchema(**_orm_to_dict(p)))
        except ValidationError as e:
            errors = "; ".join(
                f"{err['loc'][0]}: {err['msg']}" for err in e.errors()
            )
            result.rejected_products.append((p, errors))

    # ── Orders ──
    for o in orders:
        try:
            result.clean_orders.append(OrderSchema(**_orm_to_dict(o)))
        except ValidationError as e:
            errors = "; ".join(
                f"{err['loc'][0]}: {err['msg']}" for err in e.errors()
            )
            result.rejected_orders.append((o, errors))

    return result


# ─────────────────────────────────────────────
# 5.  INSERT CLEAN DATA INTO DESTINATION DB
# ─────────────────────────────────────────────

def insert_clean_data(result: ValidationResult) -> dict[str, int]:
    inserted: dict[str, int] = {"users": 0, "products": 0, "orders": 0}

    with Session(dest_engine) as session:

        for u in result.clean_users:
            session.merge(CleanUser(
                id=u.id, name=u.name, age=u.age,
                city=u.city, email=u.email,
            ))
        inserted["users"] = len(result.clean_users)

        for p in result.clean_products:
            session.merge(CleanProduct(
                id=p.id, name=p.name, price=p.price,
                category=p.category, stock=p.stock,
            ))
        inserted["products"] = len(result.clean_products)

        for o in result.clean_orders:
            session.merge(CleanOrder(
                order_id=o.order_id, user_id=o.user_id,
                product=o.product, quantity=o.quantity,
                total_price=o.total_price, status=o.status,
            ))
        inserted["orders"] = len(result.clean_orders)

        session.commit()

    return inserted


# ─────────────────────────────────────────────
# 6.  REPORT
# ─────────────────────────────────────────────

def print_report(result: ValidationResult, inserted: dict[str, int]) -> None:
    total_u = len(result.clean_users)    + len(result.rejected_users)
    total_p = len(result.clean_products) + len(result.rejected_products)
    total_o = len(result.clean_orders)   + len(result.rejected_orders)

    print("\n" + "═" * 60)
    print("  ETL PIPELINE REPORT  (Pydantic validation)")
    print("═" * 60)
    print(f"{'Table':<12} {'Total':>6} {'Clean':>6} {'Rejected':>9} {'Inserted':>9}")
    print("─" * 60)
    print(f"{'Users':<12} {total_u:>6} {len(result.clean_users):>6} {len(result.rejected_users):>9} {inserted['users']:>9}")
    print(f"{'Products':<12} {total_p:>6} {len(result.clean_products):>6} {len(result.rejected_products):>9} {inserted['products']:>9}")
    print(f"{'Orders':<12} {total_o:>6} {len(result.clean_orders):>6} {len(result.rejected_orders):>9} {inserted['orders']:>9}")
    print("═" * 60)

    if result.rejected_users:
        print("\n🚫 Rejected Users:")
        for u, errs in result.rejected_users:
            print(f"  id={u.id:>3}  →  {errs}")

    if result.rejected_products:
        print("\n🚫 Rejected Products:")
        for p, errs in result.rejected_products:
            print(f"  id={p.id:>3}  →  {errs}")

    if result.rejected_orders:
        print("\n🚫 Rejected Orders:")
        for o, errs in result.rejected_orders:
            print(f"  order_id={o.order_id:>3}  →  {errs}")


# ─────────────────────────────────────────────
# 7.  MAIN
# ─────────────────────────────────────────────

def run_pipeline() -> None:
    print("▶  Step 1: Fetching data from source DB …")
    users, products, orders = fetch_all_source_data()
    print(f"   Fetched {len(users)} users, {len(products)} products, {len(orders)} orders")

    print("▶  Step 2: Validating with Pydantic …")
    result = run_validation(users, products, orders)

    print("▶  Step 3: Inserting clean records into destination DB …")
    inserted = insert_clean_data(result)

    print_report(result, inserted)
    print("\n✅  Pipeline complete.\n")


if __name__ == "__main__":
    run_pipeline()
