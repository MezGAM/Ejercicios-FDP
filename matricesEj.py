#Escribe un programa que tome dos matrices de igual tamaño (matrices bidimensionales) y devuelva una nueva matriz 
#que sea la suma de las dos matrices originales.
matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

matrix2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

matrixNueva = []
for i in range(len(matrix1)):
    filaSuma = []
    for j in range(len(matrix1[i])):

        suma = matrix1[i][j] + matrix2[i][j]
        filaSuma.append(suma)
    matrixNueva.append(filaSuma)

for fila in matrixNueva:
    print(fila)
    
    
#Crea un programa que multiplique dos matrices de tamaño adecuado. Recuerda que para multiplicar matrices,
# el número de columnas de la primera debe coincidir con el número de filas de la segunda

matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


matrix2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

matrixNueva = []
for i in range(len(matrix1)):
    filaMult = []

    for j in range(len(matrix1[i])):
        mult = matrix1[i][j] * matrix2[i][j]
        filaMult.append(mult)

    matrixNueva.append(filaMult)

for fila in matrixNueva:
    print(fila)


#Escribe un programa que tome una matriz y devuelva su transpuesta (intercambiar filas por columnas)
import numpy as np 
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matriz_transpuesta = np.transpose(matrix)
print(*matriz_transpuesta)


#Un cuadrado mágico es una matriz en la que la suma de cada fila, columna y diagonal es la misma. Escribe
#un programa que determine si una matriz dada es un cuadrado mágico