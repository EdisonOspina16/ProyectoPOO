from .registroasistencia import RegistroAsistencia

class Mesero:
    def __init__(self, nombre: str, telefono: str):
        self.nombre = nombre
        self.telefono = telefono
        self.horas_trabajadas = 0
        self.registro_asistencia = []

    def asignar_descanso(self, dia: str):
        self.registro_asistencia.append(RegistroAsistencia(dia, "Descanso"))

    def calcular_horas_trabajadas(self) -> int:
        return sum(1 for registro in self.registro_asistencia if registro.tipo == "Trabajo")
