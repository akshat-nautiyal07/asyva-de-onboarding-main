from main import orders
from pydantic import InstanceOf
import os
import requests
from sqlalchemy import create_engine, text
from typing import Any

API_BASE_URL = os.environ.get("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
DATABASE_URL = os.environ.get("DATABASE_URL")


if not DATABASE_URL:
    raise RuntimeError("Database url is not set")


engine = create_engine(DATABASE_URL)


def fetch_Api_data(endpoint: str):
    response = requests.get(f"{API_BASE_URL}/{endpoint}")
    response.raise_for_status()
    data = response.json()

    if not isinstance(data, list):
        raise RuntimeError("Invalid datatype")
    return data


def create_table():
    with engine.begin() as conn:
        conn.execute(
            text("""
    CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER,
      city TEXT,
      email TEXT UNIQUE
      
    )
    """)
        )
        conn.execute(
            text("""
    CREATE TABLE IF NOT EXISTS products(
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      price INTEGER,
      category TEXT,
      stock INTEGER
    )
    """)
        )
        conn.execute(
            text("""
    CREATE TABLE IF NOT EXISTS orders(
      order_id INTEGER PRIMARY KEY,
      user_id INTEGER,
      product TEXT,
      quantity INTEGER,
      total_price INTEGER,
      status TEXT,
      FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
        )


def ingest_users(users):
    with engine.begin() as conn:
        for user in users:
            conn.execute(
                text("""
      INSERT INTO users (id,name,age,city,email)
      VALUES (:id,:name,:age,:city,:email)
      ON CONFLICT (id) DO UPDATE SET
      name = EXCLUDED.name,
      age = EXCLUDED.age,
      city = EXCLUDED.city,
      email = EXCLUDED.email
      """),
                user,
            )


def ingest_products(products):
    with engine.begin() as conn:
        for product in products:
            conn.execute(
                text("""
      INSERT INTO products (id,name,price,category,stock)
      VALUES (:id,:name,:price,:category,:stock)
      ON CONFLICT (id) DO UPDATE SET
      name = EXCLUDED.name,
      price = EXCLUDED.price,
      category = EXCLUDED.category,
      stock = EXCLUDED.stock
      """),
                product,
            )


def ingest_orders(orders):
    with engine.begin() as conn:
        for order in orders:
            conn.execute(
                text("""
      INSERT INTO orders (order_id,user_id,product,quantity,total_price,status)
      VALUES (:order_id,:user_id,:product,:quantity,:total_price,:status)
      ON CONFLICT (order_id) DO UPDATE SET
      user_id = EXCLUDED.user_id,
      product = EXCLUDED.product,
      quantity = EXCLUDED.quantity,
      total_price = EXCLUDED.total_price,
      status = EXCLUDED.status
      """),
                order,
            )


def main():
    try:
        create_table()

        users = fetch_Api_data("/users")
        products = fetch_Api_data("/products")
        orders = fetch_Api_data("/orders")

        ingest_users(users)
        ingest_products(products)
        ingest_orders(orders)
        print("Data Ingestion taskis completed")
        print(f"User inserted/updated: {len(users)}")
        print(f"Products inserted/updated: {len(products)}")
        print(f"Orders inserted/updated: {len(orders)}")
    except Exception as error:
        print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
