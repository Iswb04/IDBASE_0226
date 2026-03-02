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


verify = input("enter the token: ")
usuario = verificar_token(verify)

if usuario:
    print(f"access granted. welcome, {usuario[0]}.")
else:
    print("access denied.")