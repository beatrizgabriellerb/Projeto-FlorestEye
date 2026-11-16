from datetime import date
from domain.entities.denuncias_entities import Denuncia
import streamlit as st
import pandas as pd
from utils.salvar_img import save_img

def cadastrar_denuncia(id_user, nome: str):

    st.subheader(f"📝 Olá, {nome}! Faça seu cadastro")

    col1, col2 = st.columns([2, 1])

    with col1:
        local = st.text_input("Local*")
    with col2:
        data_ocorrencia = st.date_input("Data*", value=date.today(), max_value=date.today())

    descricao = st.text_area("Descrição")
    imagem = st.file_uploader("Imagem*", type=["png", "jpg", "jpeg"])

  
    
    if st.button("Enviar", use_container_width=True):
        if not local:
            st.error("Preencha o local")
            return
        if not data_ocorrencia:
            st.error("Preencha a data da ocorrência")
            return
        if not imagem:
            st.error("Adicione uma imagem")
            return
        
        try:
            denuncia = Denuncia.create_denuncia(local, data_ocorrencia, descricao, imagem.name)
            df = pd.read_csv("db/denuncias.csv", sep=",")
            ultima_linha = df.iloc[-1]

            if df.empty:
                novo_id = 1
            else:
                ultima_linha = df.iloc[-1]
                novo_id = int(ultima_linha["ID"]) + 1

            denuincia_nova = pd.DataFrame({
                "ID": [novo_id],
                "USUARIO_ID": [id_user],
                "DATA_OCORRENCIA": [denuncia.data_ocorrencia],
                "DESCRICAO": [denuncia.descricao],
                "IMAGEM_PATH": [denuncia.imagem_path],
                "STATUS": [denuncia.status]
            })

            df = pd.concat([df, denuincia_nova], ignore_index=True)
            df.to_csv("db/denuncias.csv", sep=",", index=False)
            save_img(imagem)
            st.success(f"Denuncia cadastrada com sucesso! 🎉")
            

        except Exception as e:
            st.error(f"Erro: {e}")
    
# MUDAR CRIPT DA IMAGEM
