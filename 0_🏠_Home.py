# home.py

import streamlit as st
from login import tela_login

st.set_page_config(page_title="Login", layout="centered")

authenticator = tela_login()

nome, autenticado, usuario = authenticator.login("Login", "main")

if autenticado:
    st.success(f"Bem-vindo, {nome}!")
    st.switch_page("pages/outras_páginas.py")

elif autenticado is False:
    st.error("Usuário ou senha incorretos.")

elif autenticado is None:
    st.warning("Por favor, insira suas credenciais.")
