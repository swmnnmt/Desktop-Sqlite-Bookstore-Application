import sqlite3


def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title TEXT, author TEXT, year INTEGER, ISBN INTEGER)")
    connection.commit()
    connection.close()


def insert(title, author, year, ISBN):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES(NULL ,?,?,?,?)", (title, author, year, ISBN))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    result = cursor.fetchall()
    connection.close()
    return result


def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=?", (title, author, year, isbn))
    result = cursor.fetchall()
    connection.close()
    return result


def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?,author=?,year=?,ISBN=? WHERE id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()
