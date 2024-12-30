import math # Importar modulo matemático

def area_circulo(radio):
    return math.pi * (radio ** 2)

radio = float(input("Introduce el radio del circulo: "))

print(f"El area es: {area_circulo(radio):.2f}")
