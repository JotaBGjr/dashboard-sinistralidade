import os

# Dicionário de caminhos
caminhos = {
    "Planilha de Reavaliação": r"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",

    "Amil - Bi Zetta": r"C:\JORGE_V1\Jorge\03_15_AMIL\06.2025\RELATORIO",
    "Amil - Envio Relatórios": r"C:\JORGE_V1\Jorge\03_15_AMIL\06.2025\RELATORIO_ENVIADOS",
    "Amil - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\03_15_AMIL\06.2025\RELATORIO_QUIVER",


    "Bradesco - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\BASE_CADASTRO",
    "Bradesco - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\BASE_SINISTRO",
    "Bradesco - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\BASE_SINISTRALIDADE",
    "Bradesco - Bi Zetta": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\RELATORIO",
    "Bradesco - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\RELATORIO_ENVIADOS",
    "Bradesco - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\RELATORIO_QUIVER",


    "Seguros Unimed - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\BASE_CADASTRO" ,
    "Seguros Unimed - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\BASE_SINISTRO" ,
    "Seguros Unimed - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\BASE_SINISTRALIDADE",
    "Seguros Unimed - Bi Zetta": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\RELATORIO", 
    "Seguros Unimed - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\RELATORIO_ENVIADOS",
    "Seguros Unimed - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\RELATORIO_QUIVER",

    "Bradesco (manual) - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\BASE_SINISTRALIDADE",
    "Bradesco (manual) - Produção do Relatório": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\RELATORIO",
    "Bradesco (Manual) - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\RELATORIO_ENVIADOS",
    "Bradesco (Manual) - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\RELATORIO_QUIVER",

    "SulAmérica - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\BASE_CADASTRO" ,
    "SulAmérica - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\BASE_SINISTRO" ,
    "SulAmérica - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\BASE_SINISTRALIDADE",
    "SulAmérica - Bi Zetta": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\RELATORIO",
    "SulAmérica - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\RELATORIO_ENVIADOS",
    "SulAmérica - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\RELATORIO_QUIVER",

    
    "Unimed Nacional - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\BASE_CADASTRO" ,
    "Unimed Nacional - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\BASE_SINISTRO" ,
    "Unimed Nacional - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\BASE_SINISTRALIDADE",
    "Unimed Nacional - Bi Zetta": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\RELATORIO",
    "Unimed Nacional - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\RELATORIO_ENVIADOS",
    "Unimed Nacional - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\RELATORIO_QUIVER",

    
    "Porto Seguro - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\BASE_CADASTRO" ,
    "Porto Seguro - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\BASE_SINISTRO" ,
    "Porto Seguro - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\BASE_SINISTRALIDADE",
    "Porto Seguro - Bi Zetta": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\RELATORIO",
    "Porto Seguro - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\RELATORIO_ENVIADOS",
    "Porto Seguro - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\RELATORIO_QUIVER",
    
    "Omint - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\BASE_CADASTRO" ,
    "Omint - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\BASE_SINISTRO" ,
    "Omint - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\BASE_SINISTRALIDADE",
    "Omint - Bi Zetta": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\RELATORIO",
    "Omint - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\RELATORIO_ENVIADOS",
    "Omint - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\RELATORIO_QUIVER",

    "Omint (manual) - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\BASE_SINISTRALIDADE",
    "Omint (manual) - Produção do Relatório": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\RELATORIO",
    "Omint (manual) - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\RELATORIO_ENVIADOS",
    "Omint (manual) - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\RELATORIO_QUIVER",
   
    "Hapvida - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\BASE_CADASTRO" ,
    "Hapvida - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\BASE_SINISTRO" ,
    "Hapvida - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\BASE_SINISTRALIDADE",
    "Hapvida - Bi Zetta": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\RELATORIO",
    "Hapvida - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\RELATORIO_ENVIADOS",
    "Hapvida - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\RELATORIO_QUIVER",
    

    "Plena Saúde - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\BASE_CADASTRO" ,
    "Plena Saúde - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\BASE_SINISTRO" ,
    "Plena Saúde - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\BASE_SINISTRALIDADE",
    "Plena Saúde - Bi Zetta": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\RELATORIO",
    "Plena Saúde - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\RELATORIO_ENVIADOS",
    "Plena Saúde - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\RELATORIO_QUIVER",


    
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\RELATORIO",

}

def calcular_tamanho_pasta(pasta):
    total_bytes = 0
    for raiz, dirs, arquivos in os.walk(pasta):
        for nome_arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                total_bytes += os.path.getsize(caminho_arquivo)
    return total_bytes

# Soma total acumulada
total_geral_bytes = 0

print("Tamanho das pastas:")
for nome, caminho in caminhos.items():
    if os.path.exists(caminho):
        tamanho_bytes = calcular_tamanho_pasta(caminho)
        tamanho_gb = tamanho_bytes / (1024 ** 3)
        total_geral_bytes += tamanho_bytes
        print(f"- {nome}: {tamanho_gb:.2f} GB")
    else:
        print(f"- {nome}: Caminho não encontrado!")

# Exibe o total geral em GB
total_geral_gb = total_geral_bytes / (1024 ** 3)
print(f"\n Tamanho total acumulado: {total_geral_gb:.2f} GB")
