""" extract.py
Fill in implementation.
"""

import pandas as pd
import logging
from google.colab import drive

logging.getLogger(__name__)
drive.mount('/content/drive')


def extract():

  print("------------- EXTRACTING -------------")

  customers = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/etl_customers.csv')
  products = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/etl_products.csv')
  orders = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/etl_orders.csv')
  transactions = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/etl_transactions.csv')

  print(f"Customers: {len(customers)} rows")
  print(f"Products: {len(products)} rows")
  print(f"Orders: {len(orders)} rows")
  print(f"Transactions: {len(transactions)} rows")

  return customers, products, orders, transactions

