'''
Pandas 2025 - Ensinando Pandas
- Ep 02 - iloc e loc
'''

import pandas as pd

# usando os mesmos valores
idades = [11, 21, 27, 18, 32, 19]  # dataset

series = pd.Series(idades)

print(idades[0])  # acessa o idx da lista
print(series[0])  # acessa a chave da Series

# series[-1] # KeyError: -1

series = series.sort_values()  # ordena
print(series)  # key & value

# usando `iloc` acessa o índice
print(series.iloc[0])  # acessa o indice da Series

print(series.iloc[-1])  # acessa a ultima

print(series.iloc[:3])  # primeiros 3

print(series.iloc[::-1])  # acessa da ultima pra primeira (invertido)

# Data set com Indices
idades = [11, 21, 27, 18, 32, 19]  # dataset

indices = ['Matheus', 'Jose', 'Pedro', 'Maria', 'Ana', 'Marcos']  # index

series = pd.Series(idades, index=indices)
print(series)

print(series.iloc[-1])

# dataframe (próxima aula - Extra)
idades = [[11, 21], [27, 18], [32, 19]]  # dataset
indices = ['Matheus', 'Jose', 'Pedro']
colunas = ['A', 'B']

df = pd.DataFrame(idades, indices, colunas)
print(df)

# loc
print(df.loc['Pedro'])
