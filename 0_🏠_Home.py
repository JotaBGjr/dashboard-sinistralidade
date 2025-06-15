import streamlit as st
import pandas as pd
import os
from datetime import datetime
from functions.verifica_pastas import gerar_relatorio_pastas, caminhos

st.set_page_config(page_title="Painel Geral", layout="wide")
st.title("📊 Painel Geral dos Relatórios de Sinistralidade")

LOCAL_ENV = os.path.exists("C:/JORGE_V1")

# Metadados com prazos e competência por plano
metadados_etapas = {
    "Bradesco": {"prazo": 10, "competencia": "05/2025"},
    "Bradesco - Arquivo de Cadastro/Faturamento": {"prazo": 15, "competencia": "05/2025"},
    "GEAP": {"prazo": 5, "competencia": "05/2025"},
    "Fundação Saúde": {"prazo": 10, "competencia": "05/2025"},
    "Fundação Saúde (Cadastro)": {"prazo": 15, "competencia": "05/2025"},
    "Petros": {"prazo": 12, "competencia": "05/2025"},
    "Petros (Cadastro)": {"prazo": 15, "competencia": "05/2025"},
    "Postal Saúde": {"prazo": 5, "competencia": "05/2025"},
    "Postal Saúde (Cadastro)": {"prazo": 10, "competencia": "05/2025"},
    "Zetta / Operadoras": {"prazo": 10, "competencia": "05/2025"},
}

def carregar_df():
    return gerar_relatorio_pastas(caminhos) if LOCAL_ENV else pd.read_csv("dashboard/csv/home.csv")

def preparar_df(df):
    df["Total de Pastas"] = pd.to_numeric(df["Total de Pastas"], errors="coerce")
    df["Pastas com Arquivo"] = pd.to_numeric(df["Pastas com Arquivo"], errors="coerce")
    df["Diferença"] = pd.to_numeric(df["Diferença"], errors="coerce")
    return df

def ultima_data_arquivo(pasta):
    if not LOCAL_ENV or not os.path.exists(pasta):
        return "Indisponível"
    try:
        arquivos = [os.path.join(pasta, f) for f in os.listdir(pasta)]
        datas = [os.path.getmtime(f) for f in arquivos if os.path.isfile(f)]
        if datas:
            ultima_data = max(datas)
            return datetime.fromtimestamp(ultima_data).strftime('%d/%m/%Y')
        return "Sem arquivos"
    except Exception:
        return "Erro"

def gerar_bloco_html(plano, progresso, competencia_formatada, prazo, ultima_atualizacao, cor):
    return f"""
        <div style='border: 1px solid #ccc; border-radius: 12px; padding: 16px; margin-bottom: 12px;
                    background-color: #f9f9f9; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='margin: 0 0 12px;'>{plano}</h4>
            <div style='margin-bottom: 8px;'>Competência: <b>{competencia_formatada}</b> | Prazo: <b>{prazo}</b> | Últ. Atualização: <b>{ultima_atualizacao}</b></div>
            <div style='background-color: #eee; border-radius: 8px; overflow: hidden; height: 22px;'>
                <div style='width: {progresso}%; background-color: {cor}; height: 100%; text-align: center;
                            color: white; font-weight: bold;'>{progresso}%</div>
            </div>
        </div>
    """

# Carregar dados
df = carregar_df()
df = preparar_df(df)

# Atualização manual
if st.button("Atualizar Status"):
    df = carregar_df()
    df = preparar_df(df)
    st.success("Dados atualizados!")

# Dividir colunas para visualização
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Etapas", value=df["Etapa"].nunique())

with col2:
    etapas_concluidas = df[df["Diferença"] == 0]["Etapa"].nunique()
    st.metric("Etapas Concluídas", value=etapas_concluidas)

with col3:
    progresso_total = int((etapas_concluidas / df["Etapa"].nunique()) * 100)
    st.metric("Progresso Geral", value=f"{progresso_total}%")
    st.progress(progresso_total / 100)

# Exibir progresso por plano
st.markdown("### Progresso por Atividade")
planos_unicos = df["Plano"].unique()

blocos_html_lista = []

for plano in planos_unicos:
    df_plano = df[df["Plano"] == plano]
    total = df_plano["Total de Pastas"].sum()
    com_arquivo = df_plano["Pastas com Arquivo"].sum()
    progresso = int((com_arquivo / total) * 100) if total else 0

    cor = "#4CAF50" if progresso == 100 else "#2196F3" if progresso >= 50 else "#FF9800"

    prazo = metadados_etapas.get(plano, {}).get("prazo", "N/A")
    competencia = metadados_etapas.get(plano, {}).get("competencia", "N/A")
    competencia_formatada = competencia.replace("/", "-")

    caminhos_pasta = [caminhos.get(etapa, "") for etapa in df_plano["Etapa"]]
    ultima_atualizacao = max([ultima_data_arquivo(pasta) for pasta in caminhos_pasta if pasta], default="N/A")

    bloco_html = gerar_bloco_html(plano, progresso, competencia_formatada, prazo, ultima_atualizacao, cor)
    blocos_html_lista.append(bloco_html)

# Exibir todos os blocos de uma vez
st.components.v1.html(
    "<div style='max-height: 720px; overflow-y: auto; padding-right: 10px;'>" +
    "".join(blocos_html_lista) +
    "</div>",
    height=740
)
