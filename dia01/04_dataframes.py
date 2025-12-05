'''
Pandas 2025 - Ensinando Pandas
- Ep 02 - iloc e loc
'''

# %%
import pandas as pd

idades = [11, 21, 27, 18, 32, 19]
nomes = ['Matheus', 'Jose', 'Pedro', 'Maria', 'Ana', 'Marcos']

series_idades = pd.Series(idades)
series_idades

# %%
series_nomes = pd.Series(nomes)
series_nomes

# %%
# cria um datafreme a parti das series idades e nomes
df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_nomes
df  # lista o datafreme formado (tables [idades] [nomes])

# %%
df['nomes']  # torna uma series e acessa o nomes

# %%
df['idades']

# %%
# acesssa o dataframe no indice especifico
# virando uma series, onde a coluna do dataframe torna o indice
df.iloc[0]  # idades: 11 nome: matheus - primeira linha

# %%
type(df.iloc[0])  # series

# %%
# acessa então o indice 'nomes' da seria
df.iloc[0]['nomes']  # Matheus

# %%
df.iloc[-1]['idades']  # 19

# %%
# como o indice é um numero ele acessa o rótulo numerico
df.loc[4]  # idades 32, nomes Ana

# %%
# cria os rótulos pra acessar com `loc` (Extra)
idades2 = [11, 21, 27, 18, 32, 19]
nomes2 = ['Matheus', 'Jose', 'Pedro', 'Maria', 'Ana', 'Marcos']

df2 = pd.DataFrame(idades2, index=nomes2, columns=['idades'])
df2

# %%
df2.loc['Maria']

# %%
df2.loc['Ana']
