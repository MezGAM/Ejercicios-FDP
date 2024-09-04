#saludo personalizado
def saludar(nombre):
   return print(f'bienvenido {nombre}, esto es python')

nombre = str(input('ingresa tu nombre: '))
saludar(nombre)

#Area de un circulo 
def area_circulo(radio):
   return 3.1416 * (radio **2)
radio = int(input('ingresa el radio del circulo: '))
area = area_circulo(radio)
print(f'el area del circulo es {area}')


#milla a kilometro
def millas_a_kilometros(milla):
   return milla * 1.60934
milla = int(input('ingresa las millas: '))
resultado = millas_a_kilometros(milla)
print(f'{milla} millas es igual a {resultado} kilometros')

#repetir texto
def repetir_texto(texto, veces):
    return texto * veces

texto = input('ingresa el texto: ')
veces = int(input('ingresa el numero de veces a repetir: '))

resultado = repetir_texto(texto, veces)
print(resultado)

#multiplicacion simple
def multiplicar(a, b):
   return a * b

a, b = [int(input(f'ingresa el {num} numero : ')) for num in ('primer', 'segundo')]

resultado = multiplicar(a, b)

print(f'el resultado es {resultado}')

#mayusculas y minusculas
def cambiar_caso(texto):
    resultado = ''
    for letra in texto:
        if letra.isupper():
            resultado += letra.lower()
        elif letra.islower():
            resultado += letra.upper()
        else:
            resultado += letra
    return resultado

texto = input('ingresa un texto: ')
resultado = cambiar_caso(texto)
print('texto cambiado: ', resultado)

#perimetro de un rectangulo
def perimetro_rectangulo(largo, ancho):
    return 2 * (largo + ancho)
largo, ancho = [int(input(f'ingresa el {lado} del rectangulo: ')) for lado in ('largo', 'ancho')]
print(f'el area del rectangulo es {perimetro_rectangulo(largo, ancho)}')

#programa temperatura
def calcular_temperatura_media(temp_max, temp_min):
    return (temp_max + temp_min) / 2

def programa_principal():
    num_dias = int(input('cuantos dias son?: '))
    
    for dia in range(1, num_dias + 1):
        print(f"\ndia {dia}:")
        temp_max, temp_min = [int(input(f'ingresa la temperatura {MinMax}')) for MinMax in ('minima', 'maxima')]
        media = calcular_temperatura_media(temp_max, temp_min)
        print(f'la temperatura media del día {dia} es: {media}°C')

programa_principal()
