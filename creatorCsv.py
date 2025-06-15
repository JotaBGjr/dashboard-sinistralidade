import os
import pandas as pd
from verifica_pastas import gerar_relatorio_pastas, caminhos, caminhos_1, caminhos_2, caminhos_3, caminhos_4

# Criar a pasta se não existir
output_dir = os.path.join("dashboard", "csv")
os.makedirs(output_dir, exist_ok=True)

# Lista de tuplas com nome do arquivo e dicionário correspondente
tabelas = [
    ("home.csv", caminhos),
    ("recepcao.csv", caminhos_1),
    ("bi_zetta.csv", caminhos_2),
    ("envio_relatorios.csv", caminhos_3),
    ("anexar_quiver.csv", caminhos_4),
]

# Gerar os arquivos CSV
for nome_csv, dicionario in tabelas:
    df = gerar_relatorio_pastas(dicionario)
    caminho_arquivo = os.path.join(output_dir, nome_csv)
    df.to_csv(caminho_arquivo, index=False)
    print(f"Arquivo salvo: {caminho_arquivo}")