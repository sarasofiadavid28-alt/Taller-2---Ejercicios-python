lista1 = input("Ingrese la primera lista (separada por comas): ").split(",")
lista2 = input("Ingrese la segunda lista (separada por comas): ").split(",")

comunes = []
unicos1 = []
unicos2 = []

# revisa cada elemento de la primera lista
for elemento in lista1:

    if elemento in lista2:
        comunes.append(elemento)  # elemento presente en ambas listas
    else:
        unicos1.append(elemento)  # solo existe en la primera lista

# revisa cada elemento de la segunda lista
for elemento in lista2:

    if elemento not in lista1:
        unicos2.append(elemento)  # solo existe en la segunda lista

print("\nElementos comunes:", comunes)
print("Únicos de la primera lista:", unicos1)
print("Únicos de la segunda lista:", unicos2)