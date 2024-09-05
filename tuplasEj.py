#Escribe una función que reciba tres números enteros como parámetros y devuelva una tupla con esos tres números. 
def crear_tupla(a, b, c):
    return a, b, c
futura_tupla = input('ingresa 3 numeros separados por comas: ')
num = tuple(map(int, futura_tupla.split(',')))

tupla = crear_tupla(*num)
print(f'esta es tu tupla {tupla}')

#Dada la siguiente tupla: numeros = (10, 20, 30, 40, 50), accede al tercer elemento e imprímelo.
numeros = (10, 20, 30, 40, 50)
print(numeros[2])

#Dada la siguiente tupla anidada: tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9)), accede al número 5 y muéstralo por pantalla.
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
num = tupla_anidada[1][1]
print(num)

#Define dos tuplas, una con los primeros 5 números pares y otra con los primeros 5 números impares.
#Luego, concaténalas y muestra el resultado.
tupla_par = (2, 4, 6, 8, 10)
tupla_impar = (1, 3, 5, 7, 9)
tupla_concatenada = tupla_par + tupla_impar
print(tupla_concatenada)

#Dada la tupla colores = ('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo'), 
# cuenta cuántas veces aparece el color "rojo" e imprime el resultado.
colores = ('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo')
print(colores)
rojo = colores.count('rojo')
print(f'la palabra rojo aparece {rojo} veces')


#Dada una lista de nombres: nombres = ['Ana', 'Juan', 'Pedro', 'Luis'], 
# convierte esta lista en una tupla y muestra la tupla resultante.
nombres = ['Ana', 'Juan', 'Pedro', 'Luis']
tupla_num = tuple(nombres)
print(tupla_num)

#Dada la tupla tupla_larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 
# crea una nueva tupla que contenga solo los primeros 5 elementos.
tupla_larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

nueva_tupla = tupla_larga[:5]
print(nueva_tupla)


#Escribe un programa que intercambie el valor de dos variables utilizando una tupla. 
# Por ejemplo, si a = 5 y b = 10, después del intercambio a debe ser 10 y b debe ser 5.
a, b = [int(input(f'ingresa {oa} numero: ')) for oa in ('un','otro')]
print({a}, {b})
a, b,= b, a
print({a}, {b})
