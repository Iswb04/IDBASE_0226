import sqlite3

def deletar_por_token(token):
    conn = sqlite3.connect("tokens.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE token = ?", (token,))
    conn.commit()

    if cursor.rowcount > 0:
        print("success.")
    else:
        print("token not found.")

    conn.close()


token = input("enter the token you want to delete: ")
deletar_por_token(token)