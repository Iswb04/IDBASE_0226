import sqlite3

conn = sqlite3.connect("tokens.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    token number NOT NULL UNIQUE
)
""")

conn.commit()
conn.close()

print("success.")