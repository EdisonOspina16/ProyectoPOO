import tkinter as tk
from tkinter import messagebox
from restaurante.view.console import UIConsola


class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Restaurantes")

        self.ui_consola = UIConsola()

        self.label_bienvenida = tk.Label(root, text="Bienvenido al sistema de gestión de restaurantes")
        self.label_bienvenida.pack()

        self.boton_agregar_mesero = tk.Button(root, text="Agregar Mesero", command=self.agregar_mesero)
        self.boton_agregar_mesero.pack()

        self.boton_asignar_descanso = tk.Button(root, text="Asignar Día de Descanso", command=self.asignar_descanso)
        self.boton_asignar_descanso.pack()

        self.boton_generar_horarios = tk.Button(root, text="Generar Horarios", command=self.generar_horarios)
        self.boton_generar_horarios.pack()

        self.boton_salir = tk.Button(root, text="Salir", command=root.quit)
        self.boton_salir.pack()

    def agregar_mesero(self):
        nombre = tk.simpledialog.askstring("Agregar Mesero", "Ingrese el nombre del mesero:")
        telefono = tk.simpledialog.askstring("Agregar Mesero", "Ingrese el teléfono del mesero:")
        try:
            self.ui_consola.registrar_mesero(nombre, telefono)
            messagebox.showinfo("Éxito", "Mesero agregado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def asignar_descanso(self):
        nombre_mesero = tk.simpledialog.askstring("Asignar Descanso", "Ingrese el nombre del mesero:")
        dia_descanso = tk.simpledialog.askstring("Asignar Descanso", "Ingrese el día de descanso:")
        try:
            mensaje = self.ui_consola.asignar_descanso_personalizado(nombre_mesero, dia_descanso)
            messagebox.showinfo("Éxito", mensaje)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generar_horarios(self):
        try:
            horarios_generados = self.ui_consola.generar_horarios()
            messagebox.showinfo("Horarios Generados", "\n".join(horarios_generados))
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()
