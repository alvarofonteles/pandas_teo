'''
Pandas 2025 - Ensinando Pandas
Ep 05 - Filtros
'''

# %%
import pandas as pd

pontos = [8, 17, 11, 5, 47, 20, 10, 100, 52, 35]
filtro = []

# pode ser dessa forma usando o for padrão
for i in pontos:
    filtro.append(i >= 35)

filtro  # [False, False, False, False, True, False, False, True, True, True]

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

print('for normal')
resultado  # [47, 100, 52, 35]

# %%
# pode ser juntando todos num for com enumerate
resultado = []
for idx, i in enumerate(pontos):
    filtro.append(i >= 35)
    if filtro[idx]:
        resultado.append(pontos[idx])

print('for com enumerate')
resultado  # [47, 100, 52, 35]

# %%
# ou mais avançado, usando o list comprehension
resultado = [i for i in pontos if i >= 35]  # em uma unica linha

print('com list comprehension')
resultado  # [47, 100, 52, 35]

# %%
apostolos = pd.DataFrame(
    {
        'nome': ['matheus', 'lucas', 'joão'],
        'idade': [17, 35, 28],
        'uf': ['ce', 'pr', 'rn'],
    }
)

# devolve uma series, com as idades
apostolos['idade']

# %%
# faz a comparação, mas devolve uma series, true ou false (bool)
apostolos['idade'] >= 18

# %%
filtro = apostolos['idade'] >= 18  # armazena a nova series em uma variavel
apostolos[filtro]  # e cria-se um novo dataframe filtrado

# %%
# como se passase literal [False, True, True] dentro do dataframe
apostolos[[False, True, True]]  # mesmo resultado


# usando agora dados reais do dataset transacoes.csv
# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv')
df.head()

# %%
# valores maiores que 50
filtro = df['QtdePontos'] >= 50
df[filtro]

# %%
# valores entre 50 (inclusive) e 100
# usando o operador lógico do Pandas & (and)
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)
filtro  # devolver uma seriea de bool
df[filtro]  # cria a nova estrutura

# %%
# usando o operador lógico do Pandas | (or)
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]

# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente
# usando ambos operadores lógico do Pandas & (and) e | (or)
# a logica deve ser entre parenteses ()
filtro = ((df['QtdePontos'] > 0) & (df['QtdePontos'] <= 50)) | (
    df['dtCriacao'] >= '2025-01-01'
)
df[filtro]


# tabela verdade
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False
