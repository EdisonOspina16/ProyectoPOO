from .registroasistencia import RegistroAsistencia
from datetime import datetime


class Mesero:
    def __init__(self, nombre: str, telefono: str):
        self.nombre = nombre
        self.telefono = telefono
        self.horas_trabajadas = 0
        self.registro_asistencia = []

    def asignar_descanso(self, dia: str):
        self.registro_asistencia.append(RegistroAsistencia(dia, "Descanso"))

    def calcular_horas_trabajadas(self) -> int:
        total_horas = 0
        formato_24h = "%H:%M"
        for registro in self.registro_asistencia:
            if registro.tipo == "Trabajo":
                turnos = registro.turno.split(" - ")
                for i in range(0, len(turnos)-1, 2):
                    inicio = turnos[i]
                    fin = turnos[i+1]
                    if fin == "cierre":
                        fin = "23:00"  # Asumimos que "cierre" es 23:00

                    hora_inicio = datetime.strptime(inicio, formato_24h)
                    hora_fin = datetime.strptime(fin, formato_24h)
                    horas_trabajadas = (hora_fin - hora_inicio).seconds // 3600
                    total_horas += horas_trabajadas
        return total_horas

    def tiene_descanso(self, dia: str) -> bool:
        return any(registro.dia == dia and registro.tipo == "Descanso" for registro in self.registro_asistencia)

    def __str__(self):
        return f"Mesero(nombre={self.nombre}, telefono={self.telefono})"

    def __repr__(self):
        return self.__str__()
