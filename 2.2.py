# Ejercicio 2.2 - Menú interactivo simple con if-elif

while True:
    print("\n" + "-"*35)
    print("         MENÚ PRINCIPAL")
    print("-"*35)
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    print("-"*35)

    opcion = input("Elige una opción (1-3): ").strip()

    if opcion == "1":
        nombre = input("¿Cómo te llamas? ").strip()
        print(f"¡Hola, {nombre}! Qué gusto verte hoy ")

    elif opcion == "2":
        print("¡Hasta pronto! Cuídate mucho ")

    elif opcion == "3":
        print("Gracias por usar el programa. ¡Nos vemos!")
        break

    else:
        print("Opción no válida. Por favor elige 1, 2 o 3.")