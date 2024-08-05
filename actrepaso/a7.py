def encontrar_extremos(lista):
    if not lista:
        return "Vacio", "Vacio"
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

lista_numeros = [34, 7, 23, 56, 12, 89, 4, 0, 23, -5]
maximo, minimo = encontrar_extremos(lista_numeros)
print("El numero más grande en la lista es:", maximo)
print("El numero más pequeño en la lista es:", minimo)
