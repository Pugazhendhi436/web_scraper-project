import sqlite3
import pandas as pd

def view_database():
    conn = sqlite3.connect("books.db")
    df = pd.read_sql_query("SELECT * FROM books", conn)
    print(df)
    conn.close()
view_database()