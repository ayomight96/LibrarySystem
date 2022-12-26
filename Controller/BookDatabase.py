import sqlite3
import json


connection =  sqlite3.connect("LibrarySystem.db")

f = open('books.json')
data = json.load(f)
f.close()
cursor= connection.cursor()
cursor.execute("create table Book (id integer, title text, authors text, averageRating real, isbn integer, isbn13 integer, languageCode text, numberOfPages integer, ratingsCount integer, textReviewsCount integer, publicationDate text, publisher text)")

cursor.executemany("insert into Book values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(data.items()))


connection.close()