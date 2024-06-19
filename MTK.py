import csv
import tkinter as tk
from tkinter import ttk, messagebox

class Tugas:
    def __init__(self, id_tugas, nama_tugas, mata_kuliah):
        self.id_tugas = int(id_tugas)
        self.nama_tugas = nama_tugas
        self.mata_kuliah = mata_kuliah
        
class ManajemenTugas:
    def __init__(self):
        self.tugas = []

    def tambah_tugas(self, tugas):
        if any(t.id_tugas == tugas.id_tugas for t in self.tugas):
            raise ValueError("ID tugas sudah ada.")
        self.tugas.append(tugas)

    def update_tugas(self, id_tugas, id_tugas_baru, nama_tugas_baru, mata_kuliah_baru, tanggal_deadline_baru):
        for tugas in self.tugas:
            if tugas.id_tugas == id_tugas:
                if id_tugas != id_tugas_baru and any(t.id_tugas == id_tugas_baru for t in self.tugas):
                    raise ValueError("ID tugas baru sudah ada.")
                tugas.id_tugas = int(id_tugas_baru)
                tugas.nama_tugas = nama_tugas_baru
                tugas.mata_kuliah = mata_kuliah_baru
                return True
        return False

    def hapus_tugas(self, id_tugas):
        for tugas in self.tugas:
            if tugas.id_tugas == id_tugas:
                self.tugas.remove(tugas)
                return True
        return False
    
    def cari_tugas(self, kata_kunci, berdasarkan):
        hasil = []
        for tugas in self.tugas:
            if berdasarkan == "Nama Tugas" and kata_kunci.lower() in tugas.nama_tugas.lower():
                hasil.append(tugas)
            elif berdasarkan == "Mata Kuliah" and kata_kunci.lower() in tugas.mata_kuliah.lower():
                hasil.append(tugas)
            elif berdasarkan == "ID" and kata_kunci == tugas.id_tugas:
                hasil.append(tugas)
        return hasil

    def urutkan_tugas(self, berdasarkan):
        if berdasarkan == "Mata Kuliah":
            self.tugas.sort(key=lambda x: x.mata_kuliah)
        elif berdasarkan == "ID":
            self.tugas.sort(key=lambda x: x.id_tugas)

    def simpan_tugas_ke_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama Tugas', 'Mata Kuliah'])
            for tugas in self.tugas:
                writer.writerow([tugas.id_tugas, tugas.nama_tugas, tugas.mata_kuliah])

    def muat_tugas_dari_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tugas_baru = Tugas(row['ID'], row['Nama Tugas'], row['Mata Kuliah'])
                self.tugas.append(tugas_baru)