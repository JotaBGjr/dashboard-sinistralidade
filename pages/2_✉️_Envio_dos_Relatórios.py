import streamlit as st
st.set_page_config(page_title="Painel Geral", layout="wide")
import pandas as pd
import os
from datetime import datetime
from functions.verifica_pastas import gerar_relatorio_pastas, caminhos_3
from dateutil.relativedelta import relativedelta
import base64

from login import tela_login



st.title("✉️ Gestão de Envios")

LOCAL_ENV = os.path.exists("C:/JORGE_V1")

prazos_etapas = {
    "Amil":{"prazo": "Dia 15"},

    "Bradesco":{"prazo": "Dia 15"},
    "Seguros Unimed":{"prazo": "Dia 16"},
    "Bradesco (Manual)":{"prazo": "Dia 10"},
    "SulAmérica":{"prazo": "Dia 27"},
    "Unimed Nacional":{"prazo": "Dia 20"},
    "Porto Seguro":{"prazo": "Dia 27"},
    "Omint":{"prazo": "Dia 27"},
    "Omint (manual)":{"prazo": "Dia 20"},
    "Hapvida":{"prazo": "Dia 28"},
    "Plena Saúde":{"prazo": "Dia 28"},
 
}

operadoras_competencia = {
    "Reavaliação": 0,
    "Amil": -2,
    "Bradesco": -1,
    "Seguros Unimed": -1,
    "SulAmérica": -1,
    "Unimed Nacional": -1,
    "Porto Seguro": -1,
    "Omint": -1,
    "Hapvida": -2,
    "Plena Saúde": -2,
}

def identificar_competencia(etapa_nome):
    etapa_nome_lower = etapa_nome.lower()
    for operadora, ajuste_meses in operadoras_competencia.items():
        if operadora.lower() in etapa_nome_lower:
            competencia = datetime.today() + relativedelta(months=ajuste_meses)
            return competencia.strftime("%m/%Y")
    return "N/A"  # caso não encontre operadora






def carregar_df():
    return gerar_relatorio_pastas(caminhos_3) if LOCAL_ENV else pd.read_csv("dash-dados/csv/envio_relatorios.csv")

def preparar_df(df):
    df["Total de Pastas"] = pd.to_numeric(df["Total de Pastas"], errors="coerce")
    df["Pastas com Arquivo"] = pd.to_numeric(df["Pastas com Arquivo"], errors="coerce")
    df["Diferença"] = pd.to_numeric(df["Diferença"], errors="coerce")
    return df
cache_atualizacao = {}
def ultima_data_arquivo(pasta):
    if not LOCAL_ENV or not os.path.exists(pasta):
        return "Indisponível"
    try:
        datas = [os.path.getmtime(os.path.join(pasta, f)) for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]
        return datetime.fromtimestamp(max(datas)).strftime('%d/%m/%y') if datas else "Sem arquivos"
    except Exception:
        return "Erro"
def esta_perto_do_prazo(prazo_str, dias_antecedencia=3):
    try:
        dia_prazo = int(prazo_str.split(" ")[1])
        hoje = datetime.today().day
        return 0 <= (dia_prazo - hoje) <= dias_antecedencia
    except:
        return False
