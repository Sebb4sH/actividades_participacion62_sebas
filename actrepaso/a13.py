def calcular_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "no se puede dividir por cero"
    
    return suma, resta, multiplicacion, division

try:
    numero1 = float(input("ingresa el primer numero: "))
    numero2 = float(input("ingresa el segundo numero: "))
    
    suma, resta, multiplicacion, division = calcular_operaciones(numero1, numero2)
    
    print(f"Suma: {numero1} + {numero2} = {suma}")
    print(f"Resta: {numero1} - {numero2} = {resta}")
    print(f"Multiplicacion: {numero1} * {numero2} = {multiplicacion}")
    print(f"Division: {numero1} / {numero2} = {division}")
except ValueError:
    print("Por favor ingresa valores numericos validos.")
