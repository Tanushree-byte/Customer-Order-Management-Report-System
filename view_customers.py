import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("SELECT id, name, city FROM customers")
rows = cur.fetchall()

print("\n🧾 Customer List:")
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | City: {row[2]}")

conn.close()

