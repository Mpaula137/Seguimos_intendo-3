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
        x = x // 10 # se le dice al ciclo que elimine el último digito
    numeros.reverse() #usamos el reverse para que en la lista se 
    print("Esta es la lista de los digitos de el numero ingresado:", numeros[:])

if __name__ == "__main__":  #Funcion principal
 n = int(input("Ingrese un numero por favor:"))
 separar(n)