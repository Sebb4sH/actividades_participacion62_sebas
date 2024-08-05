import random

def generar_matriz(filas, columnas, valor_min, valor_max):
    matriz = [[random.randint(valor_min, valor_max) for _ in range(columnas)] for _ in range(filas)]
    return matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

filas = 4  
columnas = 5  
valor_min = 1  
valor_max = 100 

matriz = generar_matriz(filas, columnas, valor_min, valor_max)
print("matriz generada:")
imprimir_matriz(matriz)
