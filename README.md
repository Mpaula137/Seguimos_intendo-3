# Seguimos_intento:3
Resolución del taller propuesto haciendo uso de bucles, vectores, listas, etc.
 ### Integrantes del grupo ###
 - Maria Paula Machuca Hortua
 - Aaron Alejandro Suarez Bonilla
 - Diego Alejandro Muñoz Penna
 ### Nombre del grupo Pythonbrokers. ###
 [![logo.jpg](https://i.postimg.cc/HL4kxVwv/logo.jpg)](https://postimg.cc/4Kyg24Fp)

## Punto 1:
- Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.
separarción de digitos en un numero:

```
numeros = [] # lista vacía
def separar(x):
    """
    Esta función separa los enteros de cualquier número n ingresado

    Argumentos:
    x: int = Número a separar

    Devuelve: los numeros que componen al numero x
    """
    while x > 0: # X tiene que ser una variable mayor a 0
        print(x%10) # Está expresión se utiliza para conseguir el último digito de x
        numeros.append(x % 10) # se le dice al programa que agregue a la lista numeros el ultimo dijito de x
        x = x // 10 # se le dice al ciclo que se actualice con la cifra mas cercana al último dijito
    print(numeros[:])
if __name__ == "__main__":  #Funcion principal
 n = int(input("Ingrese un numero por favor:"))
 separar(n) 
```
## Punto 2:
- Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de
la decimal.
```
numero= float(input("Ingrese un numero flotante: "))

parte_entera=int(numero)#ysamos la funcion int() para obtener la parte entera
parte_decimal= numero % 1 #Utilizamos el operador modulo para hallar la parte decimal

Digitosparte_entera=[]# lista vacia para almacenar los digitos enteros
Digitosparte_decimal=[]#lista vacia para almacenar los digitos decimales

while parte_entera >0: #Esto quiere decir que mientras haya digitos para tomar
    digito= parte_entera%10 #obtener el ultimo digito
    Digitosparte_entera.append(digito)# agregar el digito a la lista
    parte_entera //=10 #eliminar el ultimo digito de la parte entera
Digitosparte_entera.reverse()#ivertir el orden

while parte_decimal != 0: #MIentras haya digitos que tomar
    digito= int(parte_decimal*10)# Esto para obtener el primer digito, El int convierte al digito en entero para la lista
    Digitosparte_decimal.append(digito)#agregar el digito a la lista
    parte_decimal= round ((parte_decimal*10) % 1, 2)  # eliminar el primer dígito de la parte decimal, redondeando a 2 decimales, por eso usamos la funcion count

print("Esta es la parte entera", Digitosparte_entera)
print("Esta es la parte decimal", Digitosparte_decimal)
```
## Punto 3:
- Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
```
if __name__ == "__main__":  #Funcion principal
 Numero1= (input("Ingrese el primer numero:"))#Pedimos al usuario ingresar dos digitos
 Numero2= (input("Ingrese el segundo numero:"))

if len(Numero1) != len(Numero2): #Creamos una condicion que nos dice que si la longitud de el numero 1 y dos es distinta
    print("LOs digitos tienen diferente longitud:/")# se imprime que tiene diferente longitud se detiene el ciclo
else:
   if Numero1 == Numero2[::-1]: #Numero2[::-1] quiere decir que muestra el numero pero inverso
      print (str(Numero1), "y", str(Numero2), "son espejos entre sí.")
   else:
      print("No son numeros espejos:((")
```
## Punto 4:
- Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
```
f
```
## Punto 5:
- Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.
```
def mcm_iterativo(a, b):
    # Buscamos el máximo común divisor con ayuda de una funcion auxiliar 
    def mcd(a, b):#declaramos la variable
        while b != 0:#mientras b sea distinto a 0
            a, b = b, a % b# a,b es igual a b, juento al modulo de a con b
        return a
    
    # Calculamos el mínimo común múltiplo usando la fórmula: mcm(a,b) = (a*b)/mcd(a,b)
    return (a * b) // mcd(a, b)# devuelve minimo comun multiplo utilizando el mcd


def mcm_recursivo(a, b):
    # Función auxiliar para calcular el máximo común divisor de manera recursiva
    def mcd(a, b):#declaramos las variable para trabajar 
        if b == 0:#mientras b sea igual a 0
            return a#retornar a
        return mcd(b, a % b)# luego retornar a,b es igual a b, juento al modulo de a con b
    
    # Función auxiliar para calcular el mínimo común múltiplo de manera recursiva
    def mcm(a, b):#declaramos la funcion 
        return (a * b) // mcd(a, b)# retornamos el mcm gracias la relacion matematica que tiene con el mcd
    
    return mcm(a, b)
if __name__ == "__main__":  #Funcion principal
# Ejemplo de uso
 a = float(input("ingrese el primer numero:"))
 b = float(input("Ingrese el segundo numero:"))

# Iterativo
print("Este es el mcm iterativo de", a, "y", b, "es:", mcm_iterativo(a, b)) 

# Recursivo
print("Este es el mcm recursivo de", a, "y", b, "es:", mcm_recursivo(a, b)) 
```
## Punto 6:
- Desarrollar un programa que determine si en una lista no existen elementos repetidos.
```
def elementos_repetidos(lista): #Funcion para encontrar elementos repetidos
    longitud = len(lista) # usamos un len para saber la longitud de nuestra lista
    for i in range(longitud): #luego usamos un ciclo for para que recorra la longitud de la lista
        for j in range(i+1, longitud):# usamos otro for para compara el elemnto actual con los otros elementos
            if lista[i] == lista[j]:#compara los elementos
                return "La lista presentada contiene elementos repetidos"
    return "La lista presentada no contiene elementos repetidos"

if __name__ == "__main__":  #Funcion principal
   mi_lista = []
   n = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
   for i in range(n):
      elemento = input("Ingrese un elemento sin espacios: ")
      mi_lista.append(elemento)
print(mi_lista)
print(elementos_repetidos(mi_lista))

```
## Punto 7:
- Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'
```
def buscamos_vocales(lista:list) -> list:
    cAdEnAsDe_vocales = [] # se crea una lista para guradar las cadenas que tengan más de 2 vocales.
    for obj in lista:
        if type(obj) == str: # se chequea que el elemento se trate de un string.
            determinador = [char for char in obj if char in "AEIOUaeiou"] # se guardan las vocales del elemento x en una lista.
            if len(determinador) > 1: # si hay más de una, se añade el elemento a la lista de vocales.
                cAdEnAsDe_vocales.append(obj)#se agrega a la lista los elementos con dos o mas vocales
    if len(cAdEnAsDe_vocales) == 0: # si no se guardaron elementos en la lista de vocales, se retorna que no existe.
        return "No existe"
    else:
        return cAdEnAsDe_vocales
    
if __name__ == "__main__":
    lista = []# tenemos la lista
    n = int(input("Ingrese el número de elmentos que va a tener la lista: "))
    for x in range(n): #usamos un ciclo for que recorre los elementos de la lista
        obj = input("Ingrese un elemento: ")#pedimos los elementos que quiera
        lista.append(obj)#agregamos los elementos a la lista
    solu = buscamos_vocales(lista)
    print(solu)
```
## Punto 8:
- Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
```
lista1 = [] #creamos la primera lista
n = int(input("¿Cuántos elementos quieres agregar a la lista 1? ")) #el usuario dice la cantidad de elementos que tendra la lista
for i in range(n): #creamos un ciclo for para agragar elementos a a lista
    elemento = input("Ingresa un elemento: ")
    lista1.append(elemento)# agragamos los elementos


lista2 = []# creamos la segunda lista
n = int(input("¿Cuántos elementos quieres agregar a la lista 2? "))
for i in range(n):
    elemento = input("Ingresa un elemento: ")
    lista2.append(elemento)


ElementosNoPresentes = [] #creamos la lista de los elementos que no se encuentran
for elemento in lista1:#un ciclo for para recorrer los elemntos de la lista
    if elemento not in lista2: #usamos un condicional para validar que no se encuentra en la lista 2
        ElementosNoPresentes.append(elemento)# los agregamos a la lista

print("Esta es la lista 1:", lista1)
print()
print("Esta es la lista 2:", lista2)
print()
print("Los elementos de la lista 1 que no están en la lista 2 son:", ElementosNoPresentes)
```
## Punto 9:
- Resolver el punto 7 del taller 1 usando operaciones con vectores.
```
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
```
## Punto 10:
- Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
```
ñ
```
