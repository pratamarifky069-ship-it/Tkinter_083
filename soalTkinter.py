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

# Menyimpan input nilai
inputs = []

# Membuat 10 input nilai mata pelajaran
for i in range(10):
    label = tk.Label(
        frame,
        text=f"Nilai Mata Pelajaran {i + 1}:",
        font=("Arial", 10, "bold"),
        bg=biru,
        fg=putih,
        width=21,
        anchor="e"
    )
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(
        frame,
        width=15,
        bg=biru_muda,
        fg=putih,
        insertbackground=putih
    )
    entry.grid(row=i, column=1, padx=5, pady=5)

    inputs.append(entry)

# Fungsi hasil prediksi
def hasil_prediksi():

