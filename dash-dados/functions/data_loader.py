import pandas as pd
from datetime import datetime

# Função para converter datas seriais do Excel para datetime
def converter_datas_excel(colunas):
    return pd.to_datetime(colunas.astype(int), unit="D", origin="1899-12-30")

# Função principal para carregar e processar a planilha
def processar_planilha(path_arquivo):
    aba = "ANÁLISES MÉDICAS"
    df = pd.read_excel(path_arquivo, sheet_name=aba, header=1)

    # Extrair metadados da célula A1
    df_meta = pd.read_excel(path_arquivo, sheet_name=aba, header=None, nrows=1, usecols="A")
    meta_str = df_meta.iloc[0, 0]  # ex: "VITAE | AMIL | SAÚDE | ... | 11/2024 A 03/2025"

    partes = [parte.strip() for parte in meta_str.split("|")]
    periodo_str = partes[-1] if partes else ""
    periodo_inicio, periodo_fim = None, None
    try:
        data_inicio_str, data_fim_str = periodo_str.split(" A ")
        periodo_inicio = pd.to_datetime("01/" + data_inicio_str, dayfirst=True)
        periodo_fim = pd.to_datetime("01/" + data_fim_str, dayfirst=True) + pd.offsets.MonthEnd(0)
    except:
        pass

    # Identificar colunas de datas seriais (entre "Qtd. Amb e terapia" e "Total")
    colunas = df.columns.tolist()
    # Limpa os nomes das colunas para facilitar comparação
    colunas_limpa = [str(c).strip().replace('\n', ' ').replace('  ', ' ') for c in colunas]

    # Localiza as posições reais
    try:
        colunas=limpa = [str(c).strip().replace('\n',' ').replace('  ') for c in colunas]

        print("colunas limpas:")
        for c in colunas_limpa:
            print("-", c)
        idx_inicio = colunas_limpa.index("Qtd. Amb e terapia") + 1
        idx_fim = colunas_limpa.index("Total")
    except ValueError as e:
        raise ValueError("Erro ao localizar colunas de datas: " + str(e))
        colunas_datas = colunas[idx_inicio:idx_fim]

    # Extrair e tratar dados estáticos (cadastro)
    dados_pacientes = []
    dados_valores = []
    data_upload = datetime.today().date()

    for _, row in df.iterrows():
        benef = str(row["Beneficiario"])
        if " - " in benef:
            id_ext, nome = benef.replace("B#", "").split(" - ", 1)
        else:
            id_ext, nome = "", benef

        paciente = {
            "id_externo": id_ext,
            "nome": nome.strip(),
            "titular": row.get("Titular", ""),
            "operadora": row.get("Operadora", ""),
            "titularidade": row.get("Titularidade", ""),
            "status": row.get("Status", ""),
            "sexo": row.get("Sexo", ""),
            "idade": int(row.get("Idade", 0)),
            "plano": row.get("Plano", ""),
            "subfatura": row.get("SubFatura", ""),
            "potencial_diabetico": row.get("Potencial  Diabético", ""),
            "potencial_hipertenso": row.get("Potencial  Hipertenso", ""),
            "potencial_dpoc": row.get("Potencial  DPOC", ""),
            "criticidade": row.get("Criticidade", ""),
            "especialidade": row.get("Especialidade", ""),
            "cirurgico_clinico": row.get("Cirúrgico/Clínico", ""),
            "cid": row.get("Cid", ""),
            "hipotese_diagnostica": row.get("Hipótese Diagnóstica / Procedimentos", ""),
            "prestador": row.get("Prestador", ""),
            "arquivo_origem": path_arquivo.split("/")[-1],
            "periodo_inicio": periodo_inicio,
            "periodo_fim": periodo_fim,
            "data_upload": data_upload
        }
        dados_pacientes.append(paciente)

        # Processar valores mensais
        for col_serial in colunas_datas:
            valor = row.get(col_serial)
            if pd.isna(valor):
                continue
            try:
                data_real = pd.to_datetime(int(col_serial), unit='D', origin='1899-12-30')
                dados_valores.append({
                    "paciente_id_externo": id_ext,
                    "data_referencia": data_real,
                    "valor": float(valor),
                    "arquivo_origem": path_arquivo.split("/")[-1]
                })
            except:
                continue

    return dados_pacientes, dados_valores