def img_base64(caminho):
    with open(caminho, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/jpeg;base64,{encoded}"

def img_operadora(etapa_nome):
    imagens = {
        "Bradesco": "pages/imagens/imagem_bradesco.jpg",
        "Omint": "pages/imagens/imagem_omint.jpg",
        "Hapvida": "pages/imagens/imagem_hapvida.jpg",
        "Plena": "pages/imagens/imagem_plenasaude.jpg",
        "Amil": "pages/imagens/imagem_amil.jpg",
        "Porto":"pages/imagens/imagem_portoseguro.jpg",
        "SulAmérica": "pages/imagens/imagem_sulamerica.jpg",
        "Seguros Unimed": "pages/imagens/imagem_segurosunimed.jpg",
        "Nacional": "pages/imagens/imagem_unimednacional.jpg"
        # Adicione outras operadoras aqui
    }
    for op in imagens:
        if op.lower() in etapa_nome.lower():
            caminho = imagens[op]
            if os.path.exists(caminho):
                return img_base64(caminho)
    return None  # Retorna None se não encontrar

def cor_operadora(etapa_nome):
    cores = {
        "Amil": "#fffff",
        "Bradesco": "#fffff",
        "Omint": "#fffff",
        "SulAmérica": "#fffff",
        "Hapvida": "#fffff",
        "Plena Saúde": "#ffffff",
        "Porto Seguro": "#fffff",
        "Seguros Unimed": "#fffff",
        "Unimed Nacional": "#fffff"
    }    
    for op in cores:
        if op.lower() in etapa_nome.lower():
            return cores[op]
    return "#f0f0f0"  # cor padrão caso nenhuma operadora seja encontrada   



def gerar_bloco_html(etapa, progresso, competencia_formatada, prazo, ultima_atualizacao, cor_barra, status):
    cor_status = {
    "Atrasado": "#f44336",       # vermelho
    "Em andamento": "#ff9800",   # amarelo
    "Concluído": "#4caf50"       # verde
}.get(status, "#9e9e9e")
    background_color = cor_operadora(etapa)
    imagem_base64 = img_operadora(etapa)
    imagem_html = f"<img src='{imagem_base64}' style='height: 30px; float: right;'/>" if imagem_base64 else ""
    return f"""
        <div style=' background: {background_color}; border: 1px solid #ccc; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='margin: 0 0 12px;'>{etapa} {imagem_html}</h4>
            <div style='margin-bottom: 8px;'>Competência: <b>{competencia_formatada}</b> | Prazo: <b>{prazo}</b> | Últ. Atualização: <b>{ultima_atualizacao}</b></div>
            <div style='margin-bottom: 8px;'>Status: <span style='color: {cor_status}; font-weight: bold;'>{status}</span></div>
            <div style='background-color: {background_color}; border-radius: 8px; overflow: hidden; height: 22px;'>
                <div style='width: {progresso}%; background-color: {cor_barra}; height: 100%; text-align: center;
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

# Exibir progresso por etapa
st.markdown("### Progresso por Atividade")
etapas_unicos = df["Etapa"].unique()

blocos_html_lista = []
status=""
for etapa in etapas_unicos:

    prazo = prazos_etapas.get(etapa, {}).get("prazo", "N/A")
    

    if proximo_do_prazo:
        background_color = "#fff9c4"  # amarelo claro
        borda_cor = "#f57c00"         # laranja escuro chamativo
    else:
        background_color = cor_operadora(etapa)
        borda_cor = "#ccc"            # borda padrão
    
    df_etapa = df[df["Etapa"] == etapa]
    total = df_etapa["Total de Pastas"].sum()
    com_arquivo = df_etapa["Pastas com Arquivo"].sum()
    progresso = int((com_arquivo / total) * 100) if total else 0

    cor = "#4CAF50" if progresso == 100 else "#2196F3" if progresso >= 50 else "#FF9800"

    prazo = prazos_etapas.get(etapa, {}).get("prazo", "N/A")
    competencia = identificar_competencia(etapa)
    competencia_formatada = competencia.replace("/", "-") if competencia != "N/A" else competencia

    
    if progresso == 100:
        status = "Concluído"
    elif prazo != "N/A":
        try:
            dia_prazo  = int(prazo.split(" ")[1])
            hoje = datetime.today().day
            status = "Atrasado" if hoje > dia_prazo else "Em andamento"
        except Exception as e:
                status = "Pendente"
    else:
        status = "Pendente"
    proximo_do_prazo = esta_perto_do_prazo(prazo) and status != "Concluído"
    
    if LOCAL_ENV:
        caminhos_3_pasta = [caminhos_3.get(etapa, "") for et in df_etapa["Etapa"]]
        cache_atualizacao = {}
        for pasta in set(caminhos_3_pasta):
            if pasta and pasta in cache_atualizacao:
                cache_atualizacao[pasta] = ultima_data_arquivo(pasta)
        valores = [cache_atualizacao.get(p, "Indisponível") for p in caminhos_3_pasta if p]
        valores_validos = [v for v in valores if v not in ["Indisponível", "Erro", "Sem arquivos"]]
        ultima_atualizacao = valores_validos[0] if valores_validos else "Indisponível"
    else:
        valores = df_etapa["Últ. Atualização"].dropna().tolist()
        ultima_atualizacao = valores[0] if valores else "Indisponível"

    #atraso_html = "<span style='color: red; font-weight: bold;'> ⚠️ Atrasado </span>" if atrasado else ""
    
    bloco_html = gerar_bloco_html(etapa , progresso, competencia_formatada, prazo, ultima_atualizacao, cor, status)
    blocos_html_lista.append(bloco_html)



# Exibir todos os blocos de uma vez
st.components.v1.html(
    "<div style='max-height: 720px; overflow-y: auto; padding-right: 10px;'>" +
    "".join(blocos_html_lista) +
    "</div>",
    height=740
)

st.markdown("###  Resumo")

# Verifique as colunas disponíveis (apagar depois de verificar)
#st.write("Colunas disponíveis:", df.columns.tolist())

# Use nomes corretos
colunas_resumo = ["Etapa", "Pastas Vazias","Pastas c/ Arquivos"]

# Garantir que só usaremos colunas que existem
colunas_existentes = [col for col in colunas_resumo if col in df.columns]

df_resumo = df[colunas_existentes].groupby("Etapa", as_index=False).sum()

st.dataframe(df_resumo, use_container_width=True)
