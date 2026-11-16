import pandas as pd

def email_exists(email):
    df = pd.read_csv("db/usuarios.csv", sep=";")

    email_existe = (df["EMAIL"] == email).any()

    if email_existe:
        return True 
    
    return False
   