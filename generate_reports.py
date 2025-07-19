import sqlite3
import csv
import matplotlib.pyplot as plt

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute('''SELECT customers.name, customers.city, orders.product, orders.quantity,
                      orders.price, orders.date
               FROM orders
               JOIN customers ON orders.customer_id = customers.id''')
rows = cur.fetchall()

with open('report.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer', 'City', 'Product', 'Quantity', 'Price', 'Date'])
    writer.writerows(rows)

cur.execute('''SELECT customers.city, SUM(orders.quantity * orders.price)
               FROM orders
               JOIN customers ON orders.customer_id = customers.id
               GROUP BY customers.city''')
data = cur.fetchall()

cities, revenues = zip(*data)
plt.bar(cities, revenues)
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.title('Revenue by City')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart.png')
print("Reports generated.")
