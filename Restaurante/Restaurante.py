import Restaurante

class Restaurante:
    def __init__(self, turno: str, ):
        pass
    def agregar_mesero(self):
        pass
    def generar_horarios(self):
        turno = [
            "11:00 am - 18:00 pm",
            "11:00 am - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - cierre"
        ]
        pass
class Mesero:
    def __init__(self, nombre: str, apellido: str, telefono: int, horario: Restaurante):
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.telefono: str = telefono
        self.horario: Restaurante = horario
    def asiganar_descanso(self, dia_descanso: str):
        pass
    def dia_descanso(self, dia: str):
        pass