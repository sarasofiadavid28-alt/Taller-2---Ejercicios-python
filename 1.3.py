# Ejercicio 1.3 - Validación básica de correo electrónico

correo = input("Ingresa tu correo electrónico: ").strip()

# Criterios básicos de validación
errores = []

if "@" not in correo:
    errores.append("Falta el símbolo @")

if "." not in correo:
    errores.append("Falta el punto (.)")

# Contamos que haya al menos un @ y un . después del @
if correo.count("@") != 1:
    errores.append("Debe haber exactamente un @")

# Buscamos si hay punto después del @
if "@" in correo:
    parte_despues_arroba = correo.split("@")[1]
    if "." not in parte_despues_arroba:
        errores.append("Debe haber al menos un punto después del @")

# Verificamos que no empiece ni termine con . o @
if correo.startswith(("@", ".")) or correo.endswith(("@", ".")):
    errores.append("El correo no puede empezar ni terminar con @ o .")

# Resultado final
if not errores:
    print("El correo parece válido:", correo)
else:
    print("El correo tiene los siguientes problemas:")
    for error in errores:
        print("   •", error)