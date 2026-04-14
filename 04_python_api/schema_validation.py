"""Validate schema and write curated output."""


"""
ETL Pipeline: Source DB → Validate → Clean DB
=============================================
Tables: users, products, orders
Steps:
  1. Define ORM models for both source & destination DBs
  2. Query source DB → load into plain Python lists
  3. Validate each record → collect clean + rejected rows
  4. Bulk-insert clean records into destination DB
"""

from sqlalchemy import (
    create_engine, Column, Integer, String, Float,
    Enum as SAEnum, text
)
from sqlalchemy.orm import DeclarativeBase, Session
from dataclasses import dataclass, field
from typing import Optional
import re
import enum

# ─────────────────────────────────────────────
# 0.  ENGINE SETUP
# ─────────────────────────────────────────────

# Source DB  (read-only; contains dirty data)
SOURCE_DB_URL = "sqlite:///source.db"          # change to your actual URL
# Destination DB (receives only clean data)
DEST_DB_URL   = "sqlite:///clean.db"           # change to your actual URL

source_engine = create_engine(SOURCE_DB_URL, echo=False)
dest_engine   = create_engine(DEST_DB_URL,   echo=False)


# ─────────────────────────────────────────────
# 1.  ORM MODELS
# ─────────────────────────────────────────────

class SourceBase(DeclarativeBase):
    pass

class DestBase(DeclarativeBase):
    pass


# ── Source models (mirrors the raw DB; nulls allowed) ──

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


# ── Destination models (NOT NULL enforced at app layer before insert) ──

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


# Create tables in destination DB
DestBase.metadata.create_all(dest_engine)


# ─────────────────────────────────────────────
# 2.  QUERY SOURCE DB → PYTHON LISTS
# ─────────────────────────────────────────────

def fetch_all_source_data() -> tuple[list, list, list]:
    """
    Returns three lists of raw ORM objects:
      (users, products, orders)
    """
    with Session(source_engine) as session:
        users    = session.query(SrcUser).all()
        products = session.query(SrcProduct).all()
        orders   = session.query(SrcOrder).all()

        # Detach from session so objects can be used outside
        # (expunge_all keeps attribute access working)
        session.expunge_all()

    return users, products, orders


# ─────────────────────────────────────────────
# 3.  VALIDATION HELPERS
# ─────────────────────────────────────────────

EMAIL_RE = re.compile(r"^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$")

VALID_ORDER_STATUSES = {"pending", "processing", "shipped", "delivered"}


@dataclass
class ValidationResult:
    clean_users:    list = field(default_factory=list)
    clean_products: list = field(default_factory=list)
    clean_orders:   list = field(default_factory=list)

    rejected_users:    list = field(default_factory=list)   # (record, [reasons])
    rejected_products: list = field(default_factory=list)
    rejected_orders:   list = field(default_factory=list)


def validate_user(u: SrcUser) -> list[str]:
    """Return a list of failure reasons; empty list = valid."""
    errors = []
    if not u.name or not str(u.name).strip():
        errors.append("name is null/empty")
    if u.age is None:
        errors.append("age is null")
    elif not (0 < u.age < 120):
        errors.append(f"age out of range: {u.age}")
    if not u.city or not str(u.city).strip():
        errors.append("city is null/empty")
    if not u.email or not EMAIL_RE.match(str(u.email)):
        errors.append(f"invalid email: {u.email!r}")
    return errors


def validate_product(p: SrcProduct) -> list[str]:
    errors = []
    if not p.name or not str(p.name).strip():
        errors.append("name is null/empty")
    if p.price is None:
        errors.append("price is null")
    elif p.price < 0:
        errors.append(f"negative price: {p.price}")
    if not p.category or not str(p.category).strip():
        errors.append("category is null/empty")
    if p.stock is None:
        errors.append("stock is null")
    elif p.stock < 0:
        errors.append(f"negative stock: {p.stock}")
    return errors


def validate_order(o: SrcOrder) -> list[str]:
    errors = []
    if not o.product or not str(o.product).strip():
        errors.append("product is null/empty")
    if o.quantity is None:
        errors.append("quantity is null")
    elif o.quantity <= 0:
        errors.append(f"quantity must be > 0: {o.quantity}")
    if o.total_price is None:
        errors.append("total_price is null")
    elif o.total_price < 0:
        errors.append(f"negative total_price: {o.total_price}")
    if not o.status or str(o.status).lower() not in VALID_ORDER_STATUSES:
        errors.append(f"invalid status: {o.status!r}")
    return errors


