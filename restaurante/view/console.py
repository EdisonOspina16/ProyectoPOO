from restaurante.model.restaurante import Restaurante


class UIConsola:
    def __init__(self):
        self.restaurante = Restaurante()

    def ejecutar_app(self):
        while True:
            print("\nBienvenido al sistema de gestión de restaurantes.")
            print("Seleccione una opción:")
            print("1. Agregar mesero")
            print("2. Asignar día de descanso personalizado a un mesero")
            print("3. Generar horarios")
            print("4. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del mesero: ")
                telefono = input("Ingrese el teléfono del mesero: ")
                self.restaurante.agregar_mesero(nombre, telefono)
                print("Mesero agregado exitosamente.")

            elif opcion == "2":
                nombre_mesero = input("Ingrese el nombre del mesero al que desea asignar el día de descanso: ")
                dia_descanso = input("Ingrese el día de descanso personalizado para el mesero: ")
                mensaje = self.restaurante.asignar_descanso_personalizado(nombre_mesero, dia_descanso)
                print(mensaje)

            elif opcion == "3":
                horarios_generados = self.restaurante.generar_horarios()
                for horario in horarios_generados:
                    print(horario)

            elif opcion == "4":
                print("Gracias por usar el sistema de gestión de restaurantes. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
