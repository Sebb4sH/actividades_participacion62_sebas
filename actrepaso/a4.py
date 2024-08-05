#punto4
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingresa un numero: "))
resultado = es_par_o_impar(numero)
print("el numero", numero, "es", resultado)
