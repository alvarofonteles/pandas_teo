'''
Pandas 2025 - Ensinando Pandas
Ep 03 - Importando dados
'''

# %%
import pandas as pd
import requests

# fonte
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

# requisição user-agent
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers).text

# Passa o conteúdo baixado para o read_html
dfs = pd.read_html(response)  # lista de dataframes
dfs

# %%
df_uf = dfs[1]  # posicao
df_uf.to_csv('ufs.csv', sep=';', index=False)

# %%
# carrega também por default com sep ',' para leitura, então usamos o ';'
df_uf_2 = pd.read_csv('ufs.csv', sep=';')  # com o sep=';'
df_uf_2  # leitura
