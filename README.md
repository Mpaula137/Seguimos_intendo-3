# Seguimos_intento:3
Resolución del taller propuesto haciendo uso de bucles, vectores, listas, etc.
 ### Integrantes del grupo ###
 - Maria Paula Machuca Hortua
 - Aaron Diaz
 - Diego

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
- Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.
- 
