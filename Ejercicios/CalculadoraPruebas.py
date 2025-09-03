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
    number1=float(input("Ingresa un numero: "))
except ValueError:
    print("Valor no valido, ingresa un número")
try:
    number2=float(input("Ingresa un segundo numero: "))
except ValueError:
    print("Valor no valido, ingresa un número")
operation=input("Ingresa una operación (suma, resta, multiplicación o división): ").lower()




def suma (a, b):
    return a + b


def resta (a, b):
    return a - b


def multi (a , b):
    return a * b

def divi (a, b):
    return a / b


def Calculadora(num1, num2, op):
    if op == "suma":
        resultado=suma(num1,num2)
        print(f"El resultado es: {resultado}")
    elif op == "resta":
        resultado = resta(num1,num2)
        print(f"El resultado es: {resultado}")
    elif op == "multiplicacion":
        resultado = multi(num1,num2)
        print(f"El resultado es: {resultado}")   
    elif op == "division":
        if num2 == 0:
            print("El divisor no puede ser 0, vuelva ejecutar la funcion")
            return
        resultado = divi(num1,num2)
        print(f"El resultado es: {resultado}")
    
    else: print("Algo tocaste mal")


try:
    Calculadora(number1, number2, operation)
except ValueError:
    print("Algo salió mal en la ejecución de la calculadora")

   




"""

1) Codear el WHILE para la pedida de numeros y operaciones

2)  Validar si la operación que escribió el usuario, es correcta. (Ver lista, include)
    operacionesValidas = [suma, resta, divi, multi]
    LISTA operacionesValidas "INCLUDE"

3) OPCIONAL: Ver si se puede refactorizar la función utilizando un diccionario.
    operacionesPosibles = {suma: +,resta: -, multi: *, divi: /}

4) Realizarlo con TRY / EXCEPT / FINALLY

"""
