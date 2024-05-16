from .excepciones import HorarioInvalidoError

class Mesero:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.dia_descanso_personalizado = None
        self.horas_trabajadas = {dia: 0 for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]}

    def asignar_descanso_personalizado(self, dia_descanso: str):
        self.dia_descanso_personalizado = dia_descanso

    def tiene_dia_descanso_personalizado(self, dia: str):
        return self.dia_descanso_personalizado == dia

    def incrementar_horas_trabajadas(self, dia: str, turno: str):
        if turno not in ["11:00 am - 18:00", "11:00 am - 15:00 - 18:00 - cierre", "12:00 pm - 15:00 - 18:00 - cierre", "12:00 pm - cierre"]:
            raise HorarioInvalidoError("El turno proporcionado es inválido")
        horas_turno = turno.count("-") + 1
        self.horas_trabajadas[dia] += horas_turno

    def reiniciar_horas_trabajadas(self):
        # Reiniciar las horas trabajadas para la siguiente semana
        self.horas_trabajadas = {dia: 0 for dia in self.horas_trabajadas}