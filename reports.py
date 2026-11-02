import sqlite3

DB_PATH = "orders.db"


def orders_by_status(status):
    cur = sqlite3.connect(DB_PATH).cursor()
    cur.execute(f"SELECT id, customer, total FROM orders WHERE status = '{status}'")
    return cur.fetchall()


if __name__ == "__main__":
    print(orders_by_status("pending"))
