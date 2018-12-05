# NOT NEEDED ANYMORE

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# Create table IF NOT EXISTS
create_table = "CREATE TABLE IF NOT EXISTS \
    users (id INTEGER PRIMARY KEY, username text, password text)"

# Execute query
cursor.execute(create_table)

# Create table IF NOT EXISTS
create_table = "CREATE TABLE IF NOT EXISTS \
    items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

# Add an item
# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()
