# Ejercicio 3.4 - Generador de tablas de multiplicar con bucle

while True:
    try:
        numero = int(input("\n¿De qué número quieres la tabla? (0 para salir): "))
        if numero == 0:
            print("¡Hasta luego!")
            break
        if numero < 0:
            print("Usaré el valor absoluto.")
            numero = abs(numero)
    except ValueError:
        print("Ingresa un número entero.")
        continue

    print(f"\nTabla del {numero}:")
    print("─"*30)
    for i in range(1, 11):
        print(f"{numero:2} × {i:2} = {numero * i:4}")
    print("─"*30)

    # Pregunta de continuación (variante más amigable)
    while True:
        resp = input("¿Otra tabla? (s/n): ").strip().lower()
        if resp in ["s", "n", ""]:
            break
        print("Responde s o n por favor.")
    if resp == "n":
        print("¡Gracias por usar el programa!")
        break