# Ejercicio 2.1 - Clasificación de edad por rangos

print("=== Clasificador de edades ===")

# Solicitamos la edad con validación básica
while True:
    try:
        edad = int(input("Ingresa tu edad: ").strip())
        if edad < 0:
            print("La edad no puede ser negativa.")
            continue
        break
    except ValueError:
        print("Ingresa un número válido.")

# Clasificación con if-elif
if 0 <= edad <= 12:
    categoria = "niño"
elif 13 <= edad <= 17:
    categoria = "adolescente"
elif 18 <= edad <= 64:
    categoria = "adulto"
else:  # 65 o más
    categoria = "adulto mayor"

print(f"\nCon {edad} años eres clasificado como: **{categoria.upper()}**")