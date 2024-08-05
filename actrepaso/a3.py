import random

def generar_lista_numeros_aleatorios(cantidad, rango_min, rango_max):
    lista_numeros = [random.randint(rango_min, rango_max) for _ in range(cantidad)]
    return lista_numeros

cantidad = 10  
rango_min = 1  
rango_max = 100

numeros_aleatorios = generar_lista_numeros_aleatorios(cantidad, rango_min, rango_max)

print("lista de numeros aleatorios generada:", numeros_aleatorios)
