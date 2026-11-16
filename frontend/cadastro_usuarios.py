import streamlit as st
from domain.entities.user_entities import User
from validators.email_exists import email_exists
import pandas as pd
import time

def cadastro_usuarios():
    st.title("➕ Cadastro de Novo Usuário")

    with st.form("form_login"):
        nome = st.text_input("NOME")
        email = st.text_input("EMAIL").lower()
        senha = st.text_input("SENHA", type="password")
        confirma_senha = st.text_input("CONFIRMAR SENHA", type="password")
        botao_criar = st.form_submit_button("Criar Usuário")

        campos = {
                "Nome": nome,
                "E-mail": email,
                "Senha": senha,
                "Confirmar Senha": confirma_senha,
            }   

        if botao_criar:
            if not all(campos.values()):
                st.error("Por favor, preencha todos os campos!")
                return
            elif not senha == confirma_senha:
                st.error("As senhas não são iguais")
                return
            try:
                user = User.create_user(nome, email, senha)
                
                if email_exists(user.email):
                    st.error("Esse email ja existe na nossa base de dados")
                    return

                df = pd.read_csv("db/usuarios.csv", sep=";")
                ultima_linha = df.iloc[-1]

                user_novo = pd.DataFrame([{
                    "ID": ultima_linha["ID"] + 1,
                    "NOME": user.nome,
                    "EMAIL": user.email,
                    "SENHA": user.senha,
                    "IS_ADMIN": user.is_admin,
                }])

                df = pd.concat([df, user_novo], ignore_index=True)
                df.to_csv("db/usuarios.csv", sep=";", index=False)

                st.success(f"Usuário {user.nome} cadastrado com sucesso! 🎉")
                time.sleep(3)
                st.session_state.pagina = "login"
                st.rerun()
                return
            except Exception as e:
                st.error(f"Erro: {e}")
                return
           
    st.write("Já tem uma conta?")
    if st.button("Faça o Login aqui"):
        st.session_state.pagina = "login"
        st.rerun()
        