# Ejercicio 2.4 - Conversor de nota numérica a letra

print("=== Conversor de calificaciones (0-100) ===")

while True:
    try:
        nota = float(input("Ingresa la calificación (0-100): ").strip())
        
        if 0 <= nota <= 100:
            break
        else:
            print("La nota debe estar entre 0 y 100.")
            
    except ValueError:
        print("Ingresa un número válido.")

# Determinación de letra
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"

print(f"\nCalificación: {nota} → Letra: **{letra}**")