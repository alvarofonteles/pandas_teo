'''
Pandas 2025 - Ensinando Pandas
- Ep 01 - Setup + Series
'''

# instale esse pacote antes -> pip install kagglehub

import kagglehub
import pandas as pd
import os

# Baixar dataset
path = kagglehub.dataset_download("teocalvo/teomewhy-loyalty-system")

print("Arquivos baixados em:", path)

# Listar arquivos disponíveis
files = os.listdir(path)
print("Arquivos encontrados:", files)

# Procurar o primeiro CSV
csv_files = [f for f in files if f.endswith(".csv")]
if not csv_files:
    raise FileNotFoundError("Nenhum arquivo CSV encontrado no dataset.")

# Usar o primeiro CSV encontrado
file_path = os.path.join(path, csv_files[0])

# Carregar no pandas com separador correto
df = pd.read_csv(file_path, sep=";")

# Mostrar as 10 primeiras linhas
print("Primeiras 10 linhas:")
print(df.head(10))

# baixa em C:\Users\?\.cache\kagglehub\datasets\teocalvo\teomewhy-loyalty-system\versions\1317
