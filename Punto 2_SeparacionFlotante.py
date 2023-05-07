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