import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
from verifica_pastas import gerar_relatorio_pastas, caminhos
import os
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale


st.set_page_config(layout="wide", page_title="Dashboard de relatório")
LOCAL_ENV = os.path.exists("C:/JORGE_V1")  # você pode ajustar esse caminho conforme desejar


if LOCAL_ENV:
        df = gerar_relatorio_pastas(caminhos)
    else
        df = pd.read_csv("dashboard/csv/home.csv")
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    # fallback para o default do sistema
    locale.setlocale(locale.LC_TIME, '')




hoje = datetime.now()
time = hoje.strftime("%m/%Y")

st.title("Monitoramento de Progressão")
st.markdown("Este painel mostra o status de andamento do Relatório de Sinistralidade mês " + time)
st.markdown("Selecione um painel para visualizar:")






def ultima_data_arquivo(pasta):
    try:
        arquivos = [os.path.join(pasta, f) for f in os.listdir(pasta)]
        arquivos = [f for f in arquivos if os.path.isfile(f)]
        if not arquivos:
            return "Sem arquivos"
        ultima_data = max(os.path.getmtime(f) for f in arquivos)
        return datetime.fromtimestamp(ultima_data).strftime("%d/%m/%Y")
    except Exception as e:
        return "Erro"

# Função para estilizar o nome do plano
def estilizar_plano(plano):
    estilo = {
        "Planilha": "background-color:#00FF00;color:#DCDCDC;font-weight:bold;padding:4px;border-radius:5px",
        "Bradesco": "background-color:#8B0000;color:#D3D3D3;font-weight:bold;padding:4px;border-radius:5px",
        "Amil": "background-color:#1E90FF;color:#FFFFFF;font-weight:bold;padding:4px;border-radius:5px",
        "Hapvida": "background-color:#FFA500;color:#0000CD;font-weight:bold;padding:4px;border-radius:5px",
        "Omint": "background-color:#00008B;color:#DCDCDC;font-weight:bold;padding:4px;border-radius:5px",
        "Plena Saúde": "background-color:#B0C4DE;color:#800080;font-weight:bold;padding:4px;border-radius:5px",
        "Porto Seguro": "background-color:#F5FFFA;color:#1E90FF;font-weight:bold;padding:4px;border-radius:5px",
        "SulAmérica -": "background-color:#FF4500;color:#000080;font-weight:bold;padding:4px;border-radius:5px",
        "Seguros Unimed": "background-color:#B0C4DE;color:#000080;font-weight:bold;padding:4px;border-radius:5px",
        "Unimed Nacional": "background-color:#228B22;color:#FFFFFF;font-weight:bold;padding:4px;border-radius:5px",
    }
    for chave in estilo:
        if chave.lower() in plano.lower():
            return f"<div style='{estilo[chave]}'>{plano}</div>"
    return f"<div style='font-weight:bold'>{plano}</div>"

# Função para cor da barra
def cor_barra(progresso):
    if progresso >= 1:
        return "#00C851"  # verde
    elif progresso >= 0.9:
        return "#4285F4"  # azul
    elif progresso >= 0.5:
        return "#FFA500"  # laranja
    else:
        return "#FF4444"  # vermelho

