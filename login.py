import streamlit as st

# Usuário e senha fixos (simples e seguro para uso pessoal)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

def login():
    st.title(" Login")

    # Campos de entrada
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    # Botão de login
    if st.button("Entrar"):
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            st.success(" Login realizado com sucesso!")
            st.session_state["autenticado"] = True
            st.experimental_rerun()
        else:
            st.error(" Usuário ou senha incorretos")

# Função principal do app (conteúdo após login)
def app_principal():
    st.title(" Dashboard da Sinistralidade")
    st.write("Bem-vindo ao sistema!")
    if st.button("Sair"):
        st.session_state["autenticado"] = False
        st.experimental_rerun()

# Roteamento com sessão
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if st.session_state["autenticado"]:
    app_principal()
else:
    login()
