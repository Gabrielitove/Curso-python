# ---------------- Funcion simple

def saludar():
    print("¡Hola!")
    
saludar() # Salida: ¡Hola!

# ---------------- Funcion con parametros

def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Gabriel")
saludar("Yadira")

# ---------------- Funcion que retorna valores

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")

# ---------------- Parametros por defecto

def saludar(nombre="invitado"):
    print(f"¡Hola, {nombre}!")

saludar()
saludar("Gabriel")


