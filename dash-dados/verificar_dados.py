import sqlite3
import pandas as pd

DB_PATH = "dash-dados/db/pacientes.db"

#Conexão com banco
conn = sqlite3.connect(DB_PATH)

print("\n Pacientes:")
df_pacientes = pd.read_sql_query("SELECT * FROM pacientes LIMIT 10", conn)
print(df_pacientes)

#Visualizar valores mensais
print("\n Valores mensais:")
df_valores = pd.read_sql_query("SELECT * FROM valores_mensais LIMIT 10", conn)
print(df_valores)

conn.close()