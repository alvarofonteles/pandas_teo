'''
Pandas 2025 - Ensinando Pandas
Ep 07 - Novas colunas e ordenação
'''

# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()


# %%
# ordena pela coluna do dataframe e retorna uma series
df['qtdePontos'].sort_values()

# %%
# metodo paleativo/alternativo usando max
max_ponto = df['qtdePontos'].max()
filtro = df['qtdePontos'] == max_ponto
df[filtro]

# %%
# ordena pelo proprio dataframe, passando a coluna e por ordem decrescente
df.sort_values(by='qtdePontos', ascending=False)

# %%
# permanece sem alteracao ois o sort_value é uma cópia e não uma view
df

# %%
# retorna os 5 primeiros registros após ordenação
df.sort_values(by='qtdePontos', ascending=False).head()

# %%
# retorna os 5 primeiros 'idCliente' após ordenação
top_5 = df.sort_values(by='qtdePontos', ascending=False).head(5)['idCliente']
top_5
# type(top_5) # Series

# %%
# dataframe de salários
salario = pd.DataFrame(
    {
        'nome': ['lucas', 'matheus', 'tiago', 'joão'],
        'idade': [32, 43, 35, 42],
        'salario': [2345, 4533, 3245, 4533],
    }
)

salario


# %%
# ordena por salário em ordem decrescente
salario.sort_values(by='salario', ascending=False)

# %%
# ordena por salário e idade, ambos em ordem decrescente
salario.sort_values(by=['salario', 'idade'], ascending=False)

# %%
# ordena por salário decrescente e idade crescente
salario.sort_values(by=['salario', 'idade'], ascending=[False, True])
