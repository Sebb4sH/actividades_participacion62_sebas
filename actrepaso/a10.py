def factorial(numero):
    if numero < 0:
        return "el factorial no está definido para numeros negativos"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero = int(input("ingresa un numero para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}.")
