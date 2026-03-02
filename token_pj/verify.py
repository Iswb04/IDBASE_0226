import sqlite3

def verificar_token(token_recebido):
    conn = sqlite3.connect("tokens.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome FROM usuarios WHERE token = ?",
        (token_recebido,)
    )

    resultado = cursor.fetchone()
    conn.close()

    return resultado


usuario = input("Digite o token: ")

if usuario:
    print(f"Acesso liberado. Bem vindo(a), {usuario[0]}")
else:
    print("Acesso negado")