#Este es un programa para saber cuales son los numeros y estrellas mas frecuentes y menos frecuentes en el Euromillon.


import pandas as pd
from itertools import combinations

# Cargar el archivo CSV
df = pd.read_csv('/Users/marcelrubin/Desktop/Euromillon/numeros_historicos.csv')

# Obtener los 5 números principales más frecuentes
top_5_numeros = list(pd.concat([df['num1'], df['num2'], df['num3'], df['num4'], df['num5']]).value_counts().head(5).index)
print("Los 5 números principales más frecuentes son:", top_5_numeros)


# Obtener los 5 números principales menos frecuentes
bottom_5_numeros = list(pd.concat([df['num1'], df['num2'], df['num3'], df['num4'], df['num5']]).value_counts().tail(5).index)
print("\nLos 5 números principales menos frecuentes son:", bottom_5_numeros)

# Generar combinaciones de los 5 números más frecuentes
combinaciones_top_5_numeros = list(combinations(top_5_numeros, 5))
print("\nCombinaciones de los 5 números más frecuentes:")
for c in combinaciones_top_5_numeros:
    print(c)

# Generar combinaciones de los 5 números menos frecuentes
combinaciones_bottom_5_numeros = list(combinations(bottom_5_numeros, 5))
print("\nCombinaciones de los 5 números menos frecuentes:")
for c in combinaciones_bottom_5_numeros:
    print(c)