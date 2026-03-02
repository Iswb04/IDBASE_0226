import sqlite3

def deletar_por_token(token):
    conn = sqlite3.connect("tokens.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE token = ?", (token,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Usuário deletado com sucesso.")
    else:
        print("Token não encontrado.")

    conn.close()


token = input("Digite o token do usuário que deseja apagar: ")
deletar_por_token(token)