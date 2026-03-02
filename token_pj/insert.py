import sqlite3

def inserir_usuario(nome, sobrenome, token):
    conn = sqlite3.connect("tokens.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, sobrenome, token) VALUES (?, ?, ?)",
            (nome, sobrenome, token)
        )
        conn.commit()
        print("success.")
    except sqlite3.IntegrityError:
        print("this token already exists.")

    conn.close()


nome = input("first name: ").capitalize()
sobrenome = input("last name: ").capitalize()

while True:
    token = input("enter the token -(exactly 9 numbers): ")

    if token.isdigit() and len(token)==9:
        break
    else: 
        print("invalid")

inserir_usuario(nome, sobrenome, token)