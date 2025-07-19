import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('orders.db', check_same_thread=False)
cur = conn.cursor()

st.title("📦 Customer Order Management System")

# Tabs
tab1, tab2, tab3 = st.tabs(["➕ Add Customer", "➕ Add Order", "📄 View Orders"])

# --- Tab 1: Add Customer ---
with tab1:
    st.header("Add New Customer")
    name = st.text_input("Customer Name")
    email = st.text_input("Email")
    city = st.text_input("City")
    if st.button("Add Customer"):
        cur.execute("INSERT INTO customers (name, email, city) VALUES (?, ?, ?)", (name, email, city))
        conn.commit()
        st.success("Customer added successfully!")

# --- Tab 2: Add Order ---
with tab2:
    st.header("Add New Order")
    customers = cur.execute("SELECT id, name FROM customers").fetchall()
    customer_list = [f"{c[0]} - {c[1]}" for c in customers]
    selected = st.selectbox("Select Customer", customer_list)
    customer_id = int(selected.split(" - ")[0])

    product = st.text_input("Product")
    quantity = st.number_input("Quantity", min_value=1)
    price = st.number_input("Price", min_value=0.0)
    date = st.date_input("Order Date")

    if st.button("Add Order"):
        cur.execute("INSERT INTO orders (customer_id, product, quantity, price, date) VALUES (?, ?, ?, ?, ?)",
                    (customer_id, product, quantity, price, date.isoformat()))
        conn.commit()
        st.success("Order added successfully!")

# --- Tab 3: View All Orders ---
with tab3:
    st.header("All Orders (with Customer Info)")
    query = """
    SELECT customers.name, customers.city, orders.product, orders.quantity, orders.price, orders.date
    FROM orders
    JOIN customers ON orders.customer_id = customers.id
    """
    df = pd.read_sql_query(query, conn)
    st.dataframe(df)