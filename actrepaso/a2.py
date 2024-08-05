import math

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio = float(input("Ingrese el radio del circulo: "))
print("el area del circulo es: ", area_circulo(radio))
