import os

if os.path.exists("tokens.db"):
    os.remove("tokens.db")
    print("Banco apagado com sucesso.")
else:
    print("Banco não encontrado.")