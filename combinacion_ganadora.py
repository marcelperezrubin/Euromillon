#Este es un programa para generar combinaciones aleatorias del Euromillon.

import random

def generar_combinacion():
    numeros = []
    estrellas = []
    
    # Generamos 5 números aleatorios del 1 al 50
    while len(numeros) < 5:
        numero = random.randint(1, 50)
        if numero not in numeros:
            numeros.append(numero)
    
    # Generamos 2 estrellas aleatorias del 1 al 12
    while len(estrellas) < 2:
        estrella = random.randint(1, 12)
        if estrella not in estrellas:
            estrellas.append(estrella)
    
    # Ordenamos los números de menor a mayor
    numeros.sort()
    
    # Devolvemos la combinación generada
    return numeros + estrellas

# Ejemplo de uso: generamos una combinación y la imprimimos en pantalla
combinacion_ganadora = generar_combinacion()
print("La combinación ganadora es:", combinacion_ganadora)