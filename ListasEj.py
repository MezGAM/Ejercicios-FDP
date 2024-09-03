#dada unalista de palabras, cuenta cuantas veces aparece la palabra 'python' en la lista
palabras = ['python', 'java', 'c++ ', 'python', 'javascript', 'python', 'c#']
print(*palabras)
print(f'la palabra "python" aparece {palabras.count('python')} veces')



#dada una lista de cadenas de  texto, convierte todas las cadenas a mayusculas sin usar metodos como upper().
frases = ['hola', 'mundo', 'python', 'es', 'genial']
frasesMayus = []

for palabra in frases:
    palabraMayus = ''
    for letra in palabra:
        if 'a' <= letra <= 'z':
            palabraMayus += chr(ord(letra) - 32)
        else:
            palabraMayus += letra
    frasesMayus.append(palabraMayus)

print(frasesMayus)


#dada una lista de palabras elimina aquellas palabras que tengan menos de 4 caracteres.
palabras = ['sol', 'luna', 'cielo', 'mar', 'estrella','pez']
print(*palabras)
for palabra in palabras[:]:
    if len(palabra) < 4:
        palabras.remove(palabra)

print(*palabras)



#dada una lista de numeros encuetra el numero maximo sin usar la funcion max().
numeros = [15, 22, 8, 34, 9, 6, 17]
print(*numeros)
max = numeros[0]
for num in numeros:
    if num > max:
        max = num
print(f'el numero maximo en la lista es {max}')



#dada una lista de numeros enteros, cuenta cuantos numeros son positivos
numeros = [-3, 5, -7, 2, -8, 10, -4, 6]
contarPosi = 0

for num in numeros:
    if num > 0:
        contarPosi += 1

print(f'la cantidad de numeros positivos es: {contarPosi}')



#dada uan lista, invierte el orden de los elementos sin usar metodos como reverse().
numeros = [1, 2, 3, 4, 5]
print(*numeros)
numeros.sort(reverse=True)
print(*numeros)
#otra forma
numeros = [1, 2, 3, 4, 5]
print(*numeros)

numInvertido = []

for elemento in numeros:
    numInvertido.insert(0, elemento)
print(*numInvertido)


#dada una lista de numeros encuentra y muestra la media de los elementos de la lista
numeros = [4, 7, 2, 9, 3, 8, 5]
print(*numeros)
promedio = sum(numeros) / len(numeros)
print(f'el promedio de la lista es {promedio}')