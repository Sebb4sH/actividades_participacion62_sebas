def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
lista_invertida = invertir_lista(lista_numeros)
print("la lista invertid es:", lista_invertida)
