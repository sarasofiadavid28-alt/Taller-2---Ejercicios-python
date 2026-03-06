# Ejercicio 1.2 - Calculadora básica con validación de división por cero

print("=== Calculadora básica ===")
print("Operaciones disponibles: +  -  *  /")

# Solicitamos los datos
try:
    num1 = float(input("Primer número: "))
    operacion = input("Operación (+, -, *, /): ").strip()
    num2 = float(input("Segundo número: "))

    # Procesamos según la operación elegida
    if operacion == "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    elif operacion == "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    elif operacion == "*":
        resultado = num1 * num2
        print(f"{num1} × {num2} = {resultado}")

    elif operacion == "/":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"{num1} ÷ {num2} = {resultado:.4f}")

    else:
        print("Operación no válida. Usa +, -, * o /")

except ValueError:
    print("Error: Debes ingresar números válidos.")