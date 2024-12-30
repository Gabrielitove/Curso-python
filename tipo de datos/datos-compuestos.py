# Creando una lista (Se puede modificar)
lista = ["Gabriel Velez", 22, 1.63, True, "Gabriel Velez"]

# Creando una tupla (No se puede modificar)
tupla = ("Gabriel Velez", 22, 1.63, True, "Gabriel Velez")

# Esto es valido
lista[3] = "Maquinola"

# Esto no es valido
#tupla[3] = "Maquinola"

# Creando un conjunto (set)
"""
Caracteristicas
- No se accede a elementos por su indice
- No almacena datos duplicados
"""

conjunto = {"Gabriel Velez", 22, 1.63, True, "Gabriel Velez"}

# Creando un diccionario (dict)
"""
La estructura es key : value y separamos con comas
"""

diccionario = {
    "nombre": "Gabriel Velez",
    "edad": 22,
    "altura": 1.63
}