if st.button("Atualizar Status"):
    if LOCAL_ENV:
        df = gerar_relatorio_pastas(caminhos)
    else:
        df = pd.read_csv("dashboard/csv/home.csv")

    blocos_html_lista = []
    
    st.success("Dados atualizados!")

    # Conversões seguras
    df["Total de Pastas"] = pd.to_numeric(df["Total de Pastas"], errors="coerce")
    df["Pastas com Arquivo"] = pd.to_numeric(df["Pastas com Arquivo"], errors="coerce")
    df["Diferença"] = pd.to_numeric(df["Diferença"], errors="coerce")

    # Métricas resumidas
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Arquivos", int(df["Total de Pastas"].sum(skipna=True)))
    col2.metric("Arquivos Recebidos", int(df["Pastas com Arquivo"].sum(skipna=True)))
    col3.metric("Arquivos Pendentes", int(df["Diferença"].sum(skipna=True)))

    # Progresso da extração
    st.subheader("Extração de Arquivos")

    total_pastas = len(df)
    pastas_com_arquivos = df[df["Pastas com Arquivo"] > 0].shape[0]

    progresso = pastas_com_arquivos / total_pastas if total_pastas > 0 else 0

    st.progress(progresso)
    st.metric("Progresso", f"{int(progresso * 100)}%")

    st.subheader("Progresso por Atividade")

    planos_unicos = df["Plano"].unique()

    metadados_etapas = {
    "Planilha de Reavaliação": {
    "prazo":"03",
    "ajuste_competencia": +1


    },

    "Amil - Bi Zetta": {
    "prazo":"10",
    "ajuste_competencia": -1

    },
    "Amil - Envio Relatórios": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Amil - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"16",
    "ajuste_competencia": -1

    },


    "Bradesco - Arquivo de Cadastro/Faturamento": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Bradesco - Base Aberta de Sinistro": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Bradesco - Relatório Gerencial de Sinistralidade": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Bradesco - Bi Zetta": {
    "prazo":"10",
    "ajuste_competencia": -1

    },
    "Bradesco - Envio Relatório de Sinistralidade": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Bradesco - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"16",
    "ajuste_competencia": -1

    },


    "Seguros Unimed - Arquivo de Cadastro/Faturamento": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Seguros Unimed - Base Aberta de Sinistro": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Seguros Unimed - Relatório Gerencial de Sinistralidade": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Seguros Unimed - Bi Zetta": {
    "prazo":"10",
    "ajuste_competencia": -1

    }, 
    "Seguros Unimed - Envio Relatório de Sinistralidade": {
    "prazo":"16",
    "ajuste_competencia": -1

    },
    "Seguros Unimed - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"17",
    "ajuste_competencia": -1

    },

    "Bradesco (manual) - Relatório Gerencial de Sinistralidade": {
    "prazo":"05",
    "ajuste_competencia": -1

    },
    "Bradesco (manual) - Produção do Relatório": {
    "prazo":"08",
    "ajuste_competencia": -1

    },
    "Bradesco (Manual) - Envio Relatório de Sinistralidade": {
    "prazo":"10",
    "ajuste_competencia": -1

    },
    "Bradesco (Manual) - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"11",
    "ajuste_competencia": -1

    },

    "SulAmérica - Arquivo de Cadastro/Faturamento": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "SulAmérica - Base Aberta de Sinistro": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "SulAmérica - Relatório Gerencial de Sinistralidade": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "SulAmérica - Bi Zetta": {
    "prazo":"18",
    "ajuste_competencia": -1

    },
    "SulAmérica - Envio Relatório de Sinistralidade": {
    "prazo":"27",
    "ajuste_competencia": -1

    },
    "SulAmérica - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"28",
    "ajuste_competencia": -1

    },

                
    "Unimed Nacional - Arquivo de Cadastro/Faturamento": {
    "prazo":"13",
    "ajuste_competencia": -1

    },
    "Unimed Nacional - Base Aberta de Sinistro": {
    "prazo":"13",
    "ajuste_competencia": -1

    },
    "Unimed Nacional - Relatório Gerencial de Sinistralidade": {
    "prazo":"13",
    "ajuste_competencia": -1

    },
    "Unimed Nacional - Bi Zetta": {
    "prazo":"18",
    "ajuste_competencia": -1

    },
    "Unimed Nacional - Envio Relatório de Sinistralidade": {
    "prazo":"25",
    "ajuste_competencia": -1

    },
    "Unimed Nacional - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"26",
    "ajuste_competencia": -1

    },

                
    "Porto Seguro - Arquivo de Cadastro/Faturamento": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Porto Seguro - Base Aberta de Sinistro": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Porto Seguro - Relatório Gerencial de Sinistralidade": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Porto Seguro - Bi Zetta": {
    "prazo":"20",
    "ajuste_competencia": -1

    },
    "Porto Seguro - Envio Relatório de Sinistralidade": {
    "prazo":"27",
    "ajuste_competencia": -1

    },
    "Porto Seguro - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"28",
    "ajuste_competencia": -1

    },
                
    "Omint - Arquivo de Cadastro/Faturamento": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Omint - Base Aberta de Sinistro": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Omint - Relatório Gerencial de Sinistralidade": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Omint - Bi Zetta": {
    "prazo":"20",
    "ajuste_competencia": -1

    },
    "Omint - Envio Relatório de Sinistralidade": {
    "prazo":"27",
    "ajuste_competencia": -1

    },
    "Omint - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"28",
    "ajuste_competencia": -1

    },

    "Omint (manual) - Relatório Gerencial de Sinistralidade": {
    "prazo":"15",
    "ajuste_competencia": -1

    },
    "Omint (manual) - Produção do Relatório": {
    "prazo":"18",
    "ajuste_competencia": -1

    },
    "Omint (manual) - Envio Relatório de Sinistralidade": {
    "prazo":"20",
    "ajuste_competencia": -1

    },
    "Omint (manual) - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"21",
    "ajuste_competencia": -1

    },
            
    "Hapvida - Arquivo de Cadastro/Faturamento": {
    "prazo":"20",
    "ajuste_competencia": -2

    },
    "Hapvida - Base Aberta de Sinistro": {
    "prazo":"20",
    "ajuste_competencia": -2

    },
    "Hapvida - Relatório Gerencial de Sinistralidade": {
    "prazo":"20",
    "ajuste_competencia": -2

    },
    "Hapvida - Bi Zetta": {
    "prazo":"25",
    "ajuste_competencia": -2

    },
    "Hapvida - Envio Relatório de Sinistralidade": {
    "prazo":"28",
    "ajuste_competencia": -2

    },
    "Hapvida - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"29",
    "ajuste_competencia": -2

    },
                

    "Plena Saúde - Arquivo de Cadastro/Faturamento": {
    "prazo":"20",
    "ajuste_competencia": -1

    },
    "Plena Saúde - Base Aberta de Sinistro": {
    "prazo":"20",
    "ajuste_competencia": -1

    },
    "Plena Saúde - Relatório Gerencial de Sinistralidade": {
    "prazo":"20",
    "ajuste_competencia": -1

    },
    "Plena Saúde - Bi Zetta": {
    "prazo":"25",
    "ajuste_competencia": -1

    },
    "Plena Saúde - Envio Relatório de Sinistralidade": {
    "prazo":"28",
    "ajuste_competencia": -1

    },
    "Plena Saúde - Quiver - Anexar Relatório de Sinistralidade": {
    "prazo":"28",
     "ajuste_competencia": -1

    }
}
        
    for plano in planos_unicos:
        caminho_da_pasta = caminhos.get(plano, "")
        ultima_atualizacao = ultima_data_arquivo(caminho_da_pasta)
        prazo = metadados_etapas.get(plano, {}).get("prazo", "")
        ajuste = metadados_etapas.get(plano, {}).get("ajuste_competencia", -1)  # padrão -1
        competencia = hoje + relativedelta(months=ajuste)  
        competencia_formatada = competencia.strftime("%B/%Y").capitalize()

        dados_etapa = df[df["Plano"] == plano]

        total_pastas = dados_etapa["Total de Pastas"].sum()
        pastas_com_arquivos = dados_etapa["Pastas com Arquivo"].sum()
        progresso = pastas_com_arquivos / total_pastas if total_pastas > 0 else 0
        cor = cor_barra(progresso)

        bloco_html = f"""
        <div style='margin: 16px 0; padding: 12px; border: 2px solid #ddd; border-radius: 8px;'>
            <div style='display: flex; align-items: center; gap: 20px;'>
                <div style='flex: 1;'>{estilizar_plano(plano)}</div>
                <div style='flex: 5;'>
                    <div style='font-size:12px; color:gray'> Competência:{competencia_formatada}  | Prazo:{prazo}  |  Últ. Atualização: {ultima_atualizacao}</div>
                    <div style='background-color:#e0e0e0;border-radius:10px;width:100%;height:20px'>
                        <div style='width:{int(progresso*100)}%;background-color:{cor};height:100%;border-radius:10px;text-align:center;color:white;font-size:12px;'>
                            {int(progresso*100)}%
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        blocos_html_lista.append(bloco_html)

        #st.markdown("### Etapas em Destaque")

        st.components.v1.html("<div style='max-height: 720px; overflow-y: auto; padding-right: 10px;'>" +
        "".join(blocos_html_lista) +
        "</div>",
        height=740,
        )


        # Tabela principal
        st.subheader("Status Geral")
        st.dataframe(df, use_container_width=True)

        # Pastas vazias | Arquivos pendentes
        st.subheader("Arquivos Pendentes")
        pastas_vazias = df[df["Pastas com Arquivo"] == 0]
        df_pendentes = pastas_vazias.rename(columns={
            "Plano": "Etapa",
            "Total de Pastas": "Total de Arquivos",
            "Pastas Vazias": "Arquivos Pendentes"

        })
        st.dataframe(df_pendentes[["Etapa", "Total de Arquivos", "Arquivos Pendentes"]], use_container_width=True)

else:
    st.info("Clique no botão acima para gerar o relatório.")
