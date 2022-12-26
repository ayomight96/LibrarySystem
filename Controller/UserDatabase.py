import sqlite3

connection =  sqlite3.connect("LibrarySystem.db")
cursor= connection.cursor()
cursor.execute("create table User (id text, name text, userName text, password text, userType text, userStation text, fine real)")

cursor.executemany("insert into User values (?, ?, ?, ?, ?, ?, ?)", [
    ('123', '123', '123', '123', '123', '123', '123'),
    ('124', '123', '123', '123', '123', '123', '123')
])

for row in cursor.execute("select * from User"):
    print (row)

connection.close()