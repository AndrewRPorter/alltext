import os
import sqlite3


def commit(db_location: str, text: str):
    # create file if it does not exist
    if not os.path.exists(db_location):
        f = open(db_location, "w")
        f.close()

    word_count, use_count = query_table(db_location)

    # increment word_count and use_count in database
    word_count += len(text.split(" "))
    use_count += 1

    conn = sqlite3.connect(db_location)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS TotalCount (id INTEGER PRIMARY KEY, count INTEGER NOT NULL DEFAULT 0, uses INTEGER NOT NULL DEFAULT 0);")
    c.execute(f"INSERT OR REPLACE INTO TotalCount (id, count, uses) VALUES(1, {word_count}, {use_count});")

    conn.commit()
    conn.close()


def query_table(db_location: str):
    conn = sqlite3.connect(db_location)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS TotalCount (id INTEGER PRIMARY KEY, count INTEGER NOT NULL DEFAULT 0, uses INTEGER NOT NULL DEFAULT 0);")
    c.execute("SELECT * FROM TotalCount WHERE id = 1;")

    data = c.fetchone()

    if data is None:
        return 0,0

    word_count = data[1]
    use_count = data[2]

    conn.commit()
    conn.close()

    return word_count, use_count
