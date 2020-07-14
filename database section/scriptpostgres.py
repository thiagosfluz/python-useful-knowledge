import psycopg2


def create_table():
    # create a connection with database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")

    # create a cursor object
    cur=conn.cursor()

    # query
    cur.execute("CREATE TABLE if not EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #commit changes
    conn.commit()

    conn.close()

def insert(item, quantity, price):
    # create a connection with database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    # create a cursor object
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price)) #not good idea, prone to sql injection attacker

    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",  (item, quantity, price))
    #commit changes
    conn.commit()
    conn.close()

# insert("Water Glass", 10, 5)

def view():
    # create a connection with database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    # create a connection with database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    # create a connection with database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    # create a cursor object
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
insert("Orange", 10, 15)
# delete("Orange")
update(20,15.0, 'apple')

# update(11,6, "Water Glass")
# delete("Wine Glass")

print(view())