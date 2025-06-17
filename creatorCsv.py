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

# Pasta de saída
output_dir = os.path.join("dashboard", "csv")
os.makedirs(output_dir, exist_ok=True)

# Tabelas a gerar
tabelas = [
    ("home.csv", caminhos),
    ("recepcao.csv", caminhos_1),
    ("bi_zetta.csv", caminhos_2),
    ("envio_relatorios.csv", caminhos_3),
    ("anexar_quiver.csv", caminhos_4),
]

# Corrigido: busca arquivos nas subpastas (ex: RELATORIO_ENVIADOS/FCTH)
def obter_ultima_atualizacao(caminho_pasta):
    try:
        arquivos_encontrados = []
        
        if not os.path.exists(caminho_pasta):
            return "Caminho inexistente"
        
        subpastas = [
            os.path.join(caminho_pasta, d)
            for d in os.listdir(caminho_pasta)
            if os.path.isdir(os.path.join(caminho_pasta, d))
        ]
        
        for subpasta in subpastas:
            for arquivo in os.listdir(subpasta):
                caminho_arquivo = os.path.join(subpasta, arquivo)
                if os.path.isfile(caminho_arquivo):
                    arquivos_encontrados.append(caminho_arquivo)

        if not arquivos_encontrados:
            return "Sem arquivos"

        mais_recente = max(os.path.getmtime(f) for f in arquivos_encontrados)
        return datetime.fromtimestamp(mais_recente).strftime("%d/%m/%Y")
    
    except Exception as e:
        return f"Erro: {e}"

# Geração dos CSVs
for nome_csv, dicionario in tabelas:
    try:
        df = gerar_relatorio_pastas(dicionario)

        # Atualização para cada etapa
        df["Últ. Atualização"] = [
            obter_ultima_atualizacao(dicionario.get(etapa)) for etapa in df["Etapa"]
        ]

        # Caminho do CSV final
        caminho_arquivo = os.path.join(output_dir, nome_csv)
        df.to_csv(caminho_arquivo, index=False, encoding="utf-8-sig")
        print(f" CSV gerado: {caminho_arquivo}")
    
    except Exception as e:
        print(f" Erro ao processar {nome_csv}: {e}")
