import tkinter as tk
from restaurante.view.Tkinter_Interfaz import InterfazRestaurante

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazRestaurante(root)
    root.mainloop()
