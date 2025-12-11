'''
Pandas 2025 - Ensinando Pandas
Ep 07 - Novas colunas e ordenação
'''

# %%
import pandas as pd
import numpy as np

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()

# %%
# podemos criar explessões e atribuir a uma nova coluna
df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%
# criando nova coluna com for normal (forma verbosa)
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i + 100)

nova_coluna
df['nova_coluna'] = nova_coluna  # e atribu a nova coluna
df

# %%
# nova coluna combinando duas flags (saber se tem ambos)
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%
# multiplicação de flags
df["flEmail"] * df["flTwitch"]

# %%
# soma de várias flags sociais
df["qtdeSocial"] = (
    df["flEmail"]
    + df["flTwitch"]
    + df["flYouTube"]
    + df["flBlueSky"]
    + df["flInstagram"]
)
df

# %%
# multiplicação de várias flags sociais
df["todas_social"] = (
    df["flEmail"]
    * df["flTwitch"]
    * df["flYouTube"]
    * df["flBlueSky"]
    * df["flInstagram"]
)
df

# %%
df["qtdePontos"]

# %%
# exemplo extra de uso de expressões avançadas, com o uso do numpy
df["logPontos"] = np.log(df["qtdePontos"] + 1)
df["logPontos"].describe()


# %%
# exibe em grafico (matplotlib) a distição de ambas situações
import matplotlib.pyplot as plt

# visualização da distribuição dos pontos
plt.grid(True)
plt.hist(df["qtdePontos"])
plt.show()

# %%
# visualização da distribuição com logaritmo aplicado, numpy.log()
plt.grid(True)
plt.hist(df["logPontos"])
plt.show()
