import sqlite3


def commit(db_location: str, text: str):
    conn = sqlite3.connect(db_location)
    c = conn.cursor()
    # c.execute("")
    # conn.commit()
    conn.close()


def query_table():
    conn = sqlite3.connect(db_location)
    c = conn.cursor()
    # c.execute("")
    # conn.commit()
    conn.close()
