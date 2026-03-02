import os

if os.path.exists("tokens.db"):
    os.remove("tokens.db")
    print("success.")
else:
    print("database not found.")