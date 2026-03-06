# Ejercicio 3.5 - Eliminar duplicados sin usar conjuntos (método de lista auxiliar)

numeros = []
print("Ingresa 10 números (pueden repetirse)\n")

for i in range(1, 11):
    while True:
        try:
            n = float(input(f"{i:2}. → "))
            numeros.append(n)
            break
        except ValueError:
            print("  Ingresa un número válido.")

# Eliminación de duplicados manteniendo el orden original
sin_duplicados = []

for num in numeros:
    # Solo agregamos si NO está ya en la lista resultado
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("\n" + "═"*50)
print("Original con posibles duplicados:")
print(numeros)
print("\nSin duplicados (manteniendo orden de aparición):")
print(sin_duplicados)
print(f"Cantidad original : {len(numeros)}")
print(f"Cantidad única    : {len(sin_duplicados)}")
print("═"*50)