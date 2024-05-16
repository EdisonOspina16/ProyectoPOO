from .mesero import Mesero
from .excepciones import MeseroExistenteError, AgendaNoDisponibleError, NotificacionError

class Restaurante:
    def __init__(self):
        self.meseros = []

    def agregar_mesero(self, nombre: str, telefono: str):
        for mesero in self.meseros:
            if mesero.nombre == nombre:
                raise MeseroExistenteError("El mesero ya está registrado")
        mesero = Mesero(nombre)
        self.meseros.append(mesero)

    def asignar_descanso_personalizado(self, nombre_mesero: str, dia_descanso: str):
        for mesero in self.meseros:
            if mesero.nombre == nombre_mesero:
                # Verificar si el día de descanso personalizado está disponible
                if dia_descanso not in mesero.horas_trabajadas:
                    raise AgendaNoDisponibleError("El día seleccionado no está disponible para el descanso personalizado")
                # Verificar si ya se alcanzó el límite de personal en descanso para ese día
                descansos_dia = sum(1 for m in self.meseros if m.tiene_dia_descanso_personalizado(dia_descanso))
                if descansos_dia >= len(self.meseros) / 2:
                    raise AgendaNoDisponibleError("Se ha alcanzado el límite de personal en descanso para este día")
                mesero.asignar_descanso_personalizado(dia_descanso)
                return f"Se ha asignado el día de descanso personalizado '{dia_descanso}' al mesero {nombre_mesero}."
        return f"No se encontró al mesero con nombre {nombre_mesero}."

    def generar_horarios(self):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horas_maximas_semana = 48
        horarios_generados = []
        for dia in dias_semana:
            horarios_generados.append(f"\nHorarios para el día {dia}:")
            for mesero in self.meseros:
                if mesero.tiene_dia_descanso_personalizado(dia):
                    horarios_generados.append(f"{mesero.nombre} - Descanso")
                else:
                    horas_trabajadas_semana = sum(mesero.horas_trabajadas.values())
                    if horas_trabajadas_semana < horas_maximas_semana:
                        turno = self.asignar_turno_normal(dia)
                        horarios_generados.append(f"{mesero.nombre}: {turno}")
                        mesero.incrementar_horas_trabajadas(dia, turno)
                    else:
                        horarios_generados.append(f"{mesero.nombre} - Descanso adicional obligatorio")
                        mesero.incrementar_horas_trabajadas(dia, "Descanso adicional")
                        mesero.reiniciar_horas_trabajadas()
        return horarios_generados

    def asignar_turno_normal(self, dia: str) -> str:
        if dia in ["Lunes", "Martes", "Miércoles", "Jueves"]:
            return "11:00 am - 18:00"
        elif dia == "Viernes" or dia == "Sábado":
            return "11:00 am - 15:00 - 18:00 - cierre"
        elif dia == "Domingo":
            return "12:00 pm - 15:00 - 18:00 - cierre"

    def consultar_agenda(self):
        if not self.meseros:
            raise AgendaNoDisponibleError("No hay meseros registrados en la agenda")
        agenda = {}
        for mesero in self.meseros:
            agenda[mesero.nombre] = mesero.horas_trabajadas
        return agenda

    def notificar_mesero(self, mesero, mensaje):
        if not mensaje:
            raise NotificacionError("El mensaje de notificación está vacío")
        # Aquí iría la lógica para notificar a un mesero


    def calcular_salario(self, mesero):
        if mesero not in self.meseros:
            raise ValueError("El mesero no está registrado en el restaurante")
        # Aquí iría la lógica para calcular el salario de un mesero
        salario_base = 940.099
        horas_trabajadas = self.calcular_horas_trabajadas(mesero)
        salario_total = salario_base + (horas_trabajadas * 10)  # Suponiendo $10 por hora trabajada
        return salario_total

    def calcular_horas_trabajadas(self, mesero):
        if mesero not in self.meseros:
            raise ValueError("El mesero no está registrado en el restaurante")
        return sum(mesero.horas_trabajadas.values())

    def evaluar_desempeño(self, mesero):
        if mesero not in self.meseros:
            raise ValueError("El mesero no está registrado en el restaurante")
        # Aquí iría la lógica para evaluar el desempeño de un mesero
        horas_trabajadas = self.calcular_horas_trabajadas(mesero)
        if horas_trabajadas > 40:
            return "Excelente desempeño"
        elif horas_trabajadas > 30:
            return "Buen desempeño"
        else:
            return "Desempeño regular"

