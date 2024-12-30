"""
Las listas son colecciones ordenadas de elementos. 
Son mutables, lo que significa que puedes modificarlas.
"""

# Crear lista

frutas = ["manzana", "pera", "piña", "banana"]
print(frutas)

# Acceder a elementos

print(frutas[0]) # Accede al primer elemento de la lista
print(frutas[2])

# Agregar o eliminar elementos

frutas.append("naranja") # Agrega al final
print(frutas)

frutas.remove("banana") # Elimina un elemento
print(frutas)

# Iterar sobre listas

for fruta in frutas:
    print(fruta)