numeros = [] #creamos una lista 
for i in range(5):  # Se crea un ciclo for que se ejecutará 5 veces
    numero = float(input("Ingrese el número {}: ".format(i+1))) #Se solicita al usuario ingresar un número por teclado y se almacena en la variable "numero"
    numeros.append(numero) # se agrega a la lista

promedio = sum(numeros) / len(numeros) # Se calcula el promedio de los números en la lista "numeros"

numeros_ordenados = sorted(numeros)# Se ordena la lista "numeros" en orden ascendente y se almacena en la variable "numeros_ordenados"
mediana = numeros_ordenados[len(numeros_ordenados)//2]# Se calcula la mediana de los números en la lista "numeros_ordenados" y se almacena en la variable "mediana"


producto = 1# Se inicializa la variable "producto" en 1
for numero in numeros:# Se crea un ciclo for que recorre los números en la lista "numeros"
    producto *= numero# Se multiplica cada número en la lista "numeros" con la variable "producto"
promedio_multiplicativo = producto ** (1/len(numeros))# Se calcula el promedio multiplicativo de los números en la lista

numeros_ascendente = sorted(numeros)#ordena la lista "numeros" en orden ascendente

numeros_descendente = sorted(numeros, reverse=True) # Se ordena la lista "numeros" en orden descendente

mayor = max(numeros)# Se obtiene el valor máximo de la lista "numeros"
menor = min(numeros) # Se obtiene el valor mínimo de la lista "numeros"
potencia = mayor ** menor # Se calcula la potencia

menor_cubico = min(numeros) ** (1/3)# Se calcula la raíz cúbica del valor mínimo de la lista "numeros" y se almacena en la variable "menor_cubico"

print("Promedio: ", promedio)
print("Mediana: ", mediana)
print("Promedio multiplicativo: ", promedio_multiplicativo)
print("Números en orden ascendente: ", numeros_ascendente)
print("Números en orden descendente: ", numeros_descendente)
print("Potencia del mayor número elevado al menor número: ", potencia)
print("Raíz cúbica del menor número: ", menor_cubico)