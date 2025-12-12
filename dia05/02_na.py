'''
Pandas 2025 - Ensinando Pandas
Ep 09 - Dados Faltantes!
'''

# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%
# remove todas as linhas que tenham pelo menos um NaN
clientes.dropna()

# %%
# remove linhas onde todos os valores são NaN
clientes.dropna(how='all')

# %%
# remove linhas onde qualquer valor seja NaN
clientes.dropna(how='any')

# %%
# valores faltantes
df = pd.DataFrame(
    {
        'nome': ['Lucas', None, 'Matheus', 'João'],
        'idade': [None, None, 34, 25],
        'salario': [4235, 2341, None, 7259],
    }
)

df

# %%
# remove linhas onde 'idade' e 'nome' são ambos NaN
df.dropna(how='all', subset=['idade', 'nome'])

# %%
# preenche valores NaN na coluna 'idade' com 0
df['idade'] = df['idade'].fillna(0)
df

# %%
# preenche valores NaN com dicionário de substituição
df.fillna({'nome': 'alguem', 'idade': 0})

# %%
# calcula médias e usa para preencher NaN
medias = df[['idade', 'salario']].mean()
df.fillna(medias)

# %%
# preenche NaN em 'idade' com média da coluna e calcula média novamente
df['idade'].fillna(df['idade'].mean()).mean()
