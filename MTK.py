import csv
import tkinter as tk
from tkinter import ttk, messagebox

class Tugas:
    def __init__(self, id_tugas, nama_tugas, mata_kuliah):
        self.id_tugas = int(id_tugas)
        self.nama_tugas = nama_tugas
        self.mata_kuliah = mata_kuliah