import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x600")
root.configure(bg="navy")
root.resizable(False, False)

# Warna aplikasi
biru = "navy"
biru_muda = "steelblue"
putih = "white"

# Label judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 15, "bold"),
    bg=biru,
    fg=putih
)
judul.pack(pady=20)

# Frame untuk input nilai
frame = tk.Frame(root, bg=biru)
frame.pack(padx=15)

