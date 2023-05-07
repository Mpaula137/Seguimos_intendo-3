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