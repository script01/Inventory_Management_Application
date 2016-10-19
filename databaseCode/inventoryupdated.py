import sqlite3
import time
import datetime
import sys

conn = sqlite3.connect('Inventory.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS InventoryManagement(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, total_amount_available INTEGER, cost_per_item REAL, date_added TEXT, status INTEGER)')

def add(name, description, total_amount_available, cost_per_item, status):
    unix = time.time()
    date_added = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))

    c.execute("INSERT INTO InventoryManagement(name, description, total_amount_available, cost_per_item, date_added, status) VALUES(?, ?, ?, ?, ?, ?)",(name, description, total_amount_available, cost_per_item, date_added, status))
    conn.commit()
    c.close()
    conn.close()

def remove(item_id):
    c.execute("DELETE FROM InventoryManagement WHERE id = " + item_id)
    conn.commit()
def list():
    c.execute("SELECT * FROM InventoryManagement")
    print(c.fetchall())

def export(file_name):
    data = c.execute("SELECT * FROM InventoryManagement")
    with open(file_name +'.csv', 'Inventory') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'description', 'total_amount_available', 'cost_per_item', 'date_added', 'status'])
        writer.writerows(data)

def checkout(item_id):
    c.execute("UPDATE InventoryManagement SET status = 0 WHERE id = " + item_id)
    conn.commit()

def checkin(item_id):
    c.execute("UPDATE InventoryManagement SET status = 1 WHERE id = " + item_id)
    conn.commit()
def view(item_id):
    c.execute("SELECT * FROM InventoryManagement WHERE id = " + item_id)
    print(c.fetchall())

def search(search_query):
    c.execute(search_query)
    return c.fetchall()
def assetvalue():
    c.execute("SELECT sum(cost_per_item * total_amount_available)")
    print(c.fetchall())

create_table()
add("name", "description", 10, 5.0, 1)

    





    