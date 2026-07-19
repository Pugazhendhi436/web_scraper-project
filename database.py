
import sqlite3
import pandas as pd


def save_database(products):

    conn = sqlite3.connect("books.db")

    df = pd.DataFrame(products)

    df.to_sql(
        "books",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database Saved")