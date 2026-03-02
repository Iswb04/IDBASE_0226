import sqlite3

def inserir_usuario(nome, token):
    conn = sqlite3.connect("tokens.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, token) VALUES (?, ?)",
            (nome, token)
        )
        conn.commit()
        print("Usuário inserido com sucesso.")
    except sqlite3.IntegrityError:
        print("Esse token já existe.")

    conn.close()


nome = input("Digite o nome: ")
token = input("Digite o token: ")

inserir_usuario(nome, token)