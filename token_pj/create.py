import sqlite3

conn = sqlite3.connect("tokens.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    token TEXT NOT NULL UNIQUE
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso.")