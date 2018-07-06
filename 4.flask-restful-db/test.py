import sqlite3  # sqlite and sqlite3 are internal packages with python

# create connection, data.db is the file connection string
connection = sqlite3.connect("data.db")

cursor = connection.cursor()  # create the cursor object

# sql string
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "Jasen", "1234")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# sqlite can auto fill the user into the query
cursor.execute(insert_query, user)

users = [
    (2, "Foo", "1234"),
    (3, "Bar", "1234"),
    (4, "Baz", "1234")
]

cursor.executemany(insert_query, users)

connection.commit()  # when write or save to a db, we need to commit it

select_query = "SELECT * from users"

result = cursor.execute(select_query)
for row in result:
    print(row)

connection.close()  # bast practise
