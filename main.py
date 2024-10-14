import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class FootballApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de posiciones")
        self.label = tk.Label(root, text="Generador de Tabla de Posiciones")
        self.label.pack(pady=10)