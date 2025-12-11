'''
Pandas 2025 - Ensinando Pandas
Ep 05 - Filtros
'''

# %%
import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv')
df.head()

# %%
filtro = (df['IdProduto'] == 5) | (df['IdProduto'] == 11)
df[filtro]

# %%
# mesma forma do filtro anterior, mas usando o isin()
filtro = df['IdProduto'].isin([5, 11])  # contém
df[filtro]

# %%
# com outro caso real anterior clientes.csv
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%
# mesma forma de negação (not null)
# usando o notnull() > pouco usado
filtro = clientes['DtCriacao'].notnull()  # retorna uma series
clientes[filtro]

# %%
# usando o notna()
filtro = clientes['DtCriacao'].notna()  # retorna uma series
clientes[filtro]

# %%
# mesma forma de negação (null)
# usando o notna() e isna()
~clientes['DtCriacao'].isna()  # retorna uma series

# %%
filtro = clientes['DtCriacao'].notna()
clientes[filtro]
