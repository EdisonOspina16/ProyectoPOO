import tkinter as tk
from tkinter import messagebox
from restaurante.model.restaurante import Restaurante
from restaurante.model.excepciones import MeseroExistenteError, AgendaNoDisponibleError, NotificacionError
from tkinter import simpledialog


class UIConsola:
    def __init__(self):
        self.restaurante = Restaurante()
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Restaurantes")

        self.label_bienvenida = tk.Label(self.ventana, text="Bienvenido al sistema de gestión de restaurantes.",
                                         font=("Arial", 12))
        self.label_bienvenida.pack(pady=10)

        self.boton_agregar_mesero = tk.Button(self.ventana, text="Agregar Mesero", command=self.agregar_mesero)
        self.boton_agregar_mesero.pack(pady=5)

        self.boton_asignar_descanso = tk.Button(self.ventana, text="Asignar Día de Descanso",
                                                command=self.asignar_descanso)
        self.boton_asignar_descanso.pack(pady=5)

        self.boton_generar_horarios = tk.Button(self.ventana, text="Generar Horarios", command=self.generar_horarios)
        self.boton_generar_horarios.pack(pady=5)

        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.quit)
        self.boton_salir.pack(pady=5)

    def agregar_mesero(self):
        nombre = tk.simpledialog.askstring("Agregar Mesero", "Ingrese el nombre del mesero:")
        telefono = tk.simpledialog.askstring("Agregar Mesero", "Ingrese el teléfono del mesero:")
        try:
            self.restaurante.agregar_mesero(nombre, telefono)
            messagebox.showinfo("Éxito", "Mesero agregado exitosamente.")
        except MeseroExistenteError as e:
            messagebox.showerror("Error", e.obtener_mensaje())

    def asignar_descanso(self):
        nombre_mesero = tk.simpledialog.askstring("Asignar Día de Descanso", "Ingrese el nombre del mesero:")
        dia_descanso = tk.simpledialog.askstring("Asignar Día de Descanso", "Ingrese el día de descanso:")
        try:
            mensaje = self.restaurante.asignar_descanso_personalizado(nombre_mesero, dia_descanso)
            messagebox.showinfo("Éxito", mensaje)
        except (MeseroExistenteError, AgendaNoDisponibleError, NotificacionError) as e:
            messagebox.showerror("Error", e.obtener_mensaje())

    def generar_horarios(self):
        horarios_generados = self.restaurante.generar_horarios()
        horarios_str = "\n".join(horarios_generados)
        messagebox.showinfo("Horarios Generados", horarios_str)

    def ejecutar_app(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    interfaz = UIConsola()
    interfaz.ejecutar_app()
