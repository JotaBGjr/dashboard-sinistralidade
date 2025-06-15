import os
import pandas as pd
from datetime import datetime
from functions.verifica_pastas import (
    gerar_relatorio_pastas,
    caminhos,
    caminhos_1,
    caminhos_2,
    caminhos_3,
    caminhos_4
)

# Pasta onde os arquivos serão salvos
output_dir = os.path.join("dashboard", "csv")
os.makedirs(output_dir, exist_ok=True)

# Lista de tuplas com nome do CSV e dicionário de caminhos
tabelas = [
    ("home.csv", caminhos),
    ("recepcao.csv", caminhos_1),
    ("bi_zetta.csv", caminhos_2),
    ("envio_relatorios.csv", caminhos_3),
    ("anexar_quiver.csv", caminhos_4),
]

# Função para obter a última data de modificação de arquivos em uma pasta
def obter_ultima_atualizacao(caminho_pasta):
    try:
        arquivos = [
            os.path.join(caminho_pasta, f)
            for f in os.listdir(caminho_pasta)
            if os.path.isfile(os.path.join(caminho_pasta, f))
        ]
        if not arquivos:
            return "Sem arquivos"
        mais_recente = max(os.path.getmtime(f) for f in arquivos)
        return datetime.fromtimestamp(mais_recente).strftime("%d/%m/%Y")
    except Exception:
        return "Erro"

# Gerar e salvar os CSVs
for nome_csv, dicionario in tabelas:
    try:
        df = gerar_relatorio_pastas(dicionario)

        # Criar lista com a última atualização para cada etapa
        atualizacoes = [
            obter_ultima_atualizacao(dicionario.get(etapa))
            for etapa in df["Etapa"]
        ]

        df["Últ. Atualização"] = atualizacoes

        # Salvar CSV
        caminho_arquivo = os.path.join(output_dir, nome_csv)
        df.to_csv(caminho_arquivo, index=False, encoding="utf-8-sig")
        print(f" CSV gerado: {caminho_arquivo}")
    except Exception as e:
        print(f" Erro ao processar {nome_csv}: {e}")
