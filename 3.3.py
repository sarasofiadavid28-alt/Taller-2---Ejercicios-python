# Ejercicio 3.3 - Búsqueda lineal en lista de nombres

nombres = [
    "Ana", "Bruno", "Carla", "Daniel", "Elena",
    "Fabio", "Gabriela", "Hugo", "Inés", "Javier"
]

buscado = input("Nombre a buscar: ").strip().title()

encontrado = False
posicion = -1

for i in range(len(nombres)):
    if nombres[i].lower() == buscado.lower():
        encontrado = True
        posicion = i
        break

print("\nResultado:")
if encontrado:
    print(f"✓ '{buscado}' encontrado en la posición {posicion} (índice {posicion})")
    print(f"  Nombre exacto en lista: {nombres[posicion]}")
else:
    print(f"✗ '{buscado}' NO se encuentra en la lista")