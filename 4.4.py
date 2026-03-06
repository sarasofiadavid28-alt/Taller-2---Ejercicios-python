entrada = input("Ingrese números separados por comas: ")

# divide el texto usando la coma como separador
numeros_texto = entrada.split(",")

numeros = []

for n in numeros_texto:
    numeros.append(float(n))  # convierte cada elemento a número decimal

maximo = max(numeros)  # valor más grande
minimo = min(numeros)  # valor más pequeño
suma = sum(numeros)    # suma total
promedio = suma / len(numeros)  # promedio

print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Suma:", suma)
print("Promedio:", promedio)