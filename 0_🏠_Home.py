# home.py

import streamlit as st
from login import tela_login

st.set_page_config(page_title="Login", layout="centered")

nome, autenticado, usuario = tela_login()

if autenticado:
    st.success(f"Bem-vindo, {nome}!")
    st.switch_page("pages/0_🏠_Gerencial.py")

elif autenticado is False:
    st.error("Usuário ou senha incorretos.")

elif autenticado is None:
    st.warning("Por favor, insira suas credenciais.")
