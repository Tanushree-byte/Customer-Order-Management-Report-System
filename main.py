import sqlite3

def add_customer():
    name = input("Name: ")
    email = input("Email: ")
    city = input("City: ")
    with sqlite3.connect('orders.db') as conn:
        conn.execute("INSERT INTO customers (name, email, city) VALUES (?, ?, ?)", (name, email, city))
        print("Customer added.")

def add_order():
    customer_id = int(input("Customer ID: "))
    product = input("Product: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    date = input("Date (YYYY-MM-DD): ")
    with sqlite3.connect('orders.db') as conn:
        conn.execute("INSERT INTO orders (customer_id, product, quantity, price, date) VALUES (?, ?, ?, ?, ?)",
                     (customer_id, product, quantity, price, date))
        print("Order added.")

def view_orders():
    customer_id = int(input("Customer ID: "))
    with sqlite3.connect('orders.db') as conn:
        for row in conn.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,)):
            print(row)

def main():
    while True:
        print("\n1. Add Customer\n2. Add Order\n3. View Orders\n4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            add_order()
        elif choice == '3':
            view_orders()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
