'''
Pandas 2025 - Ensinando Pandas
Ep 11 - APPLY
'''

# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()


# %%
# função para extrair o último segmento do idCliente
def get_last_id(idCliente):
    return idCliente.split('-')[-1]


# %%
teste_func = get_last_id('0033b737-8235-4c0f-9801-dc4ca185af00')
teste_func

# %%
# aplicação manual da função com loop
id_novo = []

for i in df['idCliente']:
    novo = get_last_id(i)
    id_novo.append(novo)

df['novo_id'] = id_novo
df.head()

# %%
# aplicação direta da função com apply()
df['idCliente'].apply(get_last_id)
