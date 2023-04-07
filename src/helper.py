import os
from collections import defaultdict
from os.path import dirname, abspath
def eucleudianDistance(nodeAwal, nodeAkhir, coordinateDictionary):
    distance = round(((coordinateDictionary[nodeAwal]["lat"] - coordinateDictionary[nodeAkhir]["lat"]) ** 2 
    + (coordinateDictionary[nodeAwal]["long"] - coordinateDictionary[nodeAkhir]["long"]) ** 2) ** (0.5), 3)
    return distance
def readFile(namaFile):
    #inisialisasi awal 
    coordinate = defaultdict(dict)
    weightDictionary = defaultdict(dict)
    #Baca File
    dir = dirname(dirname(abspath(__file__)))
    lokasiFile = os.path.join(dir, 'test\\' + namaFile + '.txt')
    f = open(lokasiFile, "r")
    #Mendapatkan list Seluruh Simpul 
    listOfSimpul =  f.readline().replace("\n", "").split(" ")
    nOfSimpul = len(listOfSimpul)
    #Membentuk kamus kordinat 
    location = f.readlines()
    kordinate = location[:location.index("MATRIKS\n")]
    for elem in kordinate: 
        node = elem.replace("\n", "").split(" ")
        coordinate[node[0]]["lat"] = float(node[1])
        coordinate[node[0]]["long"] = float(node[2])
    #Mengurus Adjacent Matriks
    mat = []
    Adjacent = location[location.index("MATRIKS\n") + 1:]
    for elemenAdjacency in Adjacent:
        elemen = elemenAdjacency.replace("\n", "").split(" ")
        elemen = list(map(int, elemen))
        mat.append(elemen)
    for i in range(nOfSimpul):
        for j in range(nOfSimpul):
            if(mat[i][j] == 1):
                weightDictionary[listOfSimpul[i]][listOfSimpul[j]] = eucleudianDistance(listOfSimpul[i], listOfSimpul[j], coordinate)

    return weightDictionary

#TesFile
#namaFile = str(input("Nama File tanpa ekstensi: "))
#test = readFile(namaFile)          
#print(test)
