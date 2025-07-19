# Customer Order Management & Report System

This is a Python-based project that allows you to manage customer details and their orders using a local SQLite database, and generate reports (CSV + graph).

---

## ✅ Features

- Add new customers manually
- Add orders for customers
- View orders of any customer
- Generate report.csv with all order records
- Create a bar chart showing revenue by city (chart.png)

---

## 🛠 Technologies Used

- Python 3
- SQLite (local database)
- Faker (for generating fake customer/order data)
- Matplotlib (for graph plotting)

---

## 📁 Project Structure

Tanushree/
├── setup_db.py ← Creates database and adds fake data
├── main.py ← CLI tool to add/view customers and orders manually
├── generate_reports.py ← Generates report.csv and chart.png
├── view_customers.py ← (Optional) Shows list of customers with IDs
├── orders.db ← SQLite database file
├── report.csv ← Excel report of all orders (generated)
├── chart.png ← Revenue by city graph (generated)
└── README.md ← This instruction file


---


