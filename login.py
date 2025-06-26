import streamlit as st

# Dicionário de usuários válidos
usuarios = {"jorge": "1234", "admin": "admin"}

def tela_login():
    st.title("🔐 Tela de Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario] == senha:
            st.session_state.login_realizado = True
            st.session_state.usuario = usuario
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha incorretos.")
