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