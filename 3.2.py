# Ejercicio 3.2 - Suma acumulativa hasta ingresar 0

print("Introduce números (0 para terminar)")

total = 0
contador = 0

while True:
    try:
        numero = float(input("→ Número: "))
    except ValueError:
        print("  Valor no válido, se ignora.")
        continue

    if numero == 0:
        break

    total += numero
    contador += 1

print("\n" + "─"*40)
if contador == 0:
    print("No se ingresaron números.")
else:
    print(f"Números ingresados: {contador}")
    print(f"Suma total.........: {total}")
    print(f"Promedio...........: {total/contador:.2f}" if contador > 0 else "")
print("─"*40)