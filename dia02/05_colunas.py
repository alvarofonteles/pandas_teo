'''
Pandas 2025 - Ensinando Pandas
Ep 04 - Dataframes
'''

# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')  # uso de nova dataset
df

# %%
df.shape  # linhas e colunas

# %%
df.info(memory_usage='deep')  # exibe o valor real de memoria alocada (80.4 MB)

# %%
df.dtypes  # tipos de dados das colunas

# %%
coluna_renomeada = {'QtdePontos': 'QtPontos', 'DescSistemaOrigem': 'SistemaOrigem'}

# df = df.rename(columns=coluna_renomeada) # nesse caso passa com atribuição
df.rename(columns=coluna_renomeada, inplace=True)  # modifica o próprio dataframe
df

# %%
df[['IdCliente', 'QtPontos']]
df

# pode ser assim melhor
colunas = ['IdCliente', 'QtPontos']
df[colunas]  # acessa mais de uma coluna

# %%
# select * from df
df  # retorna todo dataframe

# %%
# select IdCliente from df
df['IdCliente']  # retorna uma unica coluna, nesse casso uma series

# %%
df[['IdCliente']]  # retorna uma unica coluna, nesse casso [[]] um dataframe

# %%
# select IdCliente, QtPontos from df limit 10
df[['IdCliente', 'QtPontos']].head(10)  # primeiras

# %%
df[['IdCliente', 'QtPontos']].tail(10)  # ultimas

# %%
df[['IdCliente', 'QtPontos']].sample(10)  # uma amostra aleatória

# %%
# select IdCliente, IdTransacao, QtPontos from df limit 15

# as 15 primeiras linhas com 3 colunas (dataframe)
df[['IdCliente', 'IdTransacao', 'QtPontos']].head(15)  # ordem de listagem (digitada)

# %%
# colunas = df.columns.to_list # pode ser assim também a conversao
colunas = list(df.columns)  # converte em lista
colunas.sort()  # ordena alfabeticamente
colunas

df = df[colunas]  # reatribui ao dataframe
df.head()
