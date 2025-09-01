Enunciado

Crea un programa que pida al usuario dos números y una operación a realizar (suma, resta, multiplicación o división).

Define una función principal llamada calculadora() que:

Pida los datos al usuario (dos números y la operación).

Llame a otra función auxiliar según la operación elegida.

Muestre el resultado final.

Define funciones auxiliares:

sumar(a, b)

restar(a, b)

multiplicar(a, b)

dividir(a, b)

Ejemplo de uso
Ingrese el primer número: 10  
Ingrese el segundo número: 5  
Ingrese la operación (suma, resta, multiplicación, división): multiplicación  

El resultado es: 50

Pistas

La función principal no debería hacer los cálculos directamente, sino delegar en las funciones auxiliares.

Puedes usar condicionales (if/elif) para decidir qué función llamar.

Recuerda manejar la división para evitar errores si el divisor es 0.
number_1:input(float"Ingresa el primer número")
number_2: input(float"Ingresa el segundo número")
operation:input("Ingresa la operacion (suma, resta, multiplicación o división)")

def calculadora(number_1,number_2)
    if operation == suma == number_1 + number_2
    elif operation ==resta == number_1 - number_2
    elif operation == multiplicación == number_1*number_2
    elif operation == división == number_1/number_2
    elif operation == división and number_2 == 0 
        print("Error, no se puede dividir entre 0")
    else pritn("Valor no valido")
