import streamlit as st
from auth import authenticator

st.set_page_config(page_title = "Login", layout="centered")

name, auth_status, username = authenticator.login("Login", "main")

if auth_status:
    st.session_state["login_realizado"] = True
    st.session_state["usuario"] = username
    st.success(f"Bem-vindo, {name}!")
    st.switch_page("home.py") # redireciona para home

elif auth_status == False:
    st.error("Usuário ou senha incorretos.")
else:
    st.warning("Por favor, faça login.")

