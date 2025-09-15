# Ejercicio 1
# pip install multimethod
from multimethod import multimethod
import math
class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @multimethod
    def perpendicular(self):
        suma = []
        resta = []
        for i in range(len(self.a)):
            suma.append(self.a[i] + self.b[i])
            resta.append(self.a[i] - self.b[i])
        return suma, resta
    @multimethod
    def perpendicular(self, vector: list):
        suma = 0
        for i in range(len(vector)):
            suma += vector[i] ** 2
        return math.sqrt(suma)
    @multimethod
    def perpendicular(self, a: int):
        resultado = 0
        for i in range(len(self.a)):
            resultado += self.a[i] * self.b[i]
        return resultado
    @multimethod
    def perpendicular(self, b: float):
        suma, resta = self.perpendicular()
        iguales = suma == resta
        mag_suma = self.perpendicular(suma) ** 2
        mag_a = self.perpendicular(self.a) ** 2
        mag_b = self.perpendicular(self.b) ** 2
        pitagoras = round(mag_suma, 5) == round(mag_a + mag_b, 5)
        producto = self.perpendicular(0)
        perpendicular = producto == 0
        return perpendicular
    @multimethod
    def paralela(self):
        proporciones = []
        for i in range(len(self.a)):
            if self.b[i] != 0:
                proporciones.append(self.a[i] / self.b[i])
        if len(proporciones) == 0:
            return False
        r = proporciones[0]
        for i in range(len(proporciones)):
            if proporciones[i] != r:
                return False
        return True
    @multimethod
    def paralela(self, a:int):
        if len(self.a) == 3 and len(self.b) == 3:
            cx = self.a[1]*self.b[2] - self.a[2]*self.b[1]
            cy = self.a[2]*self.b[0] - self.a[0]*self.b[2]
            cz = self.a[0]*self.b[1] - self.a[1]*self.b[0]
            return [cx, cy, cz]
        else:
            return None
    def proyeccion_de_a_sobre_b(self):
        dot = self.perpendicular(0)
        mag_b = self.perpendicular(self.b)
        mag_b_cuadrado = mag_b ** 2
        escalar = dot / mag_b_cuadrado
        resultado = []
        for i in range(len(self.b)):
            resultado.append(escalar * self.b[i])
        return resultado
    def componente_de_a_en_b(self):
        dot = self.perpendicular(0)
        mag_b = self.perpendicular(self.b)
        return dot / mag_b
a = [2, 4, 6]
b = [1, 2, 3]
vectores = AlgebraVectorial(a, b)
print("¿Son perpendiculares?:", vectores.perpendicular(1.0))
print("¿Son paralelos?:", vectores.paralela())
print("Proyección de a sobre b:", vectores.proyeccion_de_a_sobre_b())
print("Componente de a en dirección de b:", vectores.componente_de_a_en_b())