def run_validation(
    users: list[SrcUser],
    products: list[SrcProduct],
    orders: list[SrcOrder],
) -> ValidationResult:

    result = ValidationResult()

    for u in users:
        errors = validate_user(u)
        if errors:
            result.rejected_users.append((u, errors))
        else:
            result.clean_users.append(u)

    for p in products:
        errors = validate_product(p)
        if errors:
            result.rejected_products.append((p, errors))
        else:
            result.clean_products.append(p)

    for o in orders:
        errors = validate_order(o)
        if errors:
            result.rejected_orders.append((o, errors))
        else:
            result.clean_orders.append(o)

    return result


# ─────────────────────────────────────────────
# 4.  INSERT CLEAN DATA INTO DESTINATION DB
# ─────────────────────────────────────────────

def insert_clean_data(result: ValidationResult) -> dict:
    """
    Bulk-insert clean records into the destination DB.
    Returns a summary dict with counts.
    """
    inserted = {"users": 0, "products": 0, "orders": 0}

    with Session(dest_engine) as session:
        # ── Users ──
        for u in result.clean_users:
            session.merge(                          # merge = upsert by PK
                CleanUser(
                    id=u.id, name=u.name.strip(),
                    age=u.age, city=u.city.strip(),
                    email=u.email.strip().lower(),
                )
            )
        inserted["users"] = len(result.clean_users)

        # ── Products ──
        for p in result.clean_products:
            session.merge(
                CleanProduct(
                    id=p.id, name=p.name.strip(),
                    price=float(p.price), category=p.category.strip(),
                    stock=int(p.stock),
                )
            )
        inserted["products"] = len(result.clean_products)

        # ── Orders ──
        for o in result.clean_orders:
            session.merge(
                CleanOrder(
                    order_id=o.order_id, user_id=o.user_id,
                    product=o.product.strip(),
                    quantity=int(o.quantity),
                    total_price=float(o.total_price),
                    status=str(o.status).lower().strip(),
                )
            )
        inserted["orders"] = len(result.clean_orders)

        session.commit()

    return inserted


# ─────────────────────────────────────────────
# 5.  REPORTING
# ─────────────────────────────────────────────

def print_report(result: ValidationResult, inserted: dict) -> None:
    total_u = len(result.clean_users)    + len(result.rejected_users)
    total_p = len(result.clean_products) + len(result.rejected_products)
    total_o = len(result.clean_orders)   + len(result.rejected_orders)

    print("\n" + "═" * 55)
    print("  ETL PIPELINE REPORT")
    print("═" * 55)
    print(f"{'Table':<12} {'Total':>6} {'Clean':>6} {'Rejected':>9} {'Inserted':>9}")
    print("─" * 55)
    print(f"{'Users':<12} {total_u:>6} {len(result.clean_users):>6} {len(result.rejected_users):>9} {inserted['users']:>9}")
    print(f"{'Products':<12} {total_p:>6} {len(result.clean_products):>6} {len(result.rejected_products):>9} {inserted['products']:>9}")
    print(f"{'Orders':<12} {total_o:>6} {len(result.clean_orders):>6} {len(result.rejected_orders):>9} {inserted['orders']:>9}")
    print("═" * 55)

    if result.rejected_users:
        print("\n🚫 Rejected Users:")
        for u, errs in result.rejected_users:
            print(f"  id={u.id:>3} → {', '.join(errs)}")

    if result.rejected_products:
        print("\n🚫 Rejected Products:")
        for p, errs in result.rejected_products:
            print(f"  id={p.id:>3} → {', '.join(errs)}")

    if result.rejected_orders:
        print("\n🚫 Rejected Orders:")
        for o, errs in result.rejected_orders:
            print(f"  order_id={o.order_id:>3} → {', '.join(errs)}")


# ─────────────────────────────────────────────
# 6.  MAIN ENTRY POINT
# ─────────────────────────────────────────────

def run_pipeline() -> None:
    print("▶  Step 1: Fetching data from source DB …")
    users, products, orders = fetch_all_source_data()
    print(f"   Fetched {len(users)} users, {len(products)} products, {len(orders)} orders")

    print("▶  Step 2: Validating records …")
    result = run_validation(users, products, orders)

    print("▶  Step 3: Inserting clean records into destination DB …")
    inserted = insert_clean_data(result)

    print_report(result, inserted)
    print("\n✅  Pipeline complete.\n")


if __name__ == "__main__":
    run_pipeline()
