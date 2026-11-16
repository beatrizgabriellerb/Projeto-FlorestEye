import pandas as pd

def get_user(email):
    df = pd.read_csv("db/usuarios.csv", sep=";")
    usuario = df[df["EMAIL"] == email]

    return usuario.iloc[0] if not usuario.empty else None