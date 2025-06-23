from functions.data_loader import processar_planilha
from functions.db_handler import criar_banco, inserir_dados

# Criar banco (executar uma vez apenas)
criar_banco()

# Processar o Excel (caminho completo do arquivo)
pacientes, valores = processar_planilha("dash-dados/uploads/planilha_teste.xlsx")

# Inserir os dados no banco
inserir_dados(pacientes, valores)

print(" Dados processados e inseridos com sucesso!")
