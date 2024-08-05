def calcular_media(lista):
    if not lista:
        return "la lista está vacia, no se puede calcular la media."
    
    suma = sum(lista)
    cantidad = len(lista)
    media = suma / cantidad
    return media

lista_numeros = [10, 20, 30, 40, 50, 60] 

media = calcular_media(lista_numeros)
print("la media aritmetica de la lista es:", media)
