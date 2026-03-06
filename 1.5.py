# Ejercicio 1.5 - Convertidor de unidades con menú interactivo

while True:
    print("\n" + "="*40)
    print("     CONVERTIDOR DE UNIDADES")
    print("="*40)
    print("1. Celsius → Fahrenheit")
    print("2. Kilómetros → Millas")
    print("3. Kilogramos → Libras")
    print("4. Salir")
    print("-"*40)

    opcion = input("Elige una opción (1-4): ").strip()

    if opcion == "4":
        print("¡Gracias por usar el convertidor!")
        break

    if opcion not in ["1", "2", "3"]:
        print("Opción no válida. Elige 1, 2, 3 o 4.")
        continue

    try:
        valor = float(input("Ingresa el valor a convertir: "))

        if opcion == "1":
            # Celsius a Fahrenheit: F = C * 9/5 + 32
            resultado = valor * 9/5 + 32
            print(f"{valor:.2f} °C → {resultado:.2f} °F")

        elif opcion == "2":
            # km a millas: 1 km = 0.621371 millas
            resultado = valor * 0.621371
            print(f"{valor:.2f} km → {resultado:.2f} millas")

        elif opcion == "3":
            # kg a libras: 1 kg = 2.20462 lb
            resultado = valor * 2.20462
            print(f"{valor:.2f} kg → {resultado:.2f} lb")

    except ValueError:
        print("Debes ingresar un número válido.")