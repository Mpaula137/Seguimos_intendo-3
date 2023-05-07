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
      