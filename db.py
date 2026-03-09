import sqlite3

def get_db():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT,
        penulis TEXT,
        tahun INTEGER,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
