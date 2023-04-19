# Seguimos_intendo:3
Resolución del taller propuesto haciendo uso de bucles, vectores, listas, etc.
1. separarcionde digitos en un numero:
''' numeros = []
def separar(x):
    while x > 0:
        print(x%10)
        numeros.append(x % 10)
        x = x // 10
    print(numeros[:])

n = int(input("Ingrese un numero por favor:"))
separar(n) '''
