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
                
class TugasGUI:
    def __init__(self, root):
        self.manajemen_tugas = ManajemenTugas()
        self.manajemen_tugas.muat_tugas_dari_csv('tugas.csv')  # Memuat tugas dari file CSV saat aplikasi dimulai
        self.root = root
        self.root.title("Sistem Manajemen Tugas Kuliah")

        # Frame Tugas
        self.frame_tugas = ttk.LabelFrame(self.root, text="Tugas Kuliah")
        self.frame_tugas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.lbl_id_tugas = ttk.Label(self.frame_tugas, text="ID Tugas:")
        self.lbl_id_tugas.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_id_tugas = ttk.Entry(self.frame_tugas)
        self.ent_id_tugas.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.lbl_nama_tugas = ttk.Label(self.frame_tugas, text="Nama Tugas:")
        self.lbl_nama_tugas.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ent_nama_tugas = ttk.Entry(self.frame_tugas)
        self.ent_nama_tugas.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        self.lbl_mata_kuliah = ttk.Label(self.frame_tugas, text="Mata Kuliah:")
        self.lbl_mata_kuliah.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.ent_mata_kuliah = ttk.Entry(self.frame_tugas)
        self.ent_mata_kuliah.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Button untuk tambah tugas
        self.btn_tambah_tugas = ttk.Button(self.frame_tugas, text="Tambah Tugas", command=self.tambah_tugas)
        self.btn_tambah_tugas.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Button untuk update tugas
        self.btn_update_tugas = ttk.Button(self.frame_tugas, text="Update Tugas", command=self.update_tugas)
        self.btn_update_tugas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Button untuk hapus tugas
        self.btn_hapus_tugas = ttk.Button(self.frame_tugas, text="Hapus Tugas", command=self.hapus_tugas)
        self.btn_hapus_tugas.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Frame untuk aksi tambahan
        self.frame_aksi = ttk.LabelFrame(self.root, text="Menu")
        self.frame_aksi.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.lbl_kata_kunci = ttk.Label(self.frame_aksi, text="Kata Kunci Pencarian:")
        self.lbl_kata_kunci.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_kata_kunci = ttk.Entry(self.frame_aksi)
        self.ent_kata_kunci.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.lbl_cari_berdasarkan = ttk.Label(self.frame_aksi, text="Cari Berdasarkan:")
        self.lbl_cari_berdasarkan.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.cmb_cari_berdasarkan = ttk.Combobox(self.frame_aksi, values=["Mata Kuliah", "Nama Tugas", "ID"])
        self.cmb_cari_berdasarkan.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.cmb_cari_berdasarkan.set("Mata Kuliah")

        self.btn_cari_tugas = ttk.Button(self.frame_aksi, text="Cari Tugas", command=self.cari_tugas)
        self.btn_cari_tugas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.lbl_urutkan_berdasarkan = ttk.Label(self.frame_aksi, text="Urutkan Berdasarkan:")
        self.lbl_urutkan_berdasarkan.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.cmb_urutkan_berdasarkan = ttk.Combobox(self.frame_aksi, values=["Mata Kuliah", "ID"])
        self.cmb_urutkan_berdasarkan.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.btn_urutkan_tugas = ttk.Button(self.frame_aksi, text="Urutkan Tugas", command=self.urutkan_tugas)
        self.btn_urutkan_tugas.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Button untuk menampilkan tugas
        self.btn_lihat_tugas = ttk.Button(self.frame_aksi, text="Lihat Tugas", command=self.lihat_tugas)
        self.btn_lihat_tugas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def tambah_tugas(self):
        id_tugas = self.ent_id_tugas.get()
        nama_tugas = self.ent_nama_tugas.get()
        mata_kuliah = self.ent_mata_kuliah.get()
        
        try:
            tugas_baru = Tugas(id_tugas, nama_tugas, mata_kuliah)
            self.manajemen_tugas.tambah_tugas(tugas_baru)
            self.manajemen_tugas.simpan_tugas_ke_csv('tugas.csv')  # Menyimpan tugas ke dalam file CSV
            messagebox.showinfo("Info", "Tugas berhasil ditambahkan!")
            self.kosongkan_entry()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_tugas(self):
        id_tugas = self.ent_id_tugas.get()
        id_tugas_baru = self.ent_id_tugas.get()
        nama_tugas_baru = self.ent_nama_tugas.get()
        mata_kuliah_baru = self.ent_mata_kuliah.get()

        try:
            if self.manajemen_tugas.update_tugas(id_tugas, id_tugas_baru, nama_tugas_baru, mata_kuliah_baru):
                self.manajemen_tugas.simpan_tugas_ke_csv('tugas.csv')  # Menyimpan tugas ke dalam file CSV
                messagebox.showinfo("Info", "Tugas berhasil diupdate!")
            else:
                messagebox.showerror("Error", "ID Tugas tidak ditemukan!")
            self.kosongkan_entry()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def hapus_tugas(self):
        id_tugas = self.ent_id_tugas.get()
        if self.manajemen_tugas.hapus_tugas(int(id_tugas)):
            self.manajemen_tugas.simpan_tugas_ke_csv('tugas.csv')  # Menyimpan tugas ke dalam file CSV
            messagebox.showinfo("Info", "Tugas berhasil dihapus!")
        else:
            messagebox.showerror("Error", "ID Tugas tidak ditemukan!")
        self.kosongkan_entry()

    def cari_tugas(self):
        kata_kunci = self.ent_kata_kunci.get()
        berdasarkan = self.cmb_cari_berdasarkan.get()
        hasil_pencarian = self.manajemen_tugas.cari_tugas(kata_kunci, berdasarkan)

        view_window = tk.Toplevel(self.root)
        view_window.title("Hasil Pencarian Tugas")

        tree = ttk.Treeview(view_window, columns=("ID", "Nama Tugas", "Mata Kuliah"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nama Tugas", text="Nama Tugas")
        tree.heading("Mata Kuliah", text="Mata Kuliah")
        tree.pack(fill=tk.BOTH, expand=True)

        for tugas in hasil_pencarian:
            tree.insert("", tk.END, values=(tugas.id_tugas, tugas.nama_tugas, tugas.mata_kuliah))

    def urutkan_tugas(self):
        berdasarkan = self.cmb_urutkan_berdasarkan.get()
        self.manajemen_tugas.urutkan_tugas(berdasarkan)
        self.manajemen_tugas.simpan_tugas_ke_csv('tugas.csv')  # Menyimpan tugas ke dalam file CSV
        messagebox.showinfo("Info", "Tugas berhasil diurutkan!")
        self.lihat_tugas()

    def lihat_tugas(self):
        tugas = self.manajemen_tugas.tugas
        view_window = tk.Toplevel(self.root)
        view_window.title("Daftar Tugas")

        tree = ttk.Treeview(view_window, columns=("ID", "Nama Tugas", "Mata Kuliah"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nama Tugas", text="Nama Tugas")
        tree.heading("Mata Kuliah", text="Mata Kuliah")
        tree.pack(fill=tk.BOTH, expand=True)

        for tugas in tugas:
            tree.insert("", tk.END, values=(tugas.id_tugas, tugas.nama_tugas, tugas.mata_kuliah))

    def kosongkan_entry(self):
        self.ent_id_tugas.delete(0, tk.END)
        self.ent_nama_tugas.delete(0, tk.END)
        self.ent_mata_kuliah.delete(0, tk.END)
        self.ent_kata_kunci.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TugasGUI(root)
    root.mainloop()
