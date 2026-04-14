from __future__ import annotations
import os
import requests
import re
from dataclasses import dataclass, field
from typing import Optional, Literal
from sqlalchemy import create_engine, text, true
from pydantic import (
    BaseModel,
    ValidationError,
    EmailStr,
    Field,
    fieldvalidator,
    modelvalidator,
)
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session


DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Database connection failed")

engine = create_engine(DATABASE_URL)


class SourceBase(DeclarativeBase):
    pass


class DestBase(DeclarativeBase):
    pass


class SrcUser(SourceBase):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)
    email = Column(String)


class SrcProduct(SourceBase):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    stock = Column(String)


class SrcOrders(SourceBase):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    product = Column(String)
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String)


class CleanUser(DestBase):
    __tablename__ = "cleaned_user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    email = Column(String, nullable=False)


class CleanProduct(DestBase):
    __tablename__ = "cleaned_products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    stock = Column(String, nullable=False)


class CleanOrders(DestBase):
    __tablename__ = "cleaned_orders"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, nullable=False)


DestBase.metadata.create_all(engine)


class UserSchema(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0, lt=150)
    city: str = Field(..., min_length=3)
    email: EmailStr


class ProductSchema(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    category: str = Field(..., min_length=2)
    stock: int


class OrdersSchema(BaseModel):
    order_id: int
    user_id: int
    product: str = Field(..., min_length=2)
    quantity: int
    total_price: float = Field(..., gt=0)
    status: Literal["pending", "processing", "shipped", "delivered"]


def fetch_all_data():
    with Session(engine) as session:
        users = session.query(SrcUser).all()
        products = session.query(SrcProduct).all()
        orders = session.query(SrcOrders).all()
        session.expunge_all()
    return users, products, orders
