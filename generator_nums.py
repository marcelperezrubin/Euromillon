#Esto es un programa que genera 1 combinación de 5 numeros y 2 estrellas que no han salido en el Euromillon.

import itertools
import csv
import random

todos_los_numeros = list(range(1, 51))
todas_las_estrellas = list(range(1, 13))

with open('numeros_historicos.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # omitir encabezados
    numeros_historicos = [set(row[1:6] + row[7:9]) for row in reader]

while True:
    combinacion = random.sample(todos_los_numeros, 5) + random.sample(todas_las_estrellas, 2)
    if set(combinacion) not in numeros_historicos:
        break


print("La combinación generada es: [", end="")
print(*combinacion[:5], sep=", ", end="")
print("] y [", end="")
print(*combinacion[5:], sep=", ", end="")
print("]")
