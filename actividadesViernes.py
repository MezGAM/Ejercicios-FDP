#Objetivo: Crear un programa que permita registrar alumnos y sus calificaciones,
# calculando el promedio de cada uno.
alumnos = []
def agrega_alumno():
    nombre = input('ingresa el nombre del alumno (escribe "salir" para terminar): ')  
    calificaciones = []

    for materia in ['espanol','matematicas','ciencias naturales','fundamentos de programacion']:
        calificacion = float(input(f'ingresa la calificacion de {materia} de {nombre}: '))
        calificaciones.append(calificacion)
        
    promedio = sum(calificaciones) / len(calificaciones)
    alumnos.append((nombre, calificaciones, promedio))

def mostrar_alumnos():
    print('alumnos y sus promedios')
    for alumno in alumnos:
        nombre, calificaciones, promedio = alumno
        print(f'alumno: {nombre}, promedio: {promedio:.1f}')

def mostrar_mayor_alumnos(promedio_limite):
    print(f'alumnos con promedio mayor o igual a {promedio_limite}')
    for alumno in alumnos:
        nombre, calificaciones, promedio = alumno
        if promedio >= promedio_limite:
            print(f'alumno: {nombre}, promedio: {promedio:.1f}')

def mostrar_menor_alumnos(promedio_limite):
    print(f'alumnos con promedio menor a {promedio_limite}')
    for alumno in alumnos:
        nombre, calificaciones, promedio = alumno
    if promedio < promedio_limite:
        print(f'alumno: {nombre}, promedio: {promedio:.1f}')

def main():
    while True:
        print('registro de alumnos')
        print('1. agrega un alumno y calificaciones')
        print('2. Mostrar todos los alumnos y sus promedios')
        print('3. Mostrar alumnos con promedio mayor o igual a un valor')
        print('4. Mostrar alumnos con promedio menor a un valor')
        
        opcion = input('selecciona una opcion: ')
        
        if opcion == "1":
            agrega_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            promedio_limite = float(input('ingresa el promedio minimo: '))
            mostrar_mayor_alumnos(promedio_limite)
        elif opcion == "4":
            promedio_limite = float(input('ingresa el promedio maximo: '))
            mostrar_menor_alumnos(promedio_limite)
        else:
            print('Opción no valida. intenta de nuevo :p')
main()

#Objetivo: Crear un juego en el que el usuario adivine un número dentro de un rango, utilizando ciclos while 
#y listas para gestionar las pistas.
import random

def juego_adivinanza():
    num = random.randint(1, 100)
    intentos_restantes = 10
    pistas = []

    print('bienvenido al juego')
    print('debes adivinar un número entre 1 y 100, tienes 5 intentos.')
    
    while intentos_restantes > 0:
        intento = int(input('adivina el numero: '))
        intentos_restantes -= 1

        if intento == num:
            print(f'lo lograste! adivinaste el numero: {num}')
            break
        elif intento < num:
            pista = 'el numero es mas alto'
        else:
            pista = 'el numero es mas bajo'

        diferencia = abs(num - intento)
        if diferencia <= 10:
            pista += 'estas cerca'
        
        pistas.append(pista)
        print(pista)
        print(f'te quedan {intentos_restantes} intentos.')
    
    if intentos_restantes == 0 and intento != num:
        print(f'ijole, perdiste, el numero era: {num}')

    print('resumen de tus pistas:')
    for i, pista in enumerate(pistas, 1):
        print(f'pista {i}: {pista}')

juego_adivinanza()



inventario = []

def agregar_producto():
    nombre = input('ingresa el nombre del producto: ')
    cantidad = int(input(f'ingresa la cantidad de {nombre}: '))
    precio = float(input(f'ingresa el precio de {nombre}: '))
    inventario.append([nombre, cantidad, precio])
    print(f'{nombre} agregado al inventario :3')

def actualizar_cantidad():
    nombre = input('ingresa el nombre del producto a actualizar: ')
    for producto in inventario:
        if producto[0] == nombre:
            nueva_cantidad = int(input(f'ingrese la nueva cantidad de {nombre}: '))
            producto[1] = nueva_cantidad
            print(f'la cantidad de {nombre} se ha actualizado a {nueva_cantidad} c:')
            if nueva_cantidad == 0:
                eliminar_producto(nombre)  # Eliminar producto si la cantidad es cero
            return
    print("producto no encontrado en el inventario :p")
def mostrar_inventario():
    if len(inventario) == 0:
        print('el inventario esta vacio :o')
    else:
        print('\ninventario:')
        for producto in inventario:
            nombre, cantidad, precio = producto
            print(f'producto: {nombre}, cantidad: {cantidad}, precio: {precio:.2f}')
        calcular_valor_total()


def calcular_valor_total():
    valor_total = sum(producto[1] * producto[2] for producto in inventario)
    print(f'\nel valor total del inventario es: ${valor_total:.2f}\n')
 
def eliminar_producto(nombre):
    global inventario
    inventario = [producto for producto in inventario if producto[0] != nombre]
    print(f'{nombre} ha sido eliminado del inventario :D')

def main():
    while True:
        print('\ngestion de inventario')
        print('1. agregar producto')
        print('2. actualizar cantidad de un producto')
        print('3. mostrar inventario')
        print('4. salir')

        opcion = input('selecciona una opcion: ')

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            actualizar_cantidad()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print('saliendo del programa... :s')
            break
        else:
            print('ppcion no valida, intenta de nuevo')

main()
