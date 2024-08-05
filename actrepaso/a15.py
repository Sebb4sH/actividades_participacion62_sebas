def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
texto = input("ingresa una cadena de texto: ")

if es_palindromo(texto):
    print(f'"{texto}" es un palindromo.')
else:
    print(f'"{texto}" no es un palindromo.')
