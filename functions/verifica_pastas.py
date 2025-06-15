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

caminhos_1 = {
    "Planilha de Reavaliação": r"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",

    "Bradesco - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\BASE_CADASTRO",
    "Bradesco - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\BASE_SINISTRO",
    "Bradesco - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\BASE_SINISTRALIDADE",
   
    "Seguros Unimed - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\BASE_CADASTRO" ,
    "Seguros Unimed - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\BASE_SINISTRO" ,
    "Seguros Unimed - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\BASE_SINISTRALIDADE",
    
    "Bradesco (manual) - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\BASE_SINISTRALIDADE",
    
    "SulAmérica - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\BASE_CADASTRO" ,
    "SulAmérica - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\BASE_SINISTRO" ,
    "SulAmérica - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\BASE_SINISTRALIDADE",
    
    "Unimed Nacional - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\BASE_CADASTRO" ,
    "Unimed Nacional - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\BASE_SINISTRO" ,
    "Unimed Nacional - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\BASE_SINISTRALIDADE",
    
    "Porto Seguro - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\BASE_CADASTRO" ,
    "Porto Seguro - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\BASE_SINISTRO" ,
    "Porto Seguro - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\BASE_SINISTRALIDADE",
    
    "Omint - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\BASE_CADASTRO" ,
    "Omint - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\BASE_SINISTRO" ,
    "Omint - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\BASE_SINISTRALIDADE",
    

    "Omint (manual) - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\BASE_SINISTRALIDADE",
    
    "Hapvida - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\BASE_CADASTRO" ,
    "Hapvida - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\BASE_SINISTRO" ,
    "Hapvida - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\BASE_SINISTRALIDADE",


    "Plena Saúde - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\BASE_CADASTRO" ,
    "Plena Saúde - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\BASE_SINISTRO" ,
    "Plena Saúde - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\BASE_SINISTRALIDADE",   
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\RELATORIO",
}

caminhos_2 = {
    "Planilha de Reavaliação": r"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",

    "Amil - Bi Zetta": r"C:\JORGE_V1\Jorge\03_15_AMIL\06.2025\RELATORIO",

    
    "Bradesco - Bi Zetta": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\RELATORIO",   

    
    "Seguros Unimed - Bi Zetta": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\RELATORIO", 
    
    
    "Bradesco (Manual) - Produção Manual": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\RELATORIO",
    
    "SulAmérica - Bi Zetta": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\RELATORIO", 
    
    "Unimed Nacional - Bi Zetta": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\RELATORIO",
    
    "Porto Seguro - Bi Zetta": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\RELATORIO",
    
    "Omint - Bi Zetta": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\RELATORIO",

    "Omint (manual) - Produção Manual": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\RELATORIO",

    "Hapvida - Bi Zetta": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\RELATORIO",

    "Plena Saúde - Bi Zetta": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\RELATORIO",     
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\RELATORIO",
}
caminhos_3 = {    
    "Planilha de Reavaliação": r"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",
    "Amil - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\03_15_AMIL\06.2025\RELATORIO_ENVIADOS",

    "Bradesco - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\RELATORIO_ENVIADOS",

    "Seguros Unimed - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\RELATORIO_ENVIADOS", 
    
    "Bradesco (Manual) - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\RELATORIO_ENVIADOS",
    
    "SulAmérica - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\RELATORIO_ENVIADOS", 
    
    "Unimed Nacional - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\RELATORIO_ENVIADOS",
    
    "Porto Seguro - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\RELATORIO_ENVIADOS",
    
    "Omint - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\RELATORIO_ENVIADOS",

    "Omint (manual) - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\RELATORIO_ENVIADOS",
    
    "Hapvida - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\RELATORIO_ENVIADOS",

    "Plena Saúde - Envio Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\RELATORIO_ENVIADOS",      
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\RELATORIO",
}
caminhos_4 = {
        "Planilha de Reavaliação": r"C:\JORGE_V1\Jorge\PLANILHA_REAVALIACAO_03",
    "Amil - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\03_15_AMIL\06.2025\RELATORIO_QUIVER",

    "Bradesco - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\2_Bradesco\06.2025\RELATORIO_QUIVER",

    "Seguros Unimed - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\7_SEGUROS_UNIMED\06.2025\RELATORIO_QUIVER", 
    
    "Bradesco (Manual) - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\BRADESCO\06.2025\RELATORIO_QUIVER",
    
    "SulAmérica - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\9_SULAMERICA\06.2025\RELATORIO_QUIVER", 
    
    "Unimed Nacional - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\11_UNIMED_NACIONAL_CNU\06.2025\RELATORIO_QUIVER",
    
    "Porto Seguro - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\6_PORTO_SEGURO\06.2025\RELATORIO_QUIVER",
    
    "Omint - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\4_OMINT\06.2025\RELATORIO_QUIVER",

    "Omint (manual) - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\16_RELATORIO MANUAL\OMINT\06.2025\RELATORIO_QUIVER",

    "Hapvida - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\3_Hapvida\06.2025\RELATORIO_QUIVER",

    "Plena Saúde - Quiver - Anexar Relatório de Sinistralidade": r"C:\JORGE_V1\Jorge\5_PLENA_SAUDE\06.2025\RELATORIO_QUIVER",  

    
    

    
    #"GNDI - Arquivo de Cadastro/Faturamento": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_CADASTRO" ,
    #"GNDI - Base Aberta de Sinistro": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRO" ,
    #"GNDI - Relatório Gerencial de Sinistralidade": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\BASE_BI\BASE_SINISTRALIDADE",
    #"GNDI - Bi Zetta": r"C:\JORGE_V1\Jorge\10_GNDI\06.2025\RELATORIO",
}




