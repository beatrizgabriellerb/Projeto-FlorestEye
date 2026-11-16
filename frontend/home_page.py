import streamlit as st


def home_page(nome: str):
    st.title(f"🌿 Bem-vindo(a), {nome}!")
    st.subheader("Sistema Inteligente de Cadastro de Denúncias Ambientais")

    st.markdown("---")

    st.markdown(
        """
        ### Sobre o nosso ecossistema de proteção ambiental
        
        Você acaba de acessar a central oficial de registro e acompanhamento de ocorrências 
        contra o meio ambiente. Este espaço foi desenvolvido para aproximar o cidadão 
        dos órgãos de fiscalização, garantindo que a sua voz seja ouvida e que ações 
        efetivas sejam tomadas de forma rápida e transparente.
        
        A degradação ambiental afeta a todos nós — seja através do desmatamento ilegal, 
        poluição de rios, descarte inadequado de resíduos ou maus-tratos à fauna. Aqui, 
        cada denúncia registrada é um passo vital em direção à preservação dos nossos 
        recursos naturais para as futuras gerações.
    """
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🔒 100% Seguro")
        st.write(
            "Privacidade garantida. Seus dados pessoais e de acesso são mantidos em absoluto sigilo."
        )

    with col2:
        st.markdown("### 🛡️ Criptografia Avançada")
        st.write(
            "Todas as informações e evidências enviadas passam por criptografia."
        )

    with col3:
        st.markdown("### ⚡ Acompanhamento")
        st.write(
            "Monitore o status de cada denúncia enviada diretamente pelo seu painel de usuário."
        )

    st.markdown("---")

    st.info(
        "💡 **Dica:** Utilize o menu lateral para cadastrar uma nova ocorrência ou acompanhar "
        "o andamento das denúncias que você já realizou. Juntos, podemos fazer a diferença!"
    )