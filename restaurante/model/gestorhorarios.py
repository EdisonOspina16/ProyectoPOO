from .excepciones import HorarioInvalidoError
class GestorHorarios:
    def __init__(self):
        self.horarios = []

    def generar_horarios(self):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horarios_generados = {}
        for dia in dias_semana:
            horarios_generados[dia] = self.asignar_turno_normal()
        return horarios_generados

    def asignar_turno(self, mesero, dia, inicio, fin):
        if inicio not in ["11:00 am", "12:00 pm"] or fin not in ["18:00", "15:00", "cierre"]:
            raise HorarioInvalidoError("Horario de inicio o fin inválido")
        turno = f"{inicio} - {fin}"
        mesero.registro_asistencia.append(RegistroAsistencia(dia, "Trabajo", turno))

    def verificar_disponibilidad(self):
        total_meseros = len(self.horarios)
        if total_meseros < 8:
            return False
        return True

    def asignar_turno_normal(self):
        turnos = [
            "11:00 am - 18:00",
            "11:00 am - 15:00 - 18:00 - cierre",
            "12:00 pm - 15:00 - 18:00 - cierre",
            "12:00 pm - cierre"
        ]
        return turnos[0]
