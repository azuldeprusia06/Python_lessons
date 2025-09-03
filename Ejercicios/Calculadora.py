"""
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

Ejemplo de uso:
Ingrese el primer número: 10  
Ingrese el segundo número: 5  
Ingrese la operación (suma, resta, multiplicación, división): multiplicación  

El resultado es: 50

Pistas:
La función principal no debería hacer los cálculos directamente, sino delegar en las funciones auxiliares.
Puedes usar condicionales (if/elif) para decidir qué función llamar.
Recuerda manejar la división para evitar errores si el divisor es 0.


"""

try:
    number1=float(input("Ingresa un numero"))
except ValueError
    print("Valor no valido, ingresa un número")

try:
    number2=float(input("Ingresa un numero"))
except ValueError
    print("Valor no valido, ingresa un número")
operation=input("Ingresa una operación (suma, resta, multiplicación o división)")

try:
    def calculator (number1,number2)
    if operation = "suma"or"Suma"
        resultado: number1+number2
        print(resultado)
        