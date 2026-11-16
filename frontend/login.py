import streamlit as st
from validators.email_exists import email_exists
from utils.get_user import get_user
import bcrypt
import time
from frontend.cadastro_usuarios import cadastro_usuarios

def login():
    st.title("Login de Usuários")

    with st.form("form_cadastro"):
        email = st.text_input("EMAIL")
        senha = st.text_input("SENHA", type="password")
        botao_criar = st.form_submit_button("Fazer Login")

        campos = {
                "E-mail": email,
                "Senha": senha,
            }   

        if botao_criar:
            if not all(campos.values()):
                st.error("Por favor, preencha todos os campos!")
                return
            elif len(senha) < 6:
                st.error("Senha inválida deve ter no mínimo 6 caracteres")     
                return       
            elif not email_exists(email):
                st.error("Credenciais inválidas")
                return

            user = get_user(email)
            user_password_hash = user["SENHA"]
            
            if not bcrypt.checkpw(senha.encode(), user_password_hash.encode()):
                st.error("Credenciais inválidas")
                return

            st.session_state["logado"] = True
            st.session_state["id"] = user["ID"]
            st.session_state["nome"] = user["NOME"]
            st.session_state["admin"] = user["IS_ADMIN"]
            
            time.sleep(3)
            st.success("Logado com sucesso!")

            st.rerun()

            
    
    
    st.write("Não tem uma conta?")
    if st.button("Cadastre-se aqui"):
        st.session_state.pagina = "cadastro"
        st.rerun()
            


# decriptografar: bcrypt.checkpw(senha.encode(), hash_armazenado.encode())