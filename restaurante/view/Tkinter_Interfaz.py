import tkinter as tk
from tkinter import messagebox
from restaurante.model.restaurante import Restaurante


class InterfazRestaurante:
    def __init__(self, root):
        self.entry_telefono = None
        self.entry_nombre = None
        self.combo_dias_descanso = None  # Variable para almacenar el día de descanso seleccionado
        self.restaurante = Restaurante()
        self.root = root
        self.root.title("Gestión de Restaurante")

        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Sección de registro de meseros
        frame_registro = tk.LabelFrame(self.root, text="Registrar Mesero")
        frame_registro.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_registro, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame_registro)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_registro, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_telefono = tk.Entry(frame_registro)
        self.entry_telefono.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_registro, text="Día de Descanso:").grid(row=2, column=0, padx=5, pady=5)
        self.combo_dias_descanso = tk.StringVar()  # Variable para almacenar el día de descanso seleccionado
        self.combo_dias_descanso.set("Lunes")  # Valor por defecto
        tk.OptionMenu(frame_registro, self.combo_dias_descanso, *["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]).grid(row=2, column=9, padx=10, pady=5)

        btn_registrar = tk.Button(frame_registro, text="Registrar", command=self.registrar_mesero)
        btn_registrar.grid(row=2, column=1, columnspan=5, pady=5)

        # Sección de generación de horarios
        frame_horarios = tk.LabelFrame(self.root, text="Generar Horarios")
        frame_horarios.pack(padx=10, pady=10, fill="x")

        btn_generar_horarios = tk.Button(frame_horarios, text="Generar Horarios", command=self.generar_horarios)
        btn_generar_horarios.pack(pady=10)

        # Sección de consulta de agenda
        frame_agenda = tk.LabelFrame(self.root, text="Consultar Agenda")
        frame_agenda.pack(padx=10, pady=10, fill="x")

        btn_consultar_agenda = tk.Button(frame_agenda, text="Consultar Agenda", command=self.consultar_agenda)
        btn_consultar_agenda.pack(pady=10)

        # Sección de notificación de meseros
        frame_notificacion = tk.LabelFrame(self.root, text="Notificar Meseros")
        frame_notificacion.pack(padx=10, pady=10, fill="x")

        btn_notificar_meseros = tk.Button(frame_notificacion, text="Notificar Meseros", command=self.notificar_meseros)
        btn_notificar_meseros.pack(pady=10)

        # Sección de evaluación de desempeño
        frame_evaluacion = tk.LabelFrame(self.root, text="Evaluar Desempeño")
        frame_evaluacion.pack(padx=10, pady=10, fill="x")

        btn_evaluar_desempeno = tk.Button(frame_evaluacion, text="Evaluar Desempeño", command=self.evaluar_desempeno)
        btn_evaluar_desempeno.pack(pady=10)

    def registrar_mesero(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        dia_descanso = self.combo_dias_descanso.get()  # Obtener el día de descanso seleccionado
        if nombre and telefono and dia_descanso:
            try:
                self.restaurante.registrar_mesero(nombre, telefono, dia_descanso)
                messagebox.showinfo("Éxito", "Mesero registrado exitosamente")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def generar_horarios(self):
        try:
            horarios = self.restaurante.generar_horarios()
            messagebox.showinfo("Éxito", "Horarios generados exitosamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def consultar_agenda(self):
        try:
            agenda = self.restaurante.consultar_agenda()
            agenda_str = "\n".join([f"{nombre}: {asistencia}" for nombre, asistencia in agenda.items()])
            messagebox.showinfo("Agenda", agenda_str)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def notificar_meseros(self):
        try:
            self.restaurante.notificar_meseros()
            messagebox.showinfo("Éxito", "Meseros notificados exitosamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def evaluar_desempeno(self):
        try:
            evaluaciones = self.restaurante.evaluar_desempeno_meseros()
            evaluaciones_str = "\n".join([f"{nombre}: {evaluacion}" for nombre, evaluacion in evaluaciones.items()])
            messagebox.showinfo("Evaluaciones", evaluaciones_str)
        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
app = InterfazRestaurante(root)
root.mainloop()
