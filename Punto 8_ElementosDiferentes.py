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