import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class FootballApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de posiciones")
        self.label = tk.Label(root, text="Generador de Tabla de Posiciones")
        self.label.pack(pady=10)
        self.load_button = tk.Button(root, text="Cargar Archivo de Google Drive", command=self.load_file)
        self.load_button.pack(pady=5)
        self.generate_button = tk.Button(root, text="Generar Tabla", command=self.generate_table)
        self.generate_button.pack(pady=5)

    def load_file(self):
            file_path = filedialog.askopenfilename()
            if file_path:
                self.file_path = file_path
                messagebox.showinfo("Archivo Cargado", "Archivo cargado con éxito")

    def generate_table(self):
            
            messagebox.showinfo("Generar", "Generando tabla...")


if __name__ == "__main__":
    root = tk.Tk()
    app = FootballApp(root)
    root.mainloop()
