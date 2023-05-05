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
