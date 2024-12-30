estudiante = {
    "nombre": input("Nombre: "),
    "edad": int(input("Edad: ")),
    "curso": input("Curso: "),
    "calificaciones": {
        "asignatura": [],
    }
}

condicion = True
while condicion:
    entrada = input("Introduzca la asignatura y calificacion: [! para terminar]: ")
    if entrada == "!":
        condicion = False
        break
    else:
        asignatura, calificacion = entrada.split(" ")
        estudiante["calificaciones"]["asignatura"].append((asignatura, float(calificacion)))


        
asignaturas = ""
suma_de_notas = 0
cantidad_de_numeros = 0
for lista in estudiante["calificaciones"]["asignatura"]:
    asignaturas += f"{lista[0]} - {lista[1]}\n"
    suma_de_notas += lista[1]
    cantidad_de_numeros += 1

promedio = suma_de_notas / cantidad_de_numeros

descripcion = f"""
Estudiante
 {estudiante['nombre']}
 {estudiante['edad']}
 {estudiante['curso']}\n
Asignaturas
 {asignaturas}
Promedio
 {promedio:.2f}
"""

print(descripcion)