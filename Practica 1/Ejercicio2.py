# Ejercicio 2
import math
class EcuacionLineal:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    def getRaiz1(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        else:
            return (-self.__b + math.sqrt(d)) / (2 * self.__a)
    def getRaiz2(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        else:
            return (-self.__b - math.sqrt(d)) / (2 * self.__a)
a, b, c = map(float, input("Ingrese a,b,c:").split())
ecuacion = EcuacionLineal(a, b, c)
discriminante = ecuacion.getDiscriminante()
if discriminante > 0:
    r1 = ecuacion.getRaiz1()
    r2 = ecuacion.getRaiz2()
    print("La ecuación tiene dos raíces", f"{r1:.6f}", "y", f"{r2:.5f}")
elif discriminante == 0:
    r1 = ecuacion.getRaiz1()
    print("La ecuación tiene una raíz", f"{r1:.6f}")
else:
    print("La ecuación no tiene raíces reales")