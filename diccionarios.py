"""
Los diccionarios almacenan pares de clave:valor.
Son ideales para representar datos estructurados.
"""

# Crear un diccionario
persona = {
    "nombre": "Gabriel",
    "edad": 22,
    "ciudad": "Valle Gran Rey"
}

print(persona["nombre"])

# Agregar o modificar datos

persona["ocupacion"] = "ingeniero" # Agregar
persona["edad"] = 21 # Modificar

print(persona)

# Recorrer diccionario

for clave, valor in persona.items():
    print(f"{clave}: {valor}")