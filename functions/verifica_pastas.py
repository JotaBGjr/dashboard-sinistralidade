import os
import pandas as pd
from datetime import datetime

def gerar_relatorio_pastas(caminhos):
    
    dados = [] # Lista para guardar cada item analisado

    for etapa, caminho in caminhos.items():
        if os.path.exists(caminho):
            subpastas = [os.path.join(caminho, d) for d in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, d))]

            total_pastas = len(subpastas) 
            pastas_com_arquivos = []
            pasta_vazias = []

            for pasta in subpastas:
                arquivos = os.listdir(pasta)
                if any(os.path.isfile(os.path.join(pasta, f)) for f in arquivos):
                    pastas_com_arquivos.append(os.path.basename(pasta))
                else: pasta_vazias.append(os.path.basename(pasta))

            diferenca = total_pastas - len(pastas_com_arquivos)
            

            pastas_com_arquivos_str = " ,".join(pastas_com_arquivos) if pastas_com_arquivos else "Nenhuma"
            pastas_vazias_str = " ,".join(pasta_vazias) if pasta_vazias else "Nenhuma"

            dados.append([etapa, total_pastas, len(pastas_com_arquivos), diferenca, pastas_vazias_str, pastas_com_arquivos_str])
        else:
            dados.append([etapa, "Caminho não encontrado", "", "", "", ""])
    df = pd.DataFrame(dados, columns=["Etapa", "Total de Pastas", "Pastas com Arquivo", "Diferença", "Pastas Vazias", "Pastas c/ Arquivos"])
 
    return df

mes_ano = "06.2025"
caminhos = {
    "Planilha de Reavaliação": rf"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",

    "Amil - Bi Zetta": rf"C:\JORGE_V1\Jorge\03_15_AMIL\{mes_ano}\RELATORIO",
    "Amil - Envio Relatórios": rf"C:\JORGE_V1\Jorge\03_15_AMIL\{mes_ano}\RELATORIO_ENVIADOS",
    "Amil - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\03_15_AMIL\{mes_ano}\RELATORIO_QUIVER",


    "Bradesco - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\BASE_CADASTRO",
    "Bradesco - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\BASE_SINISTRO",
    "Bradesco - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\BASE_SINISTRALIDADE",
    "Bradesco - Bi Zetta": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\RELATORIO",
    "Bradesco - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\RELATORIO_ENVIADOS",
    "Bradesco - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\RELATORIO_QUIVER",


    "Seguros Unimed - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\BASE_CADASTRO" ,
    "Seguros Unimed - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO" ,
    "Seguros Unimed - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\BASE_SINISTRALIDADE",
    "Seguros Unimed - Bi Zetta": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO", 
    "Seguros Unimed - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO_ENVIADOS",
    "Seguros Unimed - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO_QUIVER",

    "Bradesco (manual) - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\BASE_SINISTRALIDADE",
    "Bradesco (manual) - Produção do Relatório": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\RELATORIO",
    "Bradesco (Manual) - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\RELATORIO_ENVIADOS",
    "Bradesco (Manual) - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\RELATORIO_QUIVER",

    "SulAmérica - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\BASE_CADASTRO" ,
    "SulAmérica - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\BASE_SINISTRO" ,
    "SulAmérica - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\BASE_SINISTRALIDADE",
    "SulAmérica - Bi Zetta": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\RELATORIO",
    "SulAmérica - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\RELATORIO_ENVIADOS",
    "SulAmérica - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\RELATORIO_QUIVER",

    
    "Unimed Nacional - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\BASE_CADASTRO" ,
    "Unimed Nacional - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\BASE_SINISTRO" ,
    "Unimed Nacional - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\BASE_SINISTRALIDADE",
    "Unimed Nacional - Bi Zetta": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\RELATORIO",
    "Unimed Nacional - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\RELATORIO_ENVIADOS",
    "Unimed Nacional - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\RELATORIO_QUIVER",

    
    "Porto Seguro - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\BASE_CADASTRO" ,
    "Porto Seguro - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\BASE_SINISTRO" ,
    "Porto Seguro - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\BASE_SINISTRALIDADE",
    "Porto Seguro - Bi Zetta": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\RELATORIO",
    "Porto Seguro - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\RELATORIO_ENVIADOS",
    "Porto Seguro - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\RELATORIO_QUIVER",
    
    "Omint - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\BASE_CADASTRO" ,
    "Omint - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\BASE_SINISTRO" ,
    "Omint - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\BASE_SINISTRALIDADE",
    "Omint - Bi Zetta": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\RELATORIO",
    "Omint - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\RELATORIO_ENVIADOS",
    "Omint - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\RELATORIO_QUIVER",

    "Omint (manual) - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\BASE_SINISTRALIDADE",
    "Omint (manual) - Produção do Relatório": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\RELATORIO",
    "Omint (manual) - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\RELATORIO_ENVIADOS",
    "Omint (manual) - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\RELATORIO_QUIVER",
   
    #"Hapvida - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\BASE_CADASTRO" ,
    "Hapvida - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\BASE_SINISTRO" ,
    "Hapvida - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\BASE_SINISTRALIDADE",
    "Hapvida - Bi Zetta": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\RELATORIO",
    "Hapvida - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\RELATORIO_ENVIADOS",
    "Hapvida - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\RELATORIO_QUIVER",
    

    "Plena Saúde - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\BASE_CADASTRO" ,
    "Plena Saúde - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\BASE_SINISTRO" ,
    "Plena Saúde - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\BASE_SINISTRALIDADE",
    "Plena Saúde - Bi Zetta": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\RELATORIO",
    "Plena Saúde - Envio Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\RELATORIO_ENVIADOS",
    "Plena Saúde - Quiver - Anexar Relatório de Sinistralidade": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\RELATORIO_QUIVER",


    
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\RELATORIO",

}    

caminhos_1 = {
    "Planilha de Reavaliação": rf"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",

    "Bradesco - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\BASE_CADASTRO",
    "Bradesco - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\BASE_SINISTRO",
    "Bradesco - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\BASE_SINISTRALIDADE",
   
    "Seguros Unimed - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\BASE_CADASTRO" ,
    "Seguros Unimed - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\BASE_SINISTRO" ,
    "Seguros Unimed - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\BASE_SINISTRALIDADE",
    
    "Bradesco (manual) - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\BASE_SINISTRALIDADE",
    
    "SulAmérica - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\BASE_CADASTRO" ,
    "SulAmérica - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\BASE_SINISTRO" ,
    "SulAmérica - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\BASE_SINISTRALIDADE",
    
    "Unimed Nacional - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\BASE_CADASTRO" ,
    "Unimed Nacional - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\BASE_SINISTRO" ,
    "Unimed Nacional - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\BASE_SINISTRALIDADE",
    
    "Porto Seguro - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\BASE_CADASTRO" ,
    "Porto Seguro - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\BASE_SINISTRO" ,
    "Porto Seguro - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\BASE_SINISTRALIDADE",
    
    "Omint - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\BASE_CADASTRO" ,
    "Omint - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\BASE_SINISTRO" ,
    "Omint - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\BASE_SINISTRALIDADE",
    

    "Omint (manual) - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\BASE_SINISTRALIDADE",
    
    #"Hapvida - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\BASE_CADASTRO" ,
    "Hapvida - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\BASE_SINISTRO" ,
    "Hapvida - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\BASE_SINISTRALIDADE",


    "Plena Saúde - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\BASE_CADASTRO" ,
    "Plena Saúde - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\BASE_SINISTRO" ,
    "Plena Saúde - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\BASE_SINISTRALIDADE",   
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\RELATORIO",
}

caminhos_2 = {
   

    "Amil": rf"C:\JORGE_V1\Jorge\03_15_AMIL\{mes_ano}\RELATORIO",

    
    "Bradesco": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\RELATORIO",   

    
    "Seguros Unimed": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO", 
    
    
    "Bradesco (Manual) - Produção Manual": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\RELATORIO",
    
    "SulAmérica": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\RELATORIO", 
    
    "Unimed Nacional": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\RELATORIO",
    
    "Porto Seguro": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\RELATORIO",
    
    "Omint": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\RELATORIO",

    "Omint (manual)": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\RELATORIO",

    "Hapvida": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\RELATORIO",

    "Plena Saúde": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\RELATORIO",     
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\RELATORIO",
}
caminhos_3 = {    

    "Amil": rf"C:\JORGE_V1\Jorge\03_15_AMIL\{mes_ano}\RELATORIO_ENVIADOS",

    "Bradesco": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\RELATORIO_ENVIADOS",

    "Seguros Unimed": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO_ENVIADOS", 
    
    "Bradesco (Manual)": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\RELATORIO_ENVIADOS",
    
    "SulAmérica": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\RELATORIO_ENVIADOS", 
    
    "Unimed Nacional": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\RELATORIO_ENVIADOS",
    
    "Porto Seguro": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\RELATORIO_ENVIADOS",
    
    "Omint": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\RELATORIO_ENVIADOS",

    "Omint (manual)": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\RELATORIO_ENVIADOS",
    
    "Hapvida": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\RELATORIO_ENVIADOS",

    "Plena Saúde": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\RELATORIO_ENVIADOS",      
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\RELATORIO",
}
caminhos_4 = {
   
    "Amil": rf"C:\JORGE_V1\Jorge\03_15_AMIL\{mes_ano}\RELATORIO_QUIVER",

    "Bradesco": rf"C:\JORGE_V1\Jorge\2_Bradesco\{mes_ano}\RELATORIO_QUIVER",

    "Seguros Unimed": rf"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\{mes_ano}\RELATORIO_QUIVER", 
    
    "Bradesco (Manual)": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\{mes_ano}\RELATORIO_QUIVER",
    
    "SulAmérica - Quiver": rf"C:\JORGE_V1\Jorge\9_SULAMERICA\{mes_ano}\RELATORIO_QUIVER", 
    
    "Unimed Nacional": rf"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\{mes_ano}\RELATORIO_QUIVER",
    
    "Porto Seguro": rf"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\{mes_ano}\RELATORIO_QUIVER",
    
    "Omint": rf"C:\JORGE_V1\Jorge\4_OMINT\{mes_ano}\RELATORIO_QUIVER",

    "Omint (manual) ": rf"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\{mes_ano}\RELATORIO_QUIVER",

    "Hapvida": rf"C:\JORGE_V1\Jorge\3_Hapvida\{mes_ano}\RELATORIO_QUIVER",

    "Plena Saúde": rf"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\{mes_ano}\RELATORIO_QUIVER",  

    
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": rf"C:\JORGE_V1\Jorge\10_GNDI\{mes_ano}\RELATORIO",
}




