# Ejercicio 2
from abc import ABC, abstractmethod
import random
import math
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self):
        pass
class Figura(ABC):
    def __init__(self, color):
        self.color = color
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def toString(self):
        return f"Color: {self.color}"
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
class Cuadrado(Figura, Coloreado):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado
    def area(self):
        return self.lado * self.lado
    def perimetro(self):
        return 4 * self.lado
    def comoColorear(self):
        return "Colorear los cuatro lados"
    def toString(self):
        return "Figura: Cuadrado"
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    def area(self):
        return math.pi * self.radio * self.radio
    def perimetro(self):
        return 2 * math.pi * self.radio
    def toString(self):
        return "Figura: Círculo"
figuras = []
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Naranja"]
for i in range(5):
    tipo = random.randint(1, 2)
    color = random.choice(colores)
    if tipo == 1:
        lado = random.uniform(1.0, 10.0)
        figura = Cuadrado(color, lado)
    else:
        radio = random.uniform(1.0, 10.0)
        figura = Circulo(color, radio)
    figuras.append(figura)
print("--- Información de Figuras ---")
for fig in figuras:
    print(fig.toString())
    print(f"Área: {fig.area():.2f}")
    print(f"Perímetro: {fig.perimetro():.2f}")
    if isinstance(fig, Coloreado):
        print(f"Como colorear: {fig.comoColorear()}")