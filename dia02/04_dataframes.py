'''
Pandas 2025 - Ensinando Pandas
Ep 04 - Dataframes
'''

# %%
import pandas as pd

df_cli = pd.read_csv('../data/clientes.csv', sep=';')
df_cli

# %%
# amostra
# mostra as 7 primieira linhas, passa o valor como argumento
df_cli.head(n=7)  # nesse caso 7 linhas

# %%
# mostra as 7 últimas linhas, passa o valor como argumento
df_cli.tail(7)

# %%
df_cli.sample(7)

# %%
# mostra uma tupla, onde mostra quantidade de linhas e colunas
df_cli.shape  # nesse caso (4440, 9) linhas e colunas

# %%
ldf = df_cli.columns  # exibe os nomes das colunas uma lista/indice
list(ldf)  # converte em lista

# %%
# exibe nesse argumento a quantiade de linhas
df_cli.index  # inica em zero e vai até n-1 (4440)

# %%
df_cli.info()  # exibe uma strig de informacoes sobre o dataframe
# inclui numero de colunas linhas, dtipos, e memoria

# %%
# da msm forma que o anterior mas com limitacao de colunas
df_cli.info(memory_usage='deep', max_cols=2)  # exibe o valor real de memoria alocada

# %%
# exibe uma series de informações das colunas e tipos
df_cli.dtypes  # series

# podendo acessar nesse caso um especifico
df_cli.dtypes['flInstagram']  # dtype('int64')
