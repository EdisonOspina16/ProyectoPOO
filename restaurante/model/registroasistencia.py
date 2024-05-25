class RegistroAsistencia:
    def __init__(self, dia: str, tipo: str, turno: str = None):
        self.dia = dia
        self.tipo = tipo  # "Trabajo" o "Descanso"
        self.turno = turno  # Solo relevante para "Trabajo"

    def __str__(self):
        return f"RegistroAsistencia(dia={self.dia}, tipo={self.tipo}, turno={self.turno})"

    def __repr__(self):
        return self.__str__()
