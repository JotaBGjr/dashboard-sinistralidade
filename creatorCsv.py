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

output_dir = os.path.join("dashboard", "csv")
os.makedirs(output_dir, exist_ok=True)

tabelas = [
    ("home.csv", caminhos),
    ("recepcao.csv", caminhos_1),
    ("bi_zetta.csv", caminhos_2),
    ("envio_relatorios.csv", caminhos_3),
    ("anexar_quiver.csv", caminhos_4),
]

# Corrigido: busca arquivos em subpastas também
def obter_ultima_atualizacao(caminho_pasta):
    try:
        caminhos_arquivos = []
        for root, dirs, files in os.walk(caminho_pasta):
            for f in files:
                caminho_completo = os.path.join(root, f)
                if os.path.isfile(caminho_completo):
                    caminhos_arquivos.append(caminho_completo)

        if not caminhos_arquivos:
            return "Sem arquivos"

        mais_recente = max(os.path.getmtime(f) for f in caminhos_arquivos)
        return datetime.fromtimestamp(mais_recente).strftime("%d/%m/%Y")
    except Exception:
        return "Erro"

for nome_csv, dicionario in tabelas:
    try:
        df = gerar_relatorio_pastas(dicionario)

        atualizacoes = [
            obter_ultima_atualizacao(dicionario.get(etapa))
            for etapa in df["Etapa"]
        ]
        df["Últ. Atualização"] = atualizacoes

        caminho_arquivo = os.path.join(output_dir, nome_csv)
        df.to_csv(caminho_arquivo, index=False, encoding="utf-8-sig")
        print(f" CSV gerado: {caminho_arquivo}")
    except Exception as e:
        print(f" Erro ao processar {nome_csv}: {e}")
