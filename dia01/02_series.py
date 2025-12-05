'''
Pandas 2025 - Ensinando Pandas
- Ep 01 - Setup + Series
'''

idades = [11, 21, 27, 18, 32, 19, 43, 23]  # lista

media = sum(idades) / len(idades)
print(f'Média: {media}')

diferenca = 0
for x in idades:
    diferenca += (x - media) ** 2

variancia = diferenca / (len(idades) - 1)

print(f'Variância: {variancia:.4f}')


# Iniciando Aula Pandas (Series)
import pandas as pd

# usando os mesmos valores
idades = [11, 21, 27, 18, 32, 19, 43, 23]  # dataset

series = pd.Series(idades)
print(f'Series: \n{series}')

# estatística Series
media = series.mean()  # média
print(f'Média: {media}')

var_idades = series.var()  # variância
print(f'Variancia: {var_idades:.4f}')

descricao = series.describe()  # descrição
print(f'Descrição: \n{descricao}')
