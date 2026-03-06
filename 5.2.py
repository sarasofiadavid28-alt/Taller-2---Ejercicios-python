def calcular_promedio(lista):

    # verifica que la lista tenga elementos
    if len(lista) == 0:
        return "La lista está vacía"

    suma = sum(lista)  # suma todos los números
    promedio = suma / len(lista)

    return promedio


numeros = [5, 8, 10, 7]

resultado = calcular_promedio(numeros)

print("Promedio:", resultado)