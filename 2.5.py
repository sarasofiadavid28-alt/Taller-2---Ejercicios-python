# Ejercicio 2.5 - Calculadora de descuentos según categoría

print("=== Calculador de descuentos por categoría ===")
print("Categorías disponibles: A (20%), B (15%), C (10%)")

categoria = input("\nIngresa tu categoría (A/B/C): ").strip().upper()
monto = None

# Validación del monto
while monto is None:
    try:
        monto = float(input("Ingresa el monto de la compra: ").strip())
        if monto < 0:
            print("El monto no puede ser negativo.")
            monto = None
    except ValueError:
        print("Ingresa un valor numérico válido.")

# Determinación del porcentaje de descuento
if categoria == "A":
    descuento_porcentaje = 20
elif categoria == "B":
    descuento_porcentaje = 15
elif categoria == "C":
    descuento_porcentaje = 10
else:
    descuento_porcentaje = 0
    print(f" Categoría '{categoria}' no reconocida → sin descuento")

# Cálculos
descuento = monto * (descuento_porcentaje / 100)
total_pagar = monto - descuento

# Resultado
print("\n" + "-"*50)
print(f"Monto original:       ${monto:,.2f}")
if descuento_porcentaje > 0:
    print(f"Descuento ({descuento_porcentaje}%):   -${descuento:,.2f}")
print(f"Total a pagar:         ${total_pagar:,.2f}")
print("-"*50)