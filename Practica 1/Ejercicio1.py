# Ejercicio 1
class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0
    def getX(self):
        numerador = self.__e * self.__d - self.__b * self.__f
        denominador = self.__a * self.__d - self.__b * self.__c
        return numerador / denominador
    def getY(self):
        numerador = self.__a * self.__f - self.__e * self.__c
        denominador = self.__a * self.__d - self.__b * self.__c
        return numerador / denominador
a,b,c,d,e,f = map(float,input("Ingrese a,b,c,d,e,f:").split())
ecuacion = EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion():
    x = ecuacion.getX()
    y = ecuacion.getY()
    print("x =", x, ", y =", y)
else:
    print("La ecuación no tiene solución")