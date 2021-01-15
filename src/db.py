import sqlite3
def get_db(): return sqlite3.connect('fraud.db')
def init_db():
    with get_db() as conn:
        with open('schema.sql') as f: conn.executescript(f.read())