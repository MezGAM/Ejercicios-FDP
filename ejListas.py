#elabora una lista de numeros (7 numeros en la lista) y modificar dos elementos de esta lista
pares = [2, 4, 6, 8, 10, 12, 14]
print(pares)
pares [4] = 7
pares [2] = 3
print(pares)
#elabora una lista de frutas de tu gusto y que el usuario pueda cambiar una de las frutas las cual es de y
#que se guarde en la lista nueva
frutas = ['manzana', 'sandia', 'naranja', 'uva', 'tomate', 'aguacate', 'pera']
num = int(input('que fruta quieres cambiar?(el conteo empieza de 0 hasta el 6): '))
frutas [num] = input('por cual lo cambiarias?: ')

#realiza una lista que contenga elementos de diferentes tipos (numeros flotantes, cadenas, y un valor boleano ) 
# y con un for pueda mostrar lo que contiene 
lista = [55, 3.1416, 'gato',True]
for elemento in lista:
    print(f'el elemento es {elemento}' )
