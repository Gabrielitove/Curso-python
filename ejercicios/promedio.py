numeros = []
condicional = True
while condicional:
    
    numero = input("Introduce un numero para la lista: [! para terminar]: ")
    if numero == "!":
        condicional = False
        break
    else:
        numeros.append(int(numero))

    

print(sum(numeros))
print(len(numeros))

promedio = round(sum(numeros) / len(numeros), 2)


print(promedio)
