from os import startfile
from AStar import loadDictionary
from Visualizer import *

while True:
    dictionary = loadDictionary
    arrayOfSimpul = [node for node in dictionary]
    
    print("Tempat-Tempat: ")
    num = 1
    for i in arrayOfSimpul:
        print(f"{num}. {i}")
        num += 1
        
    tempatAwal = str(input("Tempat Awal: "))
    while (tempatAwal not in arrayOfSimpul):
        print("Tempat awal tidak ditemukan")
        tempatAwal = str(input("Tempat Awal: "))

    tempatAkhir = str(input("Tempat Akhir: "))
    while (tempatAkhir not in arrayOfSimpul):
        print("Tempat akhir tidak ditemukan")
        tempatAkhir = str(input("tempat Akhir: "))

    break
        