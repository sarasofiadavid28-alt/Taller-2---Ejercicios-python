# Ejercicio 2.3 - Calculadora con menú repetitivo

while True:
    print("\n" + "="*40)
    print("       CALCULADORA BÁSICA")
    print("="*40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("-"*40)

    opcion = input("Elige una opción (1-5): ").strip()

    if opcion == "5":
        print("¡Gracias por usar la calculadora!")
        break

    if opcion not in ["1","2","3","4"]:
        print("Opción inválida. Elige entre 1 y 5.")
        continue

    try:
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))

        if opcion == "1":
            print(f"{n1} + {n2} = {n1 + n2}")

        elif opcion == "2":
            print(f"{n1} - {n2} = {n1 - n2}")

        elif opcion == "3":
            print(f"{n1} × {n2} = {n1 * n2}")

        elif opcion == "4":
            if n2 == 0:
                print("Error: No se puede dividir entre 0")
            else:
                print(f"{n1} ÷ {n2} = {n1 / n2:.4f}")

    except ValueError:
        print("Debes ingresar números válidos.")