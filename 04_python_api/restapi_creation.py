### ********** THIS FAKE/SAMPLE DATA IS CREATED USING THE CHATGPT AND CLAUDE **********


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
    {
        "id": 9,
        "name": "Amit Patel",
        "age": None,
        "city": "Surat",
        "email": "amit@example.com",
    },  # ❌ age
    {
        "id": 10,
        "name": "Deepika Nair",
        "age": 27,
        "city": None,
        "email": "deepika@example.com",
    },  # ❌ city
    {
        "id": 11,
        "name": "Suresh Kumar",
        "age": 30,
        "city": "Chennai",
        "email": None,
    },  # ❌ email
    {
        "id": 12,
        "name": None,
        "age": 19,
        "city": "Pune",
        "email": "unknown12@example.com",
    },  # ❌ name
    {
        "id": 13,
        "name": "Nisha Joshi",
        "age": None,
        "city": None,
        "email": "nisha@example.com",
    },  # ❌ age, city
    {
        "id": 14,
        "name": "Karan Malhotra",
        "age": 33,
        "city": "Jaipur",
        "email": "karan@example.com",
    },
    {
        "id": 15,
        "name": "Pooja Reddy",
        "age": 29,
        "city": "Hyderabad",
        "email": None,
    },  # ❌ email
    {
        "id": 16,
        "name": "Arjun Bose",
        "age": 22,
        "city": "Kolkata",
        "email": "arjun@example.com",
    },
    {
        "id": 17,
        "name": "Meera Iyer",
        "age": None,
        "city": "Coimbatore",
        "email": "meera@example.com",
    },  # ❌ age
    {
        "id": 18,
        "name": "Tushar Desai",
        "age": 31,
        "city": "Ahmedabad",
        "email": "tushar@example.com",
    },
    {
        "id": 19,
        "name": None,
        "age": 24,
        "city": "Bhopal",
        "email": None,
    },  # ❌ name, email
    {
        "id": 20,
        "name": "Riya Chauhan",
        "age": 26,
        "city": "Indore",
        "email": "riya@example.com",
    },
    {
        "id": 21,
        "name": "Naveen Pillai",
        "age": 35,
        "city": None,
        "email": "naveen@example.com",
    },  # ❌ city
    {
        "id": 22,
        "name": "Sakshi Tiwari",
        "age": 21,
        "city": "Allahabad",
        "email": "sakshi@example.com",
    },
    {
        "id": 23,
        "name": "Harish Rao",
        "age": None,
        "city": "Vizag",
        "email": None,
    },  # ❌ age, email
    {
        "id": 24,
        "name": "Divya Menon",
        "age": 28,
        "city": "Kochi",
        "email": "divya@example.com",
    },
    {
        "id": 25,
        "name": "Ajay Tripathi",
        "age": 32,
        "city": "Gorakhpur",
        "email": "ajay@example.com",
    },
    {
        "id": 26,
        "name": None,
        "age": 20,
        "city": "Meerut",
        "email": "xyz26@example.com",
    },  # ❌ name
    {
        "id": 27,
        "name": "Swati Pandey",
        "age": 27,
        "city": None,
        "email": "swati@example.com",
    },  # ❌ city
    {
        "id": 28,
        "name": "Rohit Saxena",
        "age": 23,
        "city": "Aligarh",
        "email": "rohit@example.com",
    },
    {
        "id": 29,
        "name": "Preeti Shukla",
        "age": None,
        "city": "Bareilly",
        "email": "preeti@example.com",
    },  # ❌ age
    {
        "id": 30,
        "name": "Gaurav Jain",
        "age": 29,
        "city": "Mathura",
        "email": None,
    },  # ❌ email
    {
        "id": 31,
        "name": "Sonal Mishra",
        "age": 22,
        "city": "Patna",
        "email": "sonal@example.com",
    },
    {
        "id": 32,
        "name": "Deepak Verma",
        "age": None,
        "city": "Ranchi",
        "email": "deepak@example.com",
    },  # ❌ age
    {
        "id": 33,
        "name": "Kavita Yadav",
        "age": 34,
        "city": None,
        "email": "kavita@example.com",
    },  # ❌ city
    {
        "id": 34,
        "name": "Manish Tomar",
        "age": 27,
        "city": "Gurgaon",
        "email": None,
    },  # ❌ email
    {
        "id": 35,
        "name": None,
        "age": 31,
        "city": "Faridabad",
        "email": "user35@example.com",
    },  # ❌ name
    {
        "id": 36,
        "name": "Priyanka Das",
        "age": 25,
        "city": "Guwahati",
        "email": "priyanka@example.com",
    },
    {
        "id": 37,
        "name": "Sandeep Nair",
        "age": None,
        "city": None,
        "email": "sandeep@example.com",
    },  # ❌ age, city
    {
        "id": 38,
        "name": "Ankita Joshi",
        "age": 23,
        "city": "Nashik",
        "email": "ankita@example.com",
    },
    {
        "id": 39,
        "name": "Vivek Rathore",
        "age": 36,
        "city": "Udaipur",
        "email": None,
    },  # ❌ email
    {
        "id": 40,
        "name": "Pallavi Singh",
        "age": 28,
        "city": "Nagpur",
        "email": "pallavi@example.com",
    },
    {
        "id": 41,
        "name": "Ravi Shankar",
        "age": 40,
        "city": "Mysore",
        "email": "ravi@example.com",
    },
    {
        "id": 42,
        "name": None,
        "age": None,
        "city": "Srinagar",
        "email": "user42@example.com",
    },  # ❌ name, age
    {
        "id": 43,
        "name": "Isha Kapoor",
        "age": 22,
        "city": "Chandigarh",
        "email": "isha@example.com",
    },
    {
        "id": 44,
        "name": "Mohit Bansal",
        "age": 29,
        "city": None,
        "email": "mohit@example.com",
    },  # ❌ city
    {
        "id": 45,
        "name": "Ritika Saxena",
        "age": 26,
        "city": "Jodhpur",
        "email": None,
    },  # ❌ email
    {
        "id": 46,
        "name": "Pankaj Mehta",
        "age": None,
        "city": "Amritsar",
        "email": "pankaj@example.com",
    },  # ❌ age
    {
        "id": 47,
        "name": "Neha Agarwal",
        "age": 24,
        "city": "Dehradun",
        "email": "neha@example.com",
    },
    {
        "id": 48,
        "name": "Saurabh Pal",
        "age": 33,
        "city": "Raipur",
        "email": "saurabh@example.com",
    },
    {
        "id": 49,
        "name": "Tanvi Kulkarni",
        "age": None,
        "city": "Pune",
        "email": None,
    },  # ❌ age, email
    {
        "id": 50,
        "name": "Alok Srivastava",
        "age": 38,
        "city": "Lucknow",
        "email": "alok@example.com",
    },
    {
        "id": 51,
        "name": "Simran Kaur",
        "age": 21,
        "city": "Ludhiana",
        "email": "simran@example.com",
    },
    {
        "id": 52,
        "name": None,
        "age": 25,
        "city": "Jalandhar",
        "email": "user52@example.com",
    },  # ❌ name
    {
        "id": 53,
        "name": "Rahul Khanna",
        "age": 30,
        "city": None,
        "email": "rahulk@example.com",
    },  # ❌ city
    {
        "id": 54,
        "name": "Geeta Bhatt",
        "age": 27,
        "city": "Shimla",
        "email": None,
    },  # ❌ email
    {
        "id": 55,
        "name": "Abhishek Roy",
        "age": None,
        "city": "Kolkata",
        "email": "abhishek@example.com",
    },  # ❌ age
    {
        "id": 56,
        "name": "Vandana Tiwari",
        "age": 32,
        "city": "Varanasi",
        "email": "vandana@example.com",
    },
    {
        "id": 57,
        "name": "Nitin Chandra",
        "age": 28,
        "city": "Agra",
        "email": None,
    },  # ❌ email
    {
        "id": 58,
        "name": "Shruti Agarwal",
        "age": None,
        "city": None,
        "email": "shruti@example.com",
    },  # ❌ age, city
    {
        "id": 59,
        "name": None,
        "age": 22,
        "city": "Meerut",
        "email": None,
    },  # ❌ name, email
    {
        "id": 60,
        "name": "Yash Malviya",
        "age": 26,
        "city": "Gwalior",
        "email": "yash@example.com",
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
    {
        "id": 109,
        "name": "Webcam",
        "price": None,
        "category": "Accessories",
        "stock": 35,
    },  # ❌ price
    {
        "id": 110,
        "name": "Printer",
        "price": 8500,
        "category": None,
        "stock": 18,
    },  # ❌ category
    {
        "id": 111,
        "name": "USB Hub",
        "price": 600,
        "category": "Accessories",
        "stock": None,
    },  # ❌ stock
    {
        "id": 112,
        "name": None,
        "price": 3200,
        "category": "Electronics",
        "stock": 22,
    },  # ❌ name
    {
        "id": 113,
        "name": "External SSD",
        "price": 6000,
        "category": "Storage",
        "stock": 30,
    },
    {
        "id": 114,
        "name": "Gaming Mouse",
        "price": None,
        "category": "Gaming",
        "stock": 45,
    },  # ❌ price
    {
        "id": 115,
        "name": "Mechanical Keyboard",
        "price": 4500,
        "category": "Gaming",
        "stock": None,
    },  # ❌ stock
    {
        "id": 116,
        "name": "Smart Watch",
        "price": 15000,
        "category": None,
        "stock": 20,
    },  # ❌ category
    {
        "id": 117,
        "name": "Desk Lamp",
        "price": 900,
        "category": "Furniture",
        "stock": 70,
    },
    {
        "id": 118,
        "name": "Laptop Stand",
        "price": 1800,
        "category": "Accessories",
        "stock": 55,
    },
    {
        "id": 119,
        "name": None,
        "price": None,
        "category": "Electronics",
        "stock": 10,
    },  # ❌ name, price
    {"id": 120, "name": "Microphone", "price": 5000, "category": "Audio", "stock": 25},
    {
        "id": 121,
        "name": "Speaker",
        "price": 3000,
        "category": "Audio",
        "stock": None,
    },  # ❌ stock
    {"id": 122, "name": "Router", "price": 2500, "category": "Networking", "stock": 30},
    {
        "id": 123,
        "name": "Graphics Card",
        "price": None,
        "category": "Electronics",
        "stock": 8,
    },  # ❌ price
    {
        "id": 124,
        "name": "RAM 16GB",
        "price": 4200,
        "category": None,
        "stock": 40,
    },  # ❌ category
    {
        "id": 125,
        "name": "Gaming Chair",
        "price": 12000,
        "category": "Furniture",
        "stock": 10,
    },
    {
        "id": 126,
        "name": "Portable Charger",
        "price": 1500,
        "category": "Accessories",
        "stock": 80,
    },
    {
        "id": 127,
        "name": "Smart TV 43inch",
        "price": 35000,
        "category": "Electronics",
        "stock": 7,
    },
    {
        "id": 128,
        "name": "Air Purifier",
        "price": None,
        "category": "Appliances",
        "stock": 14,
    },  # ❌ price
    {
        "id": 129,
        "name": "Electric Kettle",
        "price": 1200,
        "category": None,
        "stock": 50,
    },  # ❌ category
    {
        "id": 130,
        "name": "Coffee Maker",
        "price": 3500,
        "category": "Appliances",
        "stock": None,
    },  # ❌ stock
    {
        "id": 131,
        "name": None,
        "price": 2800,
        "category": "Appliances",
        "stock": 20,
    },  # ❌ name
    {
        "id": 132,
        "name": "Noise Cancelling Earbuds",
        "price": 8000,
        "category": "Audio",
        "stock": 30,
    },
    {
        "id": 133,
        "name": "Fitness Band",
        "price": 2500,
        "category": None,
        "stock": 45,
    },  # ❌ category
    {
        "id": 134,
        "name": "Drone",
        "price": None,
        "category": "Electronics",
        "stock": 5,
    },  # ❌ price
    {
        "id": 135,
        "name": "DSLR Camera",
        "price": 45000,
        "category": "Photography",
        "stock": None,
    },  # ❌ stock
    {
        "id": 136,
        "name": "Tripod Stand",
        "price": 2200,
        "category": "Photography",
        "stock": 25,
    },
    {
        "id": 137,
        "name": "Ethernet Cable 10m",
        "price": 350,
        "category": "Networking",
        "stock": 100,
    },
    {
        "id": 138,
        "name": None,
        "price": None,
        "category": None,
        "stock": None,
    },  # ❌ name, price, category, stock
    {"id": 139, "name": "SSD 500GB", "price": 5500, "category": "Storage", "stock": 35},
    {
        "id": 140,
        "name": "Cooling Pad",
        "price": 900,
        "category": "Accessories",
        "stock": 60,
    },
    {
        "id": 141,
        "name": "Projector",
        "price": 28000,
        "category": "Electronics",
        "stock": 6,
    },
    {
        "id": 142,
        "name": "VR Headset",
        "price": None,
        "category": "Gaming",
        "stock": 9,
    },  # ❌ price
    {
        "id": 143,
        "name": "Gaming Headset",
        "price": 3500,
        "category": "Gaming",
        "stock": None,
    },  # ❌ stock
    {
        "id": 144,
        "name": "Smartpad",
        "price": 7500,
        "category": None,
        "stock": 18,
    },  # ❌ category
    {
        "id": 145,
        "name": "Blu-ray Player",
        "price": 9000,
        "category": "Electronics",
        "stock": 12,
    },
    {
        "id": 146,
        "name": None,
        "price": 1100,
        "category": "Accessories",
        "stock": 75,
    },  # ❌ name
    {
        "id": 147,
        "name": "Drawing Tablet",
        "price": 6500,
        "category": "Accessories",
        "stock": 20,
    },
    {
        "id": 148,
        "name": "E-Reader",
        "price": 8000,
        "category": "Electronics",
        "stock": None,
    },  # ❌ stock
    {
        "id": 149,
        "name": "Pocket Projector",
        "price": None,
        "category": "Electronics",
        "stock": 8,
    },  # ❌ price
    {
        "id": 150,
        "name": "Smart Bulb Pack",
        "price": 1800,
        "category": "Smart Home",
        "stock": 60,
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
    {
        "order_id": 5,
        "user_id": 5,
        "product": "Tablet",
        "quantity": 1,
        "total_price": 18000,
        "status": "delivered",
    },
    {
        "order_id": 6,
        "user_id": 6,
        "product": "Mouse",
        "quantity": 2,
        "total_price": 1600,
        "status": "shipped",
    },
    {
        "order_id": 7,
        "user_id": 7,
        "product": "Monitor",
        "quantity": 1,
        "total_price": 12000,
        "status": "delivered",
    },
    {
        "order_id": 8,
        "user_id": 8,
        "product": "Office Chair",
        "quantity": 1,
        "total_price": 7000,
        "status": "processing",
    },
    {
        "order_id": 9,
        "user_id": 9,
        "product": "Laptop",
        "quantity": None,
        "total_price": None,
        "status": "pending",
    },  # ❌ quantity, total_price
    {
        "order_id": 10,
        "user_id": 10,
        "product": None,
        "quantity": 1,
        "total_price": 1500,
        "status": "shipped",
    },  # ❌ product
    {
        "order_id": 11,
        "user_id": 11,
        "product": "Webcam",
        "quantity": 2,
        "total_price": None,
        "status": "processing",
    },  # ❌ total_price
    {
        "order_id": 12,
        "user_id": 12,
        "product": "Speaker",
        "quantity": 1,
        "total_price": 3000,
        "status": None,
    },  # ❌ status
    {
        "order_id": 13,
        "user_id": 13,
        "product": "Microphone",
        "quantity": 1,
        "total_price": 5000,
        "status": "delivered",
    },
    {
        "order_id": 14,
        "user_id": 14,
        "product": "USB Hub",
        "quantity": 3,
        "total_price": 1800,
        "status": "shipped",
    },
    {
        "order_id": 15,
        "user_id": 15,
        "product": None,
        "quantity": 2,
        "total_price": None,
        "status": "pending",
    },  # ❌ product, total_price
    {
        "order_id": 16,
        "user_id": 16,
        "product": "Router",
        "quantity": 1,
        "total_price": 2500,
        "status": "delivered",
    },
    {
        "order_id": 17,
        "user_id": 17,
        "product": "RAM 16GB",
        "quantity": None,
        "total_price": 4200,
        "status": "processing",
    },  # ❌ quantity
    {
        "order_id": 18,
        "user_id": 18,
        "product": "External SSD",
        "quantity": 2,
        "total_price": 12000,
        "status": "shipped",
    },
    {
        "order_id": 19,
        "user_id": 19,
        "product": "Desk Lamp",
        "quantity": 1,
        "total_price": 900,
        "status": None,
    },  # ❌ status
    {
        "order_id": 20,
        "user_id": 20,
        "product": "Gaming Mouse",
        "quantity": 1,
        "total_price": None,
        "status": "pending",
    },  # ❌ total_price
    {
        "order_id": 21,
        "user_id": 21,
        "product": "Smart Watch",
        "quantity": 1,
        "total_price": 15000,
        "status": "delivered",
    },
    {
        "order_id": 22,
        "user_id": 22,
        "product": "Laptop Stand",
        "quantity": 2,
        "total_price": 3600,
        "status": "shipped",
    },
    {
        "order_id": 23,
        "user_id": 23,
        "product": None,
        "quantity": None,
        "total_price": None,
        "status": "pending",
    },  # ❌ product, quantity, total_price
    {
        "order_id": 24,
        "user_id": 24,
        "product": "Graphics Card",
        "quantity": 1,
        "total_price": None,
        "status": "processing",
    },  # ❌ total_price
    {
        "order_id": 25,
        "user_id": 25,
        "product": "Gaming Chair",
        "quantity": 1,
        "total_price": 12000,
        "status": "delivered",
    },
    {
        "order_id": 26,
        "user_id": 1,
        "product": "Keyboard",
        "quantity": 2,
        "total_price": 2400,
        "status": "shipped",
    },
    {
        "order_id": 27,
        "user_id": 3,
        "product": "Headphones",
        "quantity": 1,
        "total_price": 1500,
        "status": None,
    },  # ❌ status
    {
        "order_id": 28,
        "user_id": 5,
        "product": "Smartphone",
        "quantity": 1,
        "total_price": 20000,
        "status": "delivered",
    },
    {
        "order_id": 29,
        "user_id": 7,
        "product": "Tablet",
        "quantity": None,
        "total_price": 18000,
        "status": "processing",
    },  # ❌ quantity
    {
        "order_id": 30,
        "user_id": 9,
        "product": "Monitor",
        "quantity": 1,
        "total_price": 12000,
        "status": "shipped",
    },
    {
        "order_id": 31,
        "user_id": 26,
        "product": "Portable Charger",
        "quantity": 2,
        "total_price": 3000,
        "status": "delivered",
    },
    {
        "order_id": 32,
        "user_id": 27,
        "product": "Smart TV 43inch",
        "quantity": 1,
        "total_price": 35000,
        "status": "shipped",
    },
    {
        "order_id": 33,
        "user_id": 28,
        "product": "Air Purifier",
        "quantity": 1,
        "total_price": None,
        "status": "processing",
    },  # ❌ total_price
    {
        "order_id": 34,
        "user_id": 29,
        "product": None,
        "quantity": 1,
        "total_price": 1200,
        "status": "delivered",
    },  # ❌ product
    {
        "order_id": 35,
        "user_id": 30,
        "product": "Coffee Maker",
        "quantity": 1,
        "total_price": 3500,
        "status": None,
    },  # ❌ status
    {
        "order_id": 36,
        "user_id": 31,
        "product": "Noise Cancelling Earbuds",
        "quantity": 1,
        "total_price": 8000,
        "status": "delivered",
    },
    {
        "order_id": 37,
        "user_id": 32,
        "product": "Fitness Band",
        "quantity": 2,
        "total_price": 5000,
        "status": "shipped",
    },
    {
        "order_id": 38,
        "user_id": 33,
        "product": "Drone",
        "quantity": None,
        "total_price": None,
        "status": "pending",
    },  # ❌ quantity, total_price
    {
        "order_id": 39,
        "user_id": 34,
        "product": "DSLR Camera",
        "quantity": 1,
        "total_price": 45000,
        "status": "delivered",
    },
    {
        "order_id": 40,
        "user_id": 35,
        "product": "Tripod Stand",
        "quantity": 2,
        "total_price": 4400,
        "status": "shipped",
    },
    {
        "order_id": 41,
        "user_id": 36,
        "product": "SSD 500GB",
        "quantity": 1,
        "total_price": 5500,
        "status": "delivered",
    },
    {
        "order_id": 42,
        "user_id": 37,
        "product": "Cooling Pad",
        "quantity": 3,
        "total_price": 2700,
        "status": "processing",
    },
    {
        "order_id": 43,
        "user_id": 38,
        "product": "Projector",
        "quantity": 1,
        "total_price": None,
        "status": "pending",
    },  # ❌ total_price
    {
        "order_id": 44,
        "user_id": 39,
        "product": "VR Headset",
        "quantity": 1,
        "total_price": None,
        "status": "shipped",
    },  # ❌ total_price
    {
        "order_id": 45,
        "user_id": 40,
        "product": "Gaming Headset",
        "quantity": 2,
        "total_price": 7000,
        "status": "delivered",
    },
    {
        "order_id": 46,
        "user_id": 41,
        "product": "Drawing Tablet",
        "quantity": 1,
        "total_price": 6500,
        "status": "processing",
    },
    {
        "order_id": 47,
        "user_id": 42,
        "product": None,
        "quantity": None,
        "total_price": None,
        "status": None,
    },  # ❌ product, quantity, total_price, status
    {
        "order_id": 48,
        "user_id": 43,
        "product": "E-Reader",
        "quantity": 1,
        "total_price": 8000,
        "status": "delivered",
    },
    {
        "order_id": 49,
        "user_id": 44,
        "product": "Smart Bulb Pack",
        "quantity": 3,
        "total_price": 5400,
        "status": "shipped",
    },
    {
        "order_id": 50,
        "user_id": 45,
        "product": "Laptop",
        "quantity": 1,
        "total_price": 55000,
        "status": "delivered",
    },
    {
        "order_id": 51,
        "user_id": 46,
        "product": "Ethernet Cable 10m",
        "quantity": 5,
        "total_price": 1750,
        "status": "shipped",
    },
    {
        "order_id": 52,
        "user_id": 47,
        "product": "Mechanical Keyboard",
        "quantity": 1,
        "total_price": 4500,
        "status": None,
    },  # ❌ status
    {
        "order_id": 53,
        "user_id": 48,
        "product": "Printer",
        "quantity": 1,
        "total_price": 8500,
        "status": "processing",
    },
    {
        "order_id": 54,
        "user_id": 49,
        "product": "Smartphone",
        "quantity": None,
        "total_price": 20000,
        "status": "pending",
    },  # ❌ quantity
    {
        "order_id": 55,
        "user_id": 50,
        "product": "USB Hub",
        "quantity": 2,
        "total_price": 1200,
        "status": "delivered",
    },
    {
        "order_id": 56,
        "user_id": 51,
        "product": "Monitor",
        "quantity": 1,
        "total_price": 12000,
        "status": "shipped",
    },
    {
        "order_id": 57,
        "user_id": 52,
        "product": "Office Chair",
        "quantity": 2,
        "total_price": None,
        "status": "processing",
    },  # ❌ total_price
    {
        "order_id": 58,
        "user_id": 53,
        "product": "Tablet",
        "quantity": 1,
        "total_price": 18000,
        "status": "delivered",
    },
    {
        "order_id": 59,
        "user_id": 54,
        "product": None,
        "quantity": 1,
        "total_price": 900,
        "status": "shipped",
    },  # ❌ product
    {
        "order_id": 60,
        "user_id": 55,
        "product": "Keyboard",
        "quantity": 3,
        "total_price": 3600,
        "status": "delivered",
    },
    {
        "order_id": 61,
        "user_id": 56,
        "product": "Mouse",
        "quantity": 4,
        "total_price": 3200,
        "status": "shipped",
    },
    {
        "order_id": 62,
        "user_id": 57,
        "product": "Headphones",
        "quantity": 2,
        "total_price": None,
        "status": "pending",
    },  # ❌ total_price
    {
        "order_id": 63,
        "user_id": 58,
        "product": "Webcam",
        "quantity": 1,
        "total_price": 2200,
        "status": "delivered",
    },
    {
        "order_id": 64,
        "user_id": 59,
        "product": "Smart Watch",
        "quantity": 1,
        "total_price": None,
        "status": None,
    },  # ❌ total_price, status
    {
        "order_id": 65,
        "user_id": 60,
        "product": "Laptop Stand",
        "quantity": 2,
        "total_price": 3600,
        "status": "processing",
    },
    {
        "order_id": 66,
        "user_id": 2,
        "product": "Desk Lamp",
        "quantity": 1,
        "total_price": 900,
        "status": "delivered",
    },
    {
        "order_id": 67,
        "user_id": 4,
        "product": "Router",
        "quantity": 1,
        "total_price": 2500,
        "status": None,
    },  # ❌ status
    {
        "order_id": 68,
        "user_id": 6,
        "product": "Portable Charger",
        "quantity": None,
        "total_price": None,
        "status": "shipped",
    },  # ❌ quantity, total_price
    {
        "order_id": 69,
        "user_id": 8,
        "product": "Fitness Band",
        "quantity": 1,
        "total_price": 2500,
        "status": "delivered",
    },
    {
        "order_id": 70,
        "user_id": 10,
        "product": "Coffee Maker",
        "quantity": 2,
        "total_price": 7000,
        "status": "processing",
    },
    {
        "order_id": 71,
        "user_id": 12,
        "product": "Noise Cancelling Earbuds",
        "quantity": 1,
        "total_price": 8000,
        "status": "shipped",
    },
    {
        "order_id": 72,
        "user_id": 14,
        "product": "Projector",
        "quantity": 1,
        "total_price": 28000,
        "status": "delivered",
    },
    {
        "order_id": 73,
        "user_id": 16,
        "product": "Gaming Chair",
        "quantity": 1,
        "total_price": None,
        "status": "pending",
    },  # ❌ total_price
    {
        "order_id": 74,
        "user_id": 18,
        "product": "External SSD",
        "quantity": 1,
        "total_price": 6000,
        "status": "shipped",
    },
    {
        "order_id": 75,
        "user_id": 20,
        "product": "Graphics Card",
        "quantity": None,
        "total_price": None,
        "status": "processing",
    },  # ❌ quantity, total_price
    {
        "order_id": 76,
        "user_id": 22,
        "product": "RAM 16GB",
        "quantity": 2,
        "total_price": 8400,
        "status": "delivered",
    },
    {
        "order_id": 77,
        "user_id": 24,
        "product": "Smart TV 43inch",
        "quantity": 1,
        "total_price": 35000,
        "status": "shipped",
    },
    {
        "order_id": 78,
        "user_id": 26,
        "product": None,
        "quantity": 1,
        "total_price": 5500,
        "status": "delivered",
    },  # ❌ product
    {
        "order_id": 79,
        "user_id": 28,
        "product": "Microphone",
        "quantity": 2,
        "total_price": 10000,
        "status": None,
    },  # ❌ status
    {
        "order_id": 80,
        "user_id": 30,
        "product": "E-Reader",
        "quantity": 1,
        "total_price": 8000,
        "status": "processing",
    },
]


@app.get("/")
async def root():
    return {"message": "Hello from server checking whether api is sending the response."}


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
