contactos = {}

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono: ")

        contactos[nombre] = telefono  # guarda el teléfono usando el nombre como clave

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")

        if nombre in contactos:  # verifica si la clave existe en el diccionario
            print("Teléfono:", contactos[nombre])
        else:
            print("Contacto no encontrado")

    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")

        if nombre in contactos:
            del contactos[nombre]  # elimina el par clave-valor
            print("Contacto eliminado")
        else:
            print("El contacto no existe")

    elif opcion == "4":
        break

    else:
        print("Opción inválida")