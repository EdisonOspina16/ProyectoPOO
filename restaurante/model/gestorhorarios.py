from .excepciones import HorarioInvalidoError
from .registroasistencia import RegistroAsistencia


class GestorHorarios:
    def __init__(self):
        self.horarios = []

    def generar_horarios(self, meseros):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horarios_generados = {}
        for dia in dias_semana:
            for mesero in meseros:
                if not mesero.tiene_descanso(dia):
                    turno = self.asignar_turno_normal()
                    mesero.registro_asistencia.append(RegistroAsistencia(dia, "Trabajo", turno))
            horarios_generados[dia] = self.asignar_turno_normal()
        return horarios_generados

    @staticmethod
    def asignar_turno(mesero, dia, inicio, fin):
        if inicio not in ["11:00 am", "12:00 pm"] or fin not in ["18:00", "15:00", "cierre"]:
            raise HorarioInvalidoError("Horario de inicio o fin inválido")
        turno = f"{inicio} - {fin}"
        mesero.registro_asistencia.append(RegistroAsistencia(dia, "Trabajo", turno))

    @staticmethod
    def verificar_disponibilidad(meseros):
        total_meseros = len(meseros)
        return total_meseros >= 8

    @staticmethod
    def asignar_turno_normal():
        turnos = [
            "11:00 am - 18:00",
            "11:00 am - 15:00 - 18:00 - cierre",
            "12:00 pm - 15:00 - 18:00 - cierre",
            "12:00 pm - cierre"
        ]
        return turnos[0]
