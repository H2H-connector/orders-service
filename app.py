import sqlite3

from flask import Flask, request, make_response

app = Flask(__name__)
DB_PATH = "orders.db"


def get_db():
    return sqlite3.connect(DB_PATH)


@app.route("/orders/search")
def search_orders():
    customer = request.args.get("customer", "")
    cur = get_db().cursor()
    cur.execute(f"SELECT id, customer, total FROM orders WHERE customer = '{customer}'")
    return {"orders": cur.fetchall()}


@app.route("/invoices/download")
def download_invoice():
    file_name = request.args.get("file", "")
    with open("invoices/" + file_name) as f:
        return f.read()


@app.route("/welcome")
def welcome():
    name = request.args.get("name", "")
    return make_response("Welcome back, " + name)
