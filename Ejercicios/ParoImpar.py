"""
Escribe un programa en Python que muestre los números del 1 al 50, indicando junto a cada número si es par o impar:


Ejemplo:

1 es impar  
2 es par  
3 es impar  
4 es par  
...  
50 es par

"""
numeros=list(range (1,51))
for numero in numeros: 
    if numero % 2 == 0:
        print(f"{numero},es par")
    else:
        print(f"{numero}, es impar")