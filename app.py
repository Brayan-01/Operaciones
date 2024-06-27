

#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 2.0
# 25/04/2024
# Ficha: 2877795
#Funcion: Operaciones basicas 

#*************

# Define una funcion "saludo" para dar la bienvenida
def saludo():
    #Imprime un mensaje en pantalla
    print("Hola Mundo!! ")

# Define la suma de dos numeros 
def sumar(dato1, dato2):
    #Devuelve el resultado de la suma de estos dos
    return dato1 + dato2

# Define la resta entre dos numeros
def restar(dato1,dato2):
    #Devuelve el resultado de la resta de estos numeros
    return dato1 - dato2

# Define la multiplicacion entre dos numeros
def multiplicar(dato1,dato2):
    #Devuelve el resultado de la multiplicacion de estos numeros
    return dato1 * dato2

# Define la division entre dos numeros
def dividir(dato1,dato2):
    #Devuelve el resultado de la division entre estos numeros
    return dato1 / dato2

#Creamos la este if para ejecutar correctamente el programa
if __name__ == "__main__":
    print("\n********Inicio********\n"  )
    saludo()
    
    print('\n'"**************************************************************")
    # Pedimos al usuario que escriba los números
    num1 = float(input('\n'"Escribe el primer número: "))
    num2 = float(input('\n'"Escribe el segundo número: "))
    
    print('\n'"**************************************************************")
    #Imprimimos los resultados de las operaciones correspondientes
    print('\n'"El resultado de la suma es de ", sumar(num1, num2))
    print('\n'"El resultado de la resta es ", restar(num1, num2))
    print('\n'"El resultado de la multiplicacion es", multiplicar(num1, num2))
    print('\n'"El resultado de la division es ", dividir(num1, num2))
    print('\n'"*********Fin********")
    
