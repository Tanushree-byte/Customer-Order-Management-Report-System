import sqlite3
import random
from faker import Faker

fake = Faker()

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS orders")

cur.execute('''CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    city TEXT
)''')

cur.execute('''CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)''')

for _ in range(10):
    cur.execute("INSERT INTO customers (name, email, city) VALUES (?, ?, ?)",
                (fake.name(), fake.email(), fake.city()))

for _ in range(50):
    cur.execute("INSERT INTO orders (customer_id, product, quantity, price, date) VALUES (?, ?, ?, ?, ?)", (
        random.randint(1, 10),
        fake.word(),
        random.randint(1, 5),
        round(random.uniform(10.0, 100.0), 2),
        fake.date_this_year().isoformat()
    ))

conn.commit()
conn.close()
print("Database created and filled with fake data.")
