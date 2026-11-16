import streamlit as st
from frontend.cadastro_usuarios import cadastro_usuarios
from frontend.login import login
from frontend.home_page import home_page
from frontend.cadastro_denuncia import cadastrar_denuncia
from frontend.minhas_denuncias import minhas_denuncias
from frontend.denuncias_usuarios import denuncia_usuarios

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "login"


if "id" in st.session_state:
    st.session_state['pagina'] = ''
    user_id = st.session_state["id"]
    user_name = st.session_state["nome"]
    is_admin = st.session_state["admin"]
    
    st.sidebar.title("Menu de Navegação")

    if is_admin:
        pagina = st.sidebar.radio("Escolha a página:", ["Home", "Denuncia de Usuários"])
    else:
        pagina = st.sidebar.radio("Escolha a página:", ["Home", "Cadastrar Denuncia", "Minhas Denúncias"])

    match pagina:
        case 'Home':
            home_page(user_name)
        case 'Denuncia de Usuários':
            denuncia_usuarios()
        case 'Cadastrar Denuncia':
            cadastrar_denuncia(user_id, user_name)
        case 'Minhas Denúncias':
            minhas_denuncias(user_id)
    
    
else:
    if st.session_state.pagina == "login":
        login()
    elif st.session_state.pagina == "cadastro":
        cadastro_usuarios()
    