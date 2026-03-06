# Ejercicio 1.1 - Registro de usuario simple con validación de edad

# Solicitamos los datos al usuario
nombre = input("Ingresa tu nombre: ").strip()

# Validamos que la edad sea un número positivo
while True:
    try:
        edad_texto = input("Ingresa tu edad: ").strip()
        edad = int(edad_texto)
        
        if edad <= 0:
            print(" La edad debe ser un número positivo mayor que cero.")
            continue
            
        break  # Salimos del bucle si todo está correcto
        
    except ValueError:
        print(" Por favor ingresa solo números para la edad.")

ciudad = input("Ingresa tu ciudad de residencia: ").strip()

# Mostramos el mensaje personalizado
print("\n" + "="*50)
print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")
print("="*50)