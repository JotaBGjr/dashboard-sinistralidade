import sqlite3
import pandas as pd
from datetime import datetime

# Caminho do banco de dados
DB_PATH = "dash-dados/db/pacientes.db"

# Cria as tabelas se não existirem
def criar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_externo TEXT UNIQUE,
        nome TEXT,
        titular TEXT,
        operadora TEXT,
        titularidade TEXT,
        status TEXT,
        sexo TEXT,
        idade INTEGER,
        plano TEXT,
        subfatura TEXT,
        potencial_diabetico TEXT,
        potencial_hipertenso TEXT,
        potencial_dpoc TEXT,
        criticidade TEXT,
        especialidade TEXT,
        cirurgico_clinico TEXT,
        cid TEXT,
        hipotese_diagnostica TEXT,
        prestador TEXT,
        arquivo_origem TEXT,
        periodo_inicio DATE,
        periodo_fim DATE,
        data_upload DATE
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS valores_mensais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        data_referencia DATE,
        valor FLOAT,
        arquivo_origem TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
    )''')

    conn.commit()
    conn.close()

# Insere os dados no banco

def inserir_dados(dados_pacientes, dados_valores):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    paciente_id_map = {}
    for paciente in dados_pacientes:
        #converter campos Timestamp´
        for campo in ["periodo_inicio", "periodo_fim", "data_upload"]:
            if isinstance(paciente[campo], pd.Timestamp):
                paciente[campo] = paciente[campo].date()

        id_ext = paciente["id_externo"]

        # Verifica se já existe
        cursor.execute("SELECT id FROM pacientes WHERE id_externo = ?", (id_ext,))
        res = cursor.fetchone()

        if res:
            paciente_id = res["id"]
        else:
            campos = list(paciente.keys())
            valores = [paciente[c] for c in campos]
            cursor.execute(f"INSERT INTO pacientes ({', '.join(campos)}) VALUES ({', '.join(['?']*len(campos))})", valores)
            
            paciente_id = cursor.lastrowid

        paciente_id_map[id_ext] = paciente_id

    for item in dados_valores:
        paciente_id - paciente_id_map.get(item["paciente_id_externo"])
        if not paciente_id:
            continue

        cursor.execute(

            ''' 
            INSERT INTO valores_mensais (paciente_id, data_referencia, valor, arquivo_origem)
            VALUES (?, ?, ?, ?)
            ''',
            (paciente_id, item["data_referencia"], item["valor"], item["arquivo_origem"])


        )

    conn.commit()
    conn.close()
