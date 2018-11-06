import sqlite3


def commit(db_location: str, text: str):
    length = len(text.split(" "))

    conn = sqlite3.connect(db_location)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS TotalCount (id INTEGER PRIMARY KEY, count INTEGER)')
    c.execute('UPDATE TotalCount SET count = count + {length}'.format(length=length))
    conn.commit()
    conn.close()


def query_table():
    conn = sqlite3.connect(db_location)
    c = conn.cursor()
    # c.execute("")
    # conn.commit()
    conn.close()
