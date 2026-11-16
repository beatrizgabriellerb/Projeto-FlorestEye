import pandas as pd
import streamlit as st
from utils.criptografia_propria import descriptografar

def denuncia_usuarios():
    df = pd.read_csv("db/denuncias.csv", sep=",", index_col=False)
    
    if "DESCRICAO" in df.columns and df["DESCRICAO"].notna().any():
        df["DESCRICAO"] = df["DESCRICAO"].fillna("").astype(str).apply(descriptografar).str.lower()
    
    df["IMAGEM_PATH"] = "app/static/" + df["IMAGEM_PATH"].fillna("").astype(str).apply(descriptografar).str.lower()

    st.title("Denúncias de Usuários:")

    colunas_desejadas = ["DATA_OCORRENCIA", "DESCRICAO", "IMAGEM_PATH", "STATUS"]

    # Campos de filtragem mínimos na barra lateral
    status = st.sidebar.multiselect("Status", df["STATUS"].unique())
    data = st.sidebar.date_input("Data", value=None)

    df_filtrado = df.copy()

    if status:
        df_filtrado = df_filtrado[df_filtrado["STATUS"].isin(status)]
    
    if data:
        datas = pd.to_datetime(df_filtrado["DATA_OCORRENCIA"], errors="coerce").dt.date
        df_filtrado = df_filtrado[datas == data]

    if df_filtrado.empty:
        st.info("Nenhuma denúncia encontrada com esses filtros.")
        return

    editado = st.data_editor(
        df_filtrado,
        column_order=colunas_desejadas,
        hide_index=True,
        use_container_width=True,
        disabled=["DATA_OCORRENCIA", "DESCRICAO", "IMAGEM_PATH"],
        column_config={
            "DATA_OCORRENCIA": "Data",
            "DESCRICAO": "Descrição",
            "IMAGEM_PATH": st.column_config.ImageColumn("Foto"),
            "STATUS": st.column_config.SelectboxColumn(
                "Status", options=["PENDENTE", "EM ANÁLISE", "CONFIRMADO", "CANCELADO"]
            ),
        },
    )

    mudou_df = editado[editado["STATUS"] != df_filtrado["STATUS"]]
    
    if not mudou_df.empty:
        bruto = pd.read_csv("db/denuncias.csv", sep=",", index_col=False)
        for _, linha in mudou_df.iterrows():
            bruto.loc[bruto["ID"] == linha["ID"], "STATUS"] = linha["STATUS"]
        bruto.to_csv("db/denuncias.csv", index=False)
        st.rerun()
