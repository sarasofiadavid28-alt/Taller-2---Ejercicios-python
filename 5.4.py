import string

def es_palindromo(texto):

    texto = texto.lower()  # convierte todo a minúsculas

    # elimina espacios y signos de puntuación
    for caracter in string.punctuation + " ":
        texto = texto.replace(caracter, "")

    texto_invertido = texto[::-1]  # invierte la cadena

    # compara el texto original limpio con el invertido
    return texto == texto_invertido


frase = input("Ingrese un texto: ")

if es_palindromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")