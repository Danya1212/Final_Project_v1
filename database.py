import sqlite3


def create_db():
    connection = sqlite3.connect("dealership.db")
    data = """CREATE TABLE IF NOT EXISTS catalog(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                equipment TEXT NOT NULL,
                top_speed TEXT NOT NULL,
                acceleration TEXT NOT NULL,
                consumption TEXT NOT NULL,
                weight TEXT NOT NULL,
                seats INTEGER NOT NULL,
                color TEXT NOT NULL,
                type_car TEXT NOT NULL,
                car TEXT NOT NULL
                );"""
    cursor = connection.cursor()
    cursor.execute(data)
    connection.commit()
    connection.close()
    print("Table create successfully")


def create_db_conn():
    connection = sqlite3.connect("dealership.db")
    connection.row_factory = sqlite3.Row
    return connection
