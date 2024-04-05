from restaurante.model.mesero import Mesero


class Restaurante:
    def __init__(self):
        self.meseros = []

    def agregar_mesero(self, nombre: str, telefono: str):
        mesero = Mesero(nombre)
        self.meseros.append(mesero)

    def asignar_descanso_personalizado(self, nombre_mesero: str, dia_descanso: str):
        for mesero in self.meseros:
            if mesero.nombre == nombre_mesero:
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
                        turno = self.asignar_turno_normal()
                        horarios_generados.append(f"{mesero.nombre}: {turno}")
                        mesero.incrementar_horas_trabajadas(dia, turno)
                    else:
                        horarios_generados.append(f"{mesero.nombre} - Descanso adicional obligatorio")
                        mesero.incrementar_horas_trabajadas(dia, "Descanso adicional")
                        mesero.reiniciar_horas_trabajadas()
        return horarios_generados

    def asignar_turno_normal(self) -> str:
        turnos = [
            "11:00 am - 18:00 pm",
            "11:00 am - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - cierre"
        ]
        return turnos[0]


"""
# Ejemplos de uso
restaurante = restaurante()
restaurante.agregar_mesero("Edison", "123456")
restaurante.agregar_mesero("Alejandro", "987654")

# Asignación de descanso personalizado
restaurante.asignar_descanso_personalizado("Edison", "Viernes")
restaurante.asignar_descanso_personalizado("Alejandro", "Miércoles")

# Mostrar horarios
restaurante.generar_horarios()"""