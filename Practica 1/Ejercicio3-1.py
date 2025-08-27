# Ejercicio 3.1 en Programación Modular-Estructurada
import math
def promedio(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma / len(numeros)
def desviacion(numeros):
    prom = promedio(numeros)
    suma_diferencias = 0
    for num in numeros:
        suma_diferencias += (num - prom) ** 2
    return math.sqrt(suma_diferencias / (len(numeros) - 1))
numeros = list(map(float,input("Ingrese 10 números:").split()))
prom = promedio(numeros)
des = desviacion(numeros)
print("El promedio es", f"{prom:.2f}")
print("La desviación estandar es", f"{des:.5f}")