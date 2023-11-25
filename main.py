import psycopg2

conn = psycopg2.connect (
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
)

cur = conn.cursor()

cur.execute("SELECT * FROM users;")
users_row = cur.fetchall()

cur.execute("SELECT * FROM orders;")
orders_rows = cur.fetchall()

cur.execute("SELECT * FROM products;")
products_rows = cur.fetchall()

print("Users:")
for row in users_row:
    print(row)

print("\nOrders:")
for row in orders_rows:
    print(row)

print("\nProducts:")
for row in products_rows:
    print(row)

conn.close()
