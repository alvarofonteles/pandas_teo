'''
Pandas 2025 - Ensinando Pandas
Ep 10 - DUPLICATAS
'''

# %%
import pandas as pd

# exemplo com DataFrame contendo duplicatas
df = pd.DataFrame(
    {
        'nome': [
            'teo',
            'lara',
            'nah',
            'bia',
            'mah',
            'lara',
            'mah',
            'mah',
        ],
        'sobrenome': [
            'calvo',
            'calvo',
            'ataide',
            'ataide',
            'silva',
            'silva',
            'silva',
            'silva',
        ],
        'salario': [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
    }
)

df

# %%
# ordena por salário e remove duplicatas mantendo o último registro
df = df.sort_values('salario', ascending=False)
df.drop_duplicates(keep='last', subset=['nome', 'sobrenome'])

# %%
# encadeando sort_values e drop_duplicates, também mantendo o último
df = df.sort_values('salario', ascending=False).drop_duplicates(
    keep='last', subset=['nome', 'sobrenome']
)

df
