import os
import pickle
from .mesero import Mesero
from .excepciones import MeseroExistenteError, AgendaNoDisponibleError
from .gestorhorarios import GestorHorarios
from .notificador import Notificador
from .evaluadordesempeño import EvaluadorDesempeño


class Restaurante:
    def __init__(self):
        self.meseros = []
        self.carpeta_datos = "restaurante"
        self.archivo_meseros = os.path.join(self.carpeta_datos, "meseros.dat")
        self.gestor_horarios = GestorHorarios()  # Inicializar el gestor de horarios

        # Crear la carpeta de datos si no existe
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)

        # Cargar los meseros desde el archivo si existe
        if os.path.exists(self.archivo_meseros):
            with open(self.archivo_meseros, "rb") as archivo:
                self.meseros = pickle.load(archivo)

    def registrar_mesero(self, nombre: str, telefono: str, dia_descanso):
        for mesero in self.meseros:
            if mesero.nombre == nombre:
                raise MeseroExistenteError("El mesero ya está registrado")
        mesero = Mesero(nombre, telefono)
        self.meseros.append(mesero)
        self.guardar_datos()

    def consultar_agenda(self):
        if not self.meseros:
            raise AgendaNoDisponibleError("No hay meseros registrados en la agenda")
        agenda = {}
        for mesero in self.meseros:
            agenda[mesero.nombre] = mesero.registro_asistencia
        return agenda

    @staticmethod
    def calcular_salario(mesero):
        salario_base = 940.099
        horas_trabajadas = mesero.calcular_horas_trabajadas()
        salario_total = salario_base + (horas_trabajadas * 10)  # Suponiendo $10 por hora trabajada
        return salario_total

    def generar_horarios(self):
        horarios_generados = self.gestor_horarios.generar_horarios(self.meseros)
        return horarios_generados

    def notificar_meseros(self):
        for mesero in self.meseros:
            registros = "\n".join([str(registro) for registro in mesero.registro_asistencia])
            mensaje = f"Tu horario semanal es:\n{registros}\n\n"
            Notificador.notificar_mesero(mesero, mensaje)

    def evaluar_desempeno_meseros(self):
        evaluaciones = {}
        for mesero in self.meseros:
            evaluacion = EvaluadorDesempeño.evaluar_desempeño(mesero)
            evaluaciones[mesero.nombre] = evaluacion
        return evaluaciones

    def guardar_datos(self):
        # Guardar la lista de meseros en el archivo
        with open(self.archivo_meseros, "wb") as archivo:
            pickle.dump(self.meseros, archivo)
