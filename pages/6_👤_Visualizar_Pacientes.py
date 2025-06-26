import streamlit as st
from auth import authenticator
import sqlite3
import pandas as pd
import plotly.express as px


if "login_realizado" not in st.session_state or not st.session_state["login_realizado"]:
    st.warning("Você precisa estar logado para acessar esta página.")
    st.swith_page("login.py")



if st.button("Sair"):
    authenticator.logout("Logout", "main")
    st.session_state.clear()
    st.switch_page("login.py")
    

DB_PATH = "dash-dados/db/pacientes.db"

st.set_page_config(page_title="👤 Pacientes", layout="wide")
st.title("👤 Consulta de Pacientes")

# Conectar ao banco
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row  # para acessar por nome
cursor = conn.cursor()

# Campo de busca
busca = st.text_input("🔎 Buscar por nome do paciente:")

# Consulta os pacientes
query = "SELECT * FROM pacientes"
params = ()
if busca:
    query += " WHERE nome LIKE ?"
    params = (f"%{busca}%",)

df_pacientes = pd.read_sql_query(query, conn, params=params)

# Mostra lista de pacientes encontrados
if df_pacientes.empty:
    st.warning("Nenhum paciente encontrado.")
else:
    for _, row in df_pacientes.iterrows():
        with st.expander(f"{row['nome']} ({row['operadora']})"):
            col1, col2 = st.columns(2)
            col1.markdown(f"**Titularidade:** {row['titularidade']}")
            col1.markdown(f"**Criticidade:** {row['criticidade']}")
            col1.markdown(f"**Plano:** {row['plano']}")
            col1.markdown(f"**Status:** {row['status']}")
            col1.markdown(f"**Especialidade:** {row['especialidade']}")
            col1.markdown(f"**Sexo / Idade:** {row['sexo']} / {row['idade']}")

            col2.markdown(f"**CID:** {row['cid']}")
            col2.markdown(f"**Prestador:** {row['prestador']}")
            col2.markdown(f"**Diagnóstico:** {row['hipotese_diagnostica']}")
            col2.markdown(f"**Período da análise:** {row['periodo_inicio']} até {row['periodo_fim']}")

            # Busca os valores mensais
            valores = pd.read_sql_query(
                "SELECT data_referencia, valor FROM valores_mensais WHERE paciente_id = ? ORDER BY data_referencia",
                conn,
                params=(row['id'],)
            )

            if not valores.empty:
                fig = px.line(valores, x="data_referencia", y="valor", markers=True,
                              title="Histórico de valores mensais")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Sem valores mensais cadastrados.")
