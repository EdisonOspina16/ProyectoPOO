import tkinter as tk
from tkinter import ttk, messagebox
from restaurante.model.restaurante import Restaurante
from restaurante.model.excepciones import MeseroExistenteError, AgendaNoDisponibleError


class Aplicacion:
    def __init__(self, root):
        self.restaurante = Restaurante()
        self.root = root
        self.root.title("Sistema de Gestión de Restaurante")

        # Crear pestañas
        self.tab_control = ttk.Notebook(self.root)
        self.tab_registro = ttk.Frame(self.tab_control)
        self.tab_agenda = ttk.Frame(self.tab_control)
        self.tab_salario = ttk.Frame(self.tab_control)
        self.tab_horarios = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_registro, text="Registrar Mesero")
        self.tab_control.add(self.tab_agenda, text="Consultar Agenda")
        self.tab_control.add(self.tab_salario, text="Calcular Salario")
        self.tab_control.add(self.tab_horarios, text="Gestionar Horarios")
        self.tab_control.pack(expand=1, fill="both")

        # Pestaña de registro
        self.label_nombre = tk.Label(self.tab_registro, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.tab_registro)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_telefono = tk.Label(self.tab_registro, text="Teléfono:")
        self.label_telefono.grid(row=1, column=0, padx=10, pady=10)
        self.entry_telefono = tk.Entry(self.tab_registro)
        self.entry_telefono.grid(row=1, column=1, padx=10, pady=10)

        self.boton_registrar = tk.Button(self.tab_registro, text="Registrar Mesero", command=self.registrar_mesero)
        self.boton_registrar.grid(row=2, columnspan=2, padx=10, pady=10)

        # Pestaña de agenda
        self.boton_agenda = tk.Button(self.tab_agenda, text="Consultar Agenda", command=self.consultar_agenda)
        self.boton_agenda.pack(pady=10)
        self.text_agenda = tk.Text(self.tab_agenda, height=15, width=50)
        self.text_agenda.pack(padx=10, pady=10)

        # Pestaña de salario
        self.label_mesero_salario = tk.Label(self.tab_salario, text="Nombre del Mesero:")
        self.label_mesero_salario.grid(row=0, column=0, padx=10, pady=10)
        self.entry_mesero_salario = tk.Entry(self.tab_salario)
        self.entry_mesero_salario.grid(row=0, column=1, padx=10, pady=10)

        self.boton_calcular_salario = tk.Button(self.tab_salario, text="Calcular Salario", command=self.calcular_salario)
        self.boton_calcular_salario.grid(row=1, columnspan=2, padx=10, pady=10)
        self.label_resultado_salario = tk.Label(self.tab_salario, text="")
        self.label_resultado_salario.grid(row=2, columnspan=2, padx=10, pady=10)

        # Pestaña de horarios
        self.label_mesero_horario = tk.Label(self.tab_horarios, text="Nombre del Mesero:")
        self.label_mesero_horario.grid(row=0, column=0, padx=10, pady=10)
        self.entry_mesero_horario = tk.Entry(self.tab_horarios)
        self.entry_mesero_horario.grid(row=0, column=1, padx=10, pady=10)

        self.label_dia_descanso = tk.Label(self.tab_horarios, text="Día de Descanso:")
        self.label_dia_descanso.grid(row=1, column=0, padx=10, pady=10)
        self.combo_dia_descanso = ttk.Combobox(self.tab_horarios, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        self.combo_dia_descanso.grid(row=1, column=1, padx=10, pady=10)

        self.boton_asignar_descanso = tk.Button(self.tab_horarios, text="Asignar Descanso", command=self.asignar_descanso)
        self.boton_asignar_descanso.grid(row=2, columnspan=2, padx=10, pady=10)

        self.boton_mostrar_horarios = tk.Button(self.tab_horarios, text="Mostrar Horarios", command=self.mostrar_horarios)
        self.boton_mostrar_horarios.grid(row=3, columnspan=2, padx=10, pady=10)
        self.text_horarios = tk.Text(self.tab_horarios, height=15, width=50)
        self.text_horarios.grid(row=4, columnspan=2, padx=10, pady=10)

    def registrar_mesero(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        try:
            self.restaurante.registrar_mesero(nombre, telefono)
            messagebox.showinfo("Éxito", "Mesero registrado correctamente.")
        except MeseroExistenteError as e:
            messagebox.showerror("Error", e.obtener_mensaje())
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

    def consultar_agenda(self):
        try:
            agenda = self.restaurante.consultar_agenda()
            self.text_agenda.delete(1.0, tk.END)
            for nombre, registros in agenda.items():
                self.text_agenda.insert(tk.END, f"Mesero: {nombre}\n")
                for registro in registros:
                    self.text_agenda.insert(tk.END, f"  {registro.fecha}: {registro.tipo}\n")
                self.text_agenda.insert(tk.END, "\n")
        except AgendaNoDisponibleError as e:
            messagebox.showerror("Error", e.obtener_mensaje())

    def calcular_salario(self):
        nombre = self.entry_mesero_salario.get()
        mesero = next((m for m in self.restaurante.meseros if m.nombre == nombre), None)
        if mesero:
            salario = self.restaurante.calcular_salario(mesero)
            self.label_resultado_salario.config(text=f"Salario Total: ${salario:.2f}")
        else:
            messagebox.showerror("Error", "Mesero no encontrado.")
        self.entry_mesero_salario.delete(0, tk.END)

    def asignar_descanso(self):
        nombre = self.entry_mesero_horario.get()
        dia_descanso = self.combo_dia_descanso.get()
        mesero = next((m for m in self.restaurante.meseros if m.nombre == nombre), None)
        if mesero:
            gestor_horarios = self.restaurante.gestor_horarios
            gestor_horarios.asignar_descanso(dia_descanso)
            messagebox.showinfo("Éxito", f"Día de descanso asignado: {dia_descanso}")
        else:
            messagebox.showerror("Error", "Mesero no encontrado.")
        self.entry_mesero_horario.delete(0, tk.END)
        self.combo_dia_descanso.set('')

    def mostrar_horarios(self):
        try:
            horarios = self.restaurante.gestor_horarios.generar_horarios()
            self.text_horarios.delete(1.0, tk.END)
            for dia, turno in horarios.items():
                self.text_horarios.insert(tk.END, f"{dia}: {turno}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

