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
