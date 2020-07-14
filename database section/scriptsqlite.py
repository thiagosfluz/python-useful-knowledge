import sqlite3


def create_table():
    # create a connection with database
    conn=sqlite3.connect("lite.db")

    # create a cursor object
    cur=conn.cursor()

    # query
    cur.execute("CREATE TABLE if not EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #commit changes
    conn.commit()

    conn.close()

def insert(item, quantity, price):
    # create a connection with database
    conn = sqlite3.connect("lite.db")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    #commit changes
    conn.commit()
    conn.close()

insert("Water Glass", 10, 5)

def view():
    # create a connection with database
    conn = sqlite3.connect("lite.db")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    # create a connection with database
    conn = sqlite3.connect("lite.db")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    # create a connection with database
    conn = sqlite3.connect("lite.db")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

update(11,6, "Water Glass")
# delete("Wine Glass")

print(view())