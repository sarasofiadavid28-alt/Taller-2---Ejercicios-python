lista_compras = []

while True:
    print("\n1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el producto a agregar: ")
        lista_compras.append(producto)  # agrega el producto al final de la lista

    elif opcion == "2":
        producto = input("Ingrese el producto a eliminar: ")

        if producto in lista_compras:  # verifica que el producto exista en la lista
            lista_compras.remove(producto)  # elimina la primera coincidencia
            print("Producto eliminado")
        else:
            print("El producto no está en la lista")

    elif opcion == "3":
        print("\nLista de compras:")

        if len(lista_compras) == 0:
            print("La lista está vacía")
        else:
            for producto in lista_compras:  # recorre cada elemento de la lista
                print("-", producto)

    elif opcion == "4":
        break

    else:
        print("Opción inválida")