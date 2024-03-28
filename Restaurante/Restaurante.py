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

    def generar_horarios(self):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horas_maximas_semana = 48
        for dia in dias_semana:
            print(f"\nHorarios para el día {dia}:")
            for mesero in self.meseros:
                if mesero.tiene_dia_descanso_personalizado(dia):
                    print(f"{mesero.nombre} - Descanso")
                else:
                    horas_trabajadas_semana = sum(mesero.horas_trabajadas.values())
                    if horas_trabajadas_semana < horas_maximas_semana:
                        turno = self.asignar_turno_normal()
                        print(f"{mesero.nombre}: {turno}")
                        mesero.incrementar_horas_trabajadas(dia, turno)
                    else:
                        print(f"{mesero.nombre} - Descanso adicional obligatorio")
                        mesero.incrementar_horas_trabajadas(dia, "Descanso adicional")
                        mesero.reiniciar_horas_trabajadas()

    def asignar_turno_normal(self) -> str:
        turnos = [
            "11:00 am - 18:00 pm",
            "11:00 am - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - cierre"
        ]
        return turnos[0]

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
        horas_turno = turno.count("-") + 1
        self.horas_trabajadas[dia] += horas_turno

    def reiniciar_horas_trabajadas(self):
        # Reiniciar las horas trabajadas para la siguiente semana
        self.horas_trabajadas = {dia: 0 for dia in self.horas_trabajadas}


# Ejemplos de uso
restaurante = Restaurante()
restaurante.agregar_mesero("Edison", "edison@soyudemedellin.com")
restaurante.agregar_mesero("Alejandro", "alejandro@soyudemedellin.com")

# Asignación de descanso personalizado
restaurante.asignar_descanso_personalizado("Edison", "Viernes")
restaurante.asignar_descanso_personalizado("Alejandro", "Miércoles")

# Mostrar horarios
restaurante.generar_horarios()