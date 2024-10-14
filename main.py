import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class FootballApp:
    def __init__(self, root):
        # Configuración básica de la ventana
        self.root = root
        self.root.title("Tabla de Posiciones")
        self.root.geometry("400x300")
        self.root.config(bg="#2c3e50")  # Fondo oscuro

        # Estilo del título
        self.label = tk.Label(root, text="Generador de Tabla de Posiciones", 
                              font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.label.pack(pady=20)

        # Botón para cargar el archivo
        self.load_button = tk.Button(root, text="Cargar Archivo de Google Drive", 
                                     command=self.load_file, bg="#3498db", fg="white", font=("Helvetica", 12))
        self.load_button.pack(pady=10)

        # Botón para generar la tabla
        self.generate_button = tk.Button(root, text="Generar Tabla", 
                                         command=self.generate_table, bg="#2ecc71", fg="white", font=("Helvetica", 12))
        self.generate_button.pack(pady=10)

    def load_file(self):
        # Función para cargar el archivo
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            messagebox.showinfo("Archivo Cargado", "Archivo cargado con éxito")

    def generate_table(self):
        # Función para generar la tabla (por ahora muestra un mensaje)
        messagebox.showinfo("Generar", "Generando tabla...")

if __name__ == "__main__":
    root = tk.Tk()
    app = FootballApp(root)
    root.mainloop()

