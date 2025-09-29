# Ejercicio 1
from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre:str):
        self.nombre = nombre
    @abstractmethod
    def CalcularSalarioMensual(self):
        pass
    def toString(self):
        return f"Nombre: {self.nombre}"
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre:str, salario_anual:float):
        super().__init__(nombre)
        self.salario_anual = salario_anual
    def CalcularSalarioMensual(self):
        return self.salario_anual / 12
    def toString(self):
        return f"{super().toString()}, Tipo: Empleado"
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre:str, horas_trabajadas:float, tarifa_por_hora:float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    def CalcularSalarioMensual(self):
        return self.horas_trabajadas * self.tarifa_por_hora
    def toString(self):
        return f"{super().toString()}, Tipo: Empleado"
empleados = []
for i in range(3):
    nombre = input(f"Ingrese nombre del empleado tiempo completo #{i+1}: ")
    salario_anual = float(input("Ingrese salario anual: "))
    empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))
for i in range(2):
    nombre = input(f"Ingrese nombre del empleado por horas #{i+1}: ")
    horas = float(input("Ingrese horas trabajadas: "))
    tarifa = float(input("Ingrese tarifa por hora: "))
    empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))
print("--- Información de Empleados ---")
for emp in empleados:
    print(emp.toString())
    print(f"Salario: {emp.CalcularSalarioMensual():.2f}")