# Ejercicio 1.4 - Validador de contraseña con criterios específicos

print("Criterios de contraseña segura:")
print("• Mínimo 8 caracteres")
print("• Al menos 1 letra mayúscula")
print("• Al menos 1 número")
print("• Al menos 1 carácter especial (!@#$%^&*)")

contrasena = input("\nIngresa tu contraseña: ")

# Contadores y banderas
longitud_ok = len(contrasena) >= 8
tiene_mayus = False
tiene_numero = False
tiene_especial = False

caracteres_especiales = "!@#$%^&*"

for caracter in contrasena:
    if caracter.isupper():
        tiene_mayus = True
    if caracter.isdigit():
        tiene_numero = True
    if caracter in caracteres_especiales:
        tiene_especial = True

# Evaluamos resultados
errores = []
if not longitud_ok:
    errores.append("Debe tener al menos 8 caracteres")
if not tiene_mayus:
    errores.append("Falta al menos una letra mayúscula")
if not tiene_numero:
    errores.append("Falta al menos un número")
if not tiene_especial:
    errores.append("Falta al menos un carácter especial (!@#$%^&*)")

# Mostramos resultado
if not errores:
    print("\n ¡Contraseña segura y válida!")
else:
    print("\n La contraseña NO cumple con todos los criterios:")
    for error in errores:
        print("   •", error)