# Ejercicio 2
import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, escalar):
        return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)
    def producto_punto(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def producto_cruzado(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)
    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normal(self):
        mag = self.longitud()
        if mag == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
a = Vector3D(1,2,3)
b = Vector3D(4,5,6)
suma = a + b
print("Suma de Vectores:", suma)
escalar = 3
producto_escalar = a * escalar
print("Multiplicación por un Escalar:", producto_escalar)
dot = a.producto_punto(b)
print("Producto Escalar:", dot)
cross = a.producto_cruzado(b)
print("Producto Vectorial:", cross)
print("Longitud de a:", a.longitud())
print("Normal de a:", a.normal())