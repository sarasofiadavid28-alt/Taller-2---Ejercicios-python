inventario = [
    {"nombre": "teclado", "precio": 80, "stock": 10},
    {"nombre": "mouse", "precio": 40, "stock": 15}
]

producto_buscar = input("Ingrese el nombre del producto: ")

encontrado = False

for producto in inventario:  # recorre cada diccionario dentro de la lista

    if producto["nombre"] == producto_buscar:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))

        producto["precio"] = nuevo_precio  # actualiza el valor de la clave precio
        encontrado = True

        print("Precio actualizado")

if not encontrado:
    print("Producto no encontrado")

print("\nInventario actual:")

for producto in inventario:
    print(producto)