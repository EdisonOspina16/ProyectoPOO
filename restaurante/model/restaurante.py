from .mesero import Mesero
from .excepciones import MeseroExistenteError, AgendaNoDisponibleError

class Restaurante:
    def __init__(self):
        self.meseros = []

    def registrar_mesero(self, nombre: str, telefono: str):
        for mesero in self.meseros:
            if mesero.nombre == nombre:
                raise MeseroExistenteError("El mesero ya está registrado")
        mesero = Mesero(nombre, telefono)
        self.meseros.append(mesero)

    def consultar_agenda(self):
        if not self.meseros:
            raise AgendaNoDisponibleError("No hay meseros registrados en la agenda")
        agenda = {}
        for mesero in self.meseros:
            agenda[mesero.nombre] = mesero.registro_asistencia
        return agenda

    def calcular_salario(self, mesero):
        salario_base = 940.099
        horas_trabajadas = mesero.calcular_horas_trabajadas()
        salario_total = salario_base + (horas_trabajadas * 10)  # Suponiendo $10 por hora trabajada
        return salario_total
