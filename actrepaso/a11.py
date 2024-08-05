def generar_numeros_pares(inicio, fin):
    lista_pares = [num for num in range(inicio, fin + 1) if num % 2 == 0]
    return lista_pares

inicio = 1
fin = 100
numeros_pares = generar_numeros_pares(inicio, fin)
print("lista de numeros pares entre", inicio, "y", fin, "es:", numeros_pares)
