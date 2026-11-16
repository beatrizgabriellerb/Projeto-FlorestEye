import pandas as pd
import streamlit as st
from utils.criptografia_propria import descriptografar


def minhas_denuncias(id_user):
    df = pd.read_csv("db/denuncias.csv", sep=",", index_col=False)
    df_user = df[df["USUARIO_ID"] == id_user]

    if df_user.empty:
        st.info("Você ainda não registrou nenhuma denúncia.")
        return
      
    if "DESCRICAO" in df.columns and df["DESCRICAO"].notna().any():
        df_user["DESCRICAO"] = df_user["DESCRICAO"].fillna("").astype(str).apply(descriptografar).str.lower()
    
    df_user["IMAGEM_PATH"] = "app/static/" + df_user["IMAGEM_PATH"].fillna("").astype(str).apply(descriptografar).str.lower()

    st.title("Minhas Denúncias:")

    colunas_desejadas = ["DATA_OCORRENCIA", "DESCRICAO", "IMAGEM_PATH", "STATUS"]

    st.dataframe(
        df_user[colunas_desejadas],
        hide_index=True,
        use_container_width=True,
        column_config={
            "DATA_OCORRENCIA": "Data",
            "DESCRICAO": "Descrição",
            "IMAGEM_PATH": st.column_config.ImageColumn("Foto"),
            "STATUS": "Status",
        },
    )