calificaciones = {
    "matematicas": 85,
    "fisica": 90,
    "historia": 78
}

promedio = sum(calificaciones.values()) / len(calificaciones)
print(f"El promedio es: {promedio:.2f}")