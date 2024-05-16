import datetime

class Registro:
    def __init__(self):
        self.ingresos = {}
        self.salidas = {}

    def registrar_ingreso(self, mesero):
        hora_actual = datetime.datetime.now()
        self.ingresos[mesero] = hora_actual

    def registrar_salida(self, mesero):
        hora_actual = datetime.datetime.now()
        self.salidas[mesero] = hora_actual