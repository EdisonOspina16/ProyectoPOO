class Mesero:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.dia_descanso_personalizado = None

    def asignar_descanso_personalizado(self, dia_descanso: str):
        self.dia_descanso_personalizado = dia_descanso

    def tiene_dia_descanso_personalizado(self, dia: str):
        return self.dia_descanso_personalizado == dia


class Restaurante:
    def __init__(self):
        self.meseros = []

    def agregar_mesero(self, nombre: str, correo: str):
        mesero = Mesero(nombre)
        self.meseros.append(mesero)

    def asignar_descanso_personalizado(self, nombre_mesero: str, dia_descanso: str):
        for mesero in self.meseros:
            if mesero.nombre == nombre_mesero:
                mesero.asignar_descanso_personalizado(dia_descanso)
                print(f"Se ha asignado el día de descanso personalizado '{dia_descanso}' al mesero {nombre_mesero}.")
                return
        print(f"No se encontró al mesero con nombre {nombre_mesero}.")

    def mostrar_horarios(self):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias_semana:
            print(f"\nHorarios para el día {dia}:")
            for mesero in self.meseros:
                if mesero.tiene_dia_descanso_personalizado(dia):
                    print(f"{mesero.nombre} - Descanso")
                else:
                    print(f"{mesero.nombre}:")
                    print(" - ".join(generar_turnos()))


def generar_turnos() -> list:
    return [
        "11:00 am - 18:00 pm",
        "11:00 am - 15:00 pm - 18:00 pm - cierre",
        "12:00 pm - 15:00 pm - 18:00 pm - cierre",
        "12:00 pm - cierre"
    ]


# Ejemplos de uso
restaurante = Restaurante()
restaurante.agregar_mesero("Edison", "edison@soyudemedellin.com")
restaurante.agregar_mesero("Alejandro", "alejandro@soyudemedellin.com")

# Asignación de descanso personalizado
restaurante.asignar_descanso_personalizado("Edison", "Viernes")
restaurante.asignar_descanso_personalizado("Alejandro", "Miércoles")

# Mostrar horarios
restaurante.mostrar_horarios()
