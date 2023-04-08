#Esto es un programa para saber cuales son los 5 numeros y 2 Estrellas mas frecuentes y menos frecuentes del Euromillon.



import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('/Users/marcelrubin/Desktop/Euromillon/numeros_historicos.csv')

# Concatenar las columnas de números en una sola serie
numeros = pd.concat([df['num1'], df['num2'], df['num3'], df['num4'], df['num5']])

# Obtener los 5 números principales más frecuentes
top_5_numeros = numeros.value_counts().head(5)
print("Los 5 números principales más frecuentes son:\n", top_5_numeros)

# Obtener los 5 números principales menos frecuentes
bottom_5_numeros = numeros.value_counts().tail(5)
print("\nLos 5 números principales menos frecuentes son:\n", bottom_5_numeros)

# Concatenar las columnas de estrellas en una sola serie
estrellas = pd.concat([df['estrella1'], df['estrella2']])

# Obtener las 2 estrellas más frecuentes
top_2_estrellas = estrellas.value_counts().head(2)
print("\nLas 2 estrellas más frecuentes son:\n", top_2_estrellas)

# Obtener las 2 estrellas menos frecuentes
bottom_2_estrellas = estrellas.value_counts().tail(2)
print("\nLas 2 estrellas menos frecuentes son:\n", bottom_2_estrellas)