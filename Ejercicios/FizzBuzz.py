"""
Enunciado:

Escribe un programa en Python que muestre los números del 1 al 100, pero aplicando estas reglas:

- Si el número es múltiplo de 3, en lugar del número debe mostrar la palabra "Fizz".
- Si el número es múltiplo de 5, en lugar del número debe mostrar la palabra "Buzz".
- Si el número es múltiplo tanto de 3 como de 5, debe mostrar la palabra "FizzBuzz".
- En cualquier otro caso, simplemente muestra el número.
""" 


numeros= list(range (1,101))


def fizzbuzz(numeros):
    for numero in numeros:
        if numero % 3== 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")

        else: print(numero)

fizzbuzz(numeros)
