# Ejercicio 3.1 - Mostrar números pares desde 1 hasta N con for

while True:
    try:
        n = int(input("Ingresa un número entero positivo N: "))
        if n <= 0:
            print("El número debe ser positivo.")
            continue
        break
    except ValueError:
        print("Por favor ingresa un número entero válido.")

print(f"\nNúmeros pares desde 1 hasta {n}:")

# Opción 1: más clara para principiantes
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end="  ")

print("\n")

# Opción 2: más eficiente (solo recorre los pares)
# for i in range(2, n + 1, 2):
#     print(i, end="  ")