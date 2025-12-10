'''
Pandas 2025 - Ensinando Pandas
Ep 03 - Importando dados
'''

# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')  # carrega com sep ';' para leitura
df  # leitura

# %%
# salva uma cópia do arquivo, nesse caso com o index que vem por padrão
df.to_csv('clientes.csv', index=False)  # não salva com index, e salva por padrão ','

# %%
# carrega também por default com sep ',' para leitura
df_2 = pd.read_csv('clientes.csv')  # implicito sem o sep=','
df_2  # leitura

# %%
df.to_parquet(
    'clientes.parquet', index=False, engine='fastparquet'
)  # nesse caso tem que deixar explicito o 'engine='fastparquet'

# %%
df_3 = pd.read_parquet(
    'clientes.parquet', engine='fastparquet'
)  # são arquivos binários
df_3

# %%
df.to_excel('clientes.xlsx', index=False)

# %%
df_4 = pd.read_excel('clientes.xlsx')
df_4

# %%
df_sep = pd.read_csv('../data/com_sep.csv', sep=';')
df_sep
