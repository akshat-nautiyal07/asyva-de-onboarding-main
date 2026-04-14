from fastapi import FastAPI

app = FastAPI()

users = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "age": 21,
        "city": "Delhi",
        "email": "aarav@example.com",
    },
    {
        "id": 2,
        "name": "Priya Verma",
        "age": 23,
        "city": "Lucknow",
        "email": "priya@example.com",
    },
    {
        "id": 3,
        "name": "Rohan Singh",
        "age": 25,
        "city": "Kanpur",
        "email": "rohan@example.com",
    },
    {
        "id": 4,
        "name": "Sneha Gupta",
        "age": 22,
        "city": "Agra",
        "email": "sneha@example.com",
    },
    {
        "id": 5,
        "name": "Vikram Yadav",
        "age": 28,
        "city": "Varanasi",
        "email": "vikram@example.com",
    },
    {
        "id": 6,
        "name": "Ananya Singh",
        "age": 20,
        "city": "Noida",
        "email": "ananya@example.com",
    },
    {
        "id": 7,
        "name": "Rahul Mehta",
        "age": 26,
        "city": "Mumbai",
        "email": "rahul@example.com",
    },
    {
        "id": 8,
        "name": "Kriti Sharma",
        "age": 24,
        "city": "Bangalore",
        "email": "kriti@example.com",
    },
]

products = [
    {
        "id": 101,
        "name": "Laptop",
        "price": 55000,
        "category": "Electronics",
        "stock": 10,
    },
    {
        "id": 102,
        "name": "Smartphone",
        "price": 20000,
        "category": "Electronics",
        "stock": 25,
    },
    {
        "id": 103,
        "name": "Headphones",
        "price": 1500,
        "category": "Accessories",
        "stock": 50,
    },
    {
        "id": 104,
        "name": "Office Chair",
        "price": 7000,
        "category": "Furniture",
        "stock": 15,
    },
    {
        "id": 105,
        "name": "Tablet",
        "price": 18000,
        "category": "Electronics",
        "stock": 12,
    },
    {
        "id": 106,
        "name": "Keyboard",
        "price": 1200,
        "category": "Accessories",
        "stock": 40,
    },
    {"id": 107, "name": "Mouse", "price": 800, "category": "Accessories", "stock": 60},
    {
        "id": 108,
        "name": "Monitor",
        "price": 12000,
        "category": "Electronics",
        "stock": 20,
    },
]


orders = [
    {
        "order_id": 1,
        "user_id": 1,
        "product": "Laptop",
        "quantity": 1,
        "total_price": 55000,
        "status": "delivered",
    },
    {
        "order_id": 2,
        "user_id": 2,
        "product": "Smartphone",
        "quantity": 2,
        "total_price": 40000,
        "status": "shipped",
    },
    {
        "order_id": 3,
        "user_id": 3,
        "product": "Headphones",
        "quantity": 3,
        "total_price": 4500,
        "status": "processing",
    },
    {
        "order_id": 4,
        "user_id": 4,
        "product": "Keyboard",
        "quantity": 1,
        "total_price": 1200,
        "status": "pending",
    },
]


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/users")
async def get_all_users():
    if len(users) > 0:
        return users
    return {"message": "no users are there"}


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message": "User not found"}


@app.get("/products")
async def get_all_products():
    if len(products) > 0:
        return products
    return {"message": "No products are there to show"}


@app.get("/products/{product_id}")
async def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}


@app.get("/orders")
async def get_all_products():
    if len(orders) > 0:
        return orders
    return {"message": "No orders history to show"}


@app.get("/orders/{order_id}")
async def get_order_by_id(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order
    return {"message": "No order found with this id"}
