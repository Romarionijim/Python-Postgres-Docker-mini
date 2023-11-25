import psycopg2
from data_base import DataBase
from user_data import UserData

db = DataBase(
    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres"
)

user_data = UserData(db)
result = user_data.get_users()
print(result)


# conn = psycopg2.connect (
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="postgres",
# )

# cur = conn.cursor()

# cur.execute("SELECT * FROM users;")
# users_row = cur.fetchall()

# cur.execute("SELECT * FROM orders;")
# orders_rows = cur.fetchall()

# cur.execute("SELECT * FROM products;")
# products_rows = cur.fetchall()

# print("Users:")
# for row in users_row:
#     print(row)

# print("\nOrders:")
# for row in orders_rows:
#     print(row)

# print("\nProducts:")
# for row in products_rows:
#     print(row)

# cur.execute("SELECT users.user_id, orders.user_id FROM users JOIN orders on users.user_id = orders.user_id")
# users_join_orders = cur.fetchall()
# print(f'result of joinin the two tables are {users_join_orders}')


# conn.commit()

# conn.close()
