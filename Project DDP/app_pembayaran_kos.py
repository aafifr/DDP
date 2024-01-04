import tkinter as tk
from tkinter import ttk, messagebox
import locale
from ttkbootstrap import Style

class SistemPembayaranSewa:
    def __init__(self):
        self.nama_penyewa = ""
        self.biaya_sewa = 0
        self.diskon = 0
        self.pembayaran_diterima = 0
        self.lama_sewa = 0
        self.kelas_sewa = ""
        self.metode_pembayaran = ""

    def hitung_biaya_sewa(self, biaya_bulanan, persentase_diskon):
        diskon = (persentase_diskon / 100) * biaya_bulanan
        self.diskon = min(diskon, biaya_bulanan)  
        self.biaya_sewa = biaya_bulanan - self.diskon
        return self.biaya_sewa, self.diskon

    def terima_pembayaran(self, jumlah_dibayar):
        self.pembayaran_diterima = jumlah_dibayar
        return self.pembayaran_diterima

    def hitung_kembalian(self):
        return self.pembayaran_diterima - self.biaya_sewa

class AplikasiPembayaranSewa:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistem Pembayaran Sewa")
        self.style = Style("vapor")
        self.sistem_sewa = SistemPembayaranSewa()
        locale.setlocale(locale.LC_NUMERIC, 'id_ID')
        self.buat_widget()

    def buat_widget(self):
        tk.Label(self.master, text="Nama Penyewa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nama_entry = tk.Entry(self.master)
        self.nama_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Lama Sewa (maks 1 bulan):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lama_entry = tk.Entry(self.master)
        self.lama_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Kelas Sewa:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.kelas_combo = ttk.Combobox(self.master, values=["Eksekutif", "Bisnis", "Ekonomi"])
        self.kelas_combo.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Metode Pembayaran:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.metode_combo = ttk.Combobox(self.master, values=["Cash", "Kredit"])
        self.metode_combo.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Biaya Bulanan:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.biaya_entry = tk.Entry(self.master, state="readonly", justify="right")
        self.biaya_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Diskon (%):").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.diskon_entry = tk.Entry(self.master, state="readonly")
        self.diskon_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Button(self.master, text="Hitung Pembayaran", command=self.hitung_pembayaran).grid(row=6, column=0, columnspan=2, pady=10)

        self.kelas_combo.bind("<<ComboboxSelected>>", self.perbarui_biaya_dan_diskon)

        self.tengah_kan_antarmuka()

    def hitung_pembayaran(self):
        try:
            nama_penyewa = self.nama_entry.get()
            lama_sewa = int(self.lama_entry.get())
            kelas_sewa = self.kelas_combo.get().lower()
            metode_pembayaran = self.metode_combo.get().lower()

            if lama_sewa > 1:
                messagebox.showerror("Error", "Lama sewa maksimal adalah 1 bulan.")
                return

            self.sistem_sewa.nama_penyewa = nama_penyewa
            self.sistem_sewa.lama_sewa = lama_sewa
            self.sistem_sewa.kelas_sewa = kelas_sewa
            self.sistem_sewa.metode_pembayaran = metode_pembayaran

            biaya_bulanan, persentase_diskon = self.atur_biaya_dan_diskon(kelas_sewa)

            biaya_sewa, diskon = self.sistem_sewa.hitung_biaya_sewa(biaya_bulanan, persentase_diskon)

            detail_pembayaran = f"Penyewa: {nama_penyewa}\nLama Sewa: {lama_sewa} bulan\nKelas Sewa: {kelas_sewa.capitalize()}\nMetode Pembayaran: {metode_pembayaran.capitalize()}\nBiaya Bulanan: {locale.currency(biaya_bulanan, grouping=True)}\nDiskon: {diskon}\nTotal Pembayaran: {locale.currency(biaya_sewa, grouping=True)}"
            messagebox.showinfo("Detail Pembayaran", detail_pembayaran)

        except ValueError:
            messagebox.showerror("Error", "Input tidak valid. Harap masukkan angka yang valid untuk Lama Sewa dan Diskon.")

    def perbarui_biaya_dan_diskon(self, event):
        kelas_sewa = self.kelas_combo.get().lower()
        biaya_bulanan, persentase_diskon = self.atur_biaya_dan_diskon(kelas_sewa)

        self.biaya_entry.config(state="normal")
        self.biaya_entry.delete(0, tk.END)
        self.biaya_entry.insert(0, locale.currency(biaya_bulanan, grouping=True))
        self.biaya_entry.config(state="readonly")

        self.diskon_entry.config(state="normal")
        self.diskon_entry.delete(0, tk.END)
        self.diskon_entry.insert(0, persentase_diskon)
        self.diskon_entry.config(state="readonly")

    def atur_biaya_dan_diskon(self, kelas_sewa):
        if kelas_sewa == "eksekutif":
            biaya_bulanan = 2100000
            persentase_diskon = 10
        elif kelas_sewa == "bisnis":
            biaya_bulanan = 1500000
            persentase_diskon = 8
        elif kelas_sewa == "ekonomi":
            biaya_bulanan = 900000
            persentase_diskon = 5
        else:
            messagebox.showerror("Error", "Kelas sewa tidak valid. Pilih antara Eksekutif, Bisnis, atau Ekonomi.")
            raise ValueError("Kelas sewa tidak valid.")

        return biaya_bulanan, persentase_diskon

    def tengah_kan_antarmuka(self):
        lebar_window = self.master.winfo_reqwidth()
        tinggi_window = self.master.winfo_reqheight()
        x_tengah = (self.master.winfo_screenwidth() // 4) - (lebar_window // 120)
        y_tengah = (self.master.winfo_screenheight() // 4) - (tinggi_window // 75)
        self.master.geometry(f"+{x_tengah}+{y_tengah}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPembayaranSewa(root)
    root.mainloop()