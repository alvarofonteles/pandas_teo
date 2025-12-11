'''
Pandas 2025 - Ensinando Pandas
Ep 06 - Filtros não são cópias
'''

# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%
filtro = clientes['qtdePontos'] == 0
# recebe o filtro (ponteiro), em uma nova variável
clientes_0 = clientes[filtro] # view

# %%
# na tentativa de alteração da view/referencia gera-se uma exceção
# atenção: pode afetar o original
clientes_0['flag_1'] = 1  # tenta criar uma nova coluna no novo dataframe (referencia/view)
# antes de exibir
clientes_0  # A value is trying to be set on a copy of a slice from a DataFrame.

# %%
# correção, deve ser criado uma cópia (consome memória)
filtro = clientes['qtdePontos'] == 0
clientes_0 = clientes[filtro].copy()

clientes_0['flag_1'] = 1
clientes_0

# `.copy()` não é exclusivo de filtros, mas é essencial sempre que você quiser 
# manipular um subconjunto de dados sem correr risco de alterar o original ou receber avisos.

# %%
# antes sem copy()
A = [1, 2]
B = A
print('A:', A)  # A: [1, 2]
print('B:', B)  # B: [1, 2]
print('')
B.append('mais')
print('A:', A)  # A: [1, 2, 'mais']
print('B:', B)  # B: [1, 2, 'mais']

# %%
# depois com copy
A = [1, 2]
B = A.copy()
print('A:', A)  # A: [1, 2]
print('B:', B)  # B: [1, 2]
print('')
B.append('mais')
print('A:', A)  # A: [1, 2]
print('B:', B)  # B: [1, 2, 'mais']

# %%
