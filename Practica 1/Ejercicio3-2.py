# Ejercicio 3.2 en Programación Orientada a Objetos
import math
class Estadistica:
    def __init__(self, numeros):
        self.__numeros = numeros
    def promedio(self):
        suma = 0
        for num in self.__numeros:
            suma += num
        return suma / len(self.__numeros)
    def desviacion(self):
        prom = self.promedio()
        suma_diferencias = 0
        for num in self.__numeros:
            suma_diferencias += (num - prom) ** 2
        return math.sqrt(suma_diferencias / (len(self.__numeros) - 1))
numeros = list(map(float,input("Ingrese 10 números:").split()))
est = Estadistica(numeros)
prom = est.promedio()
des = est.desviacion()
print("El promedio es", f"{prom:.2f}")
print("La desviación estandar es", f"{des:.5f}")