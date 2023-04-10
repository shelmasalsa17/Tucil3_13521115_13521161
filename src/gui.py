import tkinter as tk
from tkinter import filedialog
import networkx
import matplotlib.pyplot as plt
from Visualizer import *
from helper import *
from AStar import *
from pencarian import *

kamusBeban = {}
kamusKoordinat = {}
visited_nodes = []
shortPath = []
# Fungsi untuk membuka jendela dialog dan membaca file
def open_file_dialog():
    # Membuka jendela dialog untuk memilih file
    file_path = filedialog.askopenfilename()     
    if file_path:
        # Jika file dipilih, update teks tombol dengan nama file
        file_name = file_path.split("/")[-1]
        submit_button.config(text=file_name)
        # Memproses data dari file
        global kamusBeban, kamusKoordinat
        kamusBeban, kamusKoordinat = readFile(file_path)
        start_entry.delete(0, tk.END)
        goal_entry.delete(0, tk.END)


# Membuat fungsi untuk menampilkan grafik di GUI
def show_graph():
    start = start_entry.get()
    goal = goal_entry.get()
    try:
        shortPath, visited = UCS(kamusBeban, start, goal)
        membuatGraph(start, goal, shortPath, visited,kamusBeban, kamusKoordinat)
        shortpath_label.config(text=f"Shortest Path: {' -> '.join(shortPath)}")
        visited_label.config(text=f"Visited Nodes: {', '.join('({0}, {1})'.format(*row) for row in visited)}")
    except Exception as e:
        shortpath_label.config(text=f"Error: Periksa penulisan Start, goal dan file")
        visited_label.config(text=f"")

    # Update label untuk menampilkan jalur terpendek
def showASTAR_graph():
    start = start_entry.get()
    goal = goal_entry.get()
    try:
        # Memanggil fungsi Astar untuk mendapatkan jalur terpendek dan node yang dikunjungi
        shortPath, visited = Astar(start, goal, kamusBeban, kamusKoordinat)

        # Menampilkan grafik dengan memanggil fungsi membuatGraph dari modul Visualizer
        membuatGraph(start, goal, shortPath, visited, kamusBeban, kamusKoordinat)

        # Menampilkan hasil jalur terpendek dan node yang dikunjungi di GUI
        shortpath_label.config(text=f"Shortest Path: {' -> '.join(shortPath)}")
        visited_label.config(text=f"Visited Nodes: {', '.join('({0}, {1})'.format(*row) for row in visited)}")
    except Exception as e:
        # Menampilkan pesan error jika terjadi kesalahan saat proses pencarian jalur terpendek
        shortpath_label.config(text=f"Error: Periksa penulisan Start, goal dan file")
        visited_label.config(text=f"")


# Inisiasi
master = tk.Tk()
# Set judul window
master.title("Tucil 3 13521115, 13521161")

# Set ukuran window
master.geometry("800x600")

# Membuat canvas
canvas = tk.Canvas(master, width=800, height=600)
canvas.pack()

# Memuat gambar latar belakang
bg_image = tk.PhotoImage(file="img/bg.png", width=800, height=600)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Membuat tombol submit
submit_button = tk.Button(master, text="Pilih file", command=open_file_dialog, width=40)
submit_button.place(x=20, y=200)
shortpath_label = tk.Label(master, text="", font=("Arial", 12), bg="#f0f0f0", width=80,height=5)
shortpath_label.place(x=20, y=285)
visited_label = tk.Label(master, text="", font=("Arial", 8), bg="#f0f0f0", width=120, height=8)
visited_label.place(x=20, y=400)
# Label untuk menampilkan node yang dikunjungi
# Tombol UCS
ucs_button = tk.Button(master, text="UCS", width=20,bg="pink", command=show_graph)
ucs_button.place(x=320, y=200)


# Tombol A*
astar_button = tk.Button(master, text="A*", width=20,bg="pink", command=showASTAR_graph)
astar_button.place(x=480, y=200)


# Label start
start_label = tk.Label(master, text="Start Node", font=("Arial", 12), bg="#f0f0f0")
start_label.place(x=20, y=230)

# Field start
start_entry = tk.Entry(master, font=("Arial", 12))
start_entry.place(x=20, y=255, width=200)

# Label goal
goal_label = tk.Label(master, text="Goal Node", font=("Arial", 12), bg="#f0f0f0")
goal_label.place(x=320, y=230)

# Field goal
goal_entry = tk.Entry(master, font=("Arial", 12))
goal_entry.place(x=320, y=255, width=200)

# Menjalankan event loop
tk.mainloop()
