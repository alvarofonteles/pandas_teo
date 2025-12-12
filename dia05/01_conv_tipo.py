'''
Pandas 2025 - Ensinando Pandas
Ep 08 - ASTYPE e REPLACE
'''

# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()

# %%
# converte para o tipo int/float...
df['qtdePontos'].astype(int)

# %%
# conversao aninhada pois a primeira se trata de series (float > string)
df['qtdePontos'].astype(float).astype(str)

# %%
# acita mais de um replace pois se trata de uma lista (dict)
df['DtCriacao'].replace(
    {
        '0000-00-00 00:00:00.000': '2024-02-01 09:00:00.000',
        '2025-08-25 13:09:12.556': '2025-12-12 11:14:00.000',
    }
)

# %%
# agora sim pode fazer a conversao para data usando o pandas
pd.to_datetime(df['DtCriacao'])

# %%
# também pode fazer direto, conversao com replace
replace = {'0000-00-00 00:00:00.000': '2024-02-01 09:00:00.000'}

# atribui para a propria coluna (é uma copy)
df['DtCriacao'] = pd.to_datetime(df['DtCriacao'].replace(replace))
df['DtCriacao']

# %%
# apos a conversao usando o to_datetime, podemos usar o .dt
# para meses, anos, dias etc
df['DtCriacao'] = pd.to_datetime(
    df['DtCriacao'].replace(replace)
).dt.month  # series year month day minute
df['DtCriacao']

# %%
