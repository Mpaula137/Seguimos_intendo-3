def matrizMagica(matriz): 
    sumaFila = sum(matriz[0]) #comprobacion n1, sumar la primera fila 
    n = len(matriz)

    for i in range(1, n):
        if sum(matriz[i]) != sumaFila:
            return False #comprobacion n1, sumar la primera fila

    for j in range(n): 
        sumaColumna = 0
        for i in range(n):
            sumaColumna += matriz[i][j]
        if sumaColumna != sumaFila: # comprobacion n2, la suma de las columnas respecto a la suma de la fila
            return False

    sumaDiagonal = 0
    for i in range(n):
        sumaDiagonal += matriz[i][i]
    if sumaDiagonal != sumaFila: # comprobacion n3, la suma de la diagonal respecto a las sumas anteriores
        return False

    sumaDiagonalDos = 0
    for i in range(n):
        sumaDiagonalDos += matriz[i][n-1-i]
    if sumaDiagonalDos != sumaFila: #comprobacion n4, la suma de la segunda diagnonal respecto a las sumas anteriores
        return False 

    return True # Si todas las sumas son iguales, tenemos nuestra matriz magica

matriz = []
filas = 3
columnas = 3

for i in range(filas): # Se solicitan los valores de cada celda de la matriz
    fila = []
    for j in range(columnas):
        valor = int(input("digite los elementos ({},{}) de la matriz: ".format(i, j)))
        fila.append(valor)
    matriz.append(fila)

print(matriz)

if matrizMagica(matriz): # Se llama la funcion para evaluar las variables
    print("La matriz es magica")
else:
    print("La matriz no es magica")
