# Find The Shortest Path
Disusun untuk memenuhi Tugas Kecil 3 IF2211 Strategi Algoritma "Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan terpendek"

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Struktur Program](#struktur-program)
* [Requirement Program](#requirement-program)
* [Cara Menyiapkan *Environment*](#cara-menyiapkan-environment)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Cara Menggunakan Program](#cara-menggunakan-program)
* [Author](#author)

## Deskripsi Singkat Program
Algoritma UCS (*Uniform cost search*) dan A* (atau *A star*) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, anda diminta menentukan lintasan terpendek berdasarkan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan di peta dibentuk graf. Simpul menyatakan persilangan jalan (simpang 3, 4 atau 5) atau ujung jalan. Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul. Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara lainnya yang disediakan oleh Google Map. Langkah pertama di dalam program ini adalah membuat graf yang merepresentasikan peta (di area tertentu, misalnya di sekitar Bandung Utara/Dago). Berdasarkan graf yang dibentuk, lalu program menerima input simpul asal dan simpul tujuan, lalu menentukan lintasan terpendek antara keduanya menggunakan algoritma UCS dan A*. Lintasan terpendek dapat ditampilkan pada peta/graf (misalnya jalan-jalan yang menyatakan lintasan terpendek diberi warna merah). Nilai heuristik yang dipakai adalah jarak garis lurus dari suatu titik ke tujuan.
## Struktur Program
```bash
.
│   README.md
│   
├───bin
│       run.bat
│ 
├───doc
│       Tucil3_13521115_13521161.pdf
│  
├───img
│      bg.png
│
├───src
│   │   AStar.py
│   │   Visualizer.py
│   │   gui.py
│   │   helper.py
│   │   pencarian.py
│   │   
│   ├───__pycache__
│             AStar.cpython-310.pyc
│             A_star.cpython-310.pyc
│             Visualizer.cpython-310.pyc
│             helper.cpython-310.pyc
│             helperAstar.cpython-310.pyc
│             pencarian.cpython-310.pyc
│             priority_queue.cpython-310.pyc
│              
│
└───test
        alun2.txt
        buahbatu.txt
        garut.txt
        itb.txt
        klaten.txt
```

## Requirement Program
* Python versi 3.8.5 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.
* NumPy versi 1.22.3 atau lebih baru.
* Tkinter versi 0.1.0 atau lebih baru.
* Networkx versi 3.1 atau lebih baru.
* Matplotlib versi 3.7.1 atau lebih baru.


## Cara Menyiapkan *Environment*
1. Pastikan Python versi 3.8.5 atau lebih baru sudah terpasang pada komputer (Anda dapat mengecek versi Python dengan menjalankan *command* `py --version` pada *command prompt*).
2. Lakukan instalasi semua *library* yang digunakan pada program.
3. Jika seluruh *library* berhasil diinstalasi, maka akan terdapat pemberitahuan pada *command prompt*.

## Cara Menjalankan Program
1. Pastikan sudah menyiapkan *environment* program serta mesin eksekusi terhubung dengan internet.
2. Jalankan program `gui.py` dengan menjalankan perintah `py gui.py` pada *command prompt* pada folder `src`.
3. Untuk mempermudah bisa membuka file .exe di folder bin dan klik file tersebut.
4. Jika berhasil dijalankan, maka akan terdapat *window* Python pada komputer.

## Cara Menggunakan Program
1. *Upload* file `.txt` sesuai dengan format yang terdapat pada folder `test`.
2. Masukkan *Start Node* yaitu tempat awal sesuai yang ada di file terpilih dan *Goal Node* yaitu tempat yang akan dikunjungi. 
3. Tekan tombol *UCS* atau A* pada program.
4. Tunggu hingga program berhasil menemukan jawaban dari *UCS* atau A*.
5. Kemudian, program akan menunjukkan *Shortest Path* yang menunjukkan simpul yang dikunjungi untuk mendapatkan lintasan terpendek dan *Visited Nodes* yang menunjukkan simpul mana saja yang telah dikunjungi.

## Authors

| Nama                  | NIM      |
| --------------------- | -------- |
| Shelma Salsabila | 13521115 |
| Ferindya Aulia Berlianty | 13521161 |
