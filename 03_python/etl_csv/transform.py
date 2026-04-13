""" transform.py
Fill in implementation.
"""
import pandas as pd

def transform(customers, orders, products, transactions):
  customers["email"] = customers["email"].fillna(None)
  customers["phone"] = customers["phone"].fillna(None)
  customers["signup_date"] = pd.to_datetime(customers["signup_date"])

  orders["payment_method"] = orders["payment_method"].fillna("Unknown")
  orders["order_date"] = pd.to_datetime(orders["order_date"])
  orders["net_revenue"] = 

  # # Creating a flag for missing ratings
  # products['rating_missing'] = products['rating'].isna()
  avg_rating = round(products['rating'].mean(),1)
  products['rating'] = products['rating'].fillna(avg_rating)

  # Remove any data where price is zero or less than zero
  before_removing = len(products)
  products = products[products["price"] > 1]
  print(f"Product - removed {before_removing - len(products)}")
