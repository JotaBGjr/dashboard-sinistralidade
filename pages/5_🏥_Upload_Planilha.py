import streamlit as st
import sys
import os

if "autenticado" not in st.session_state or not st.session_state["autenticado"]:
    st.warning("⚠️ Você precisa estar logado para acessar esta página.")
    st.stop()  # Interrompe a execução

# Adiciona dash-dados ao sys.path
DASH_DADOS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dash-dados"))
if DASH_DADOS_PATH not in sys.path:
    sys.path.insert(0, DASH_DADOS_PATH)

from functions_medicas.data_loader import processar_planilha
from functions_medicas.db_handler import inserir_dados

st.set_page_config(page_title="📤 Upload de Planilha", layout="wide")
st.title("📤 Upload de Planilha Médica")

uploaded_file = st.file_uploader("Selecione o arquivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    #Salva o arquivo em uma pasta temporária
    uploads_dir = "dash-dados/uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    caminho_salvo = os.path.join(uploads_dir, uploaded_file.name)

    with open(caminho_salvo, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f" Arquivo '{uploaded_file.name}'salvo com sucesso!")
    if st.button (" Processar e Inserir no Banco de Dados"):
        try:
            pacientes, valores = processar_planilha(caminho_salvo)
            inserir_dados(pacientes, valores)
            st.success(f"{len(pacientes)} pacientes e {len(valores)} valores inseridos com sucesso!")
        except  Exception as e:
            st.error(f"Erro ao processar:{e}")
