import os
from collections import defaultdict
from os.path import dirname, abspath

coordinate = defaultdict(dict)

def euclideanDistance(start, end):
    return round(((coordinate[start]["lat"] - coordinate[end]["lat"]) ** 2 + (
        coordinate[start]["lng"] - coordinate[end]["lng"]) ** 2) ** (0.5), 3)
    
def readFile():
    directory = dirname(dirname(abspath(__file__)))
    namaFile = str(input("Nama File tanpa ekstensi: "))
    location = os.path.join(directory, 'test\\' + namaFile + '.txt')
    f = open(location, "r")
    
    loadDictionary = defaultdict(dict)
    
    # Untuk memeperoleh list 
    listNode = f.readline().replace("\n", "").split(" ")
    countNode = len(listNode)
    
    location = f.readlines()
    kordinate = location[:location.index("MATRIKS\n")]
    for elements in kordinate:
        node = elements.replace("\n", "").split(" ")
        coordinate[node[0]]["lat"] = float(node[1])
        coordinate[node[0]]["lng"] = float(node[2])
        
    mat = []
    adjacent = location[location.index("MATRIKS\n") + 1:]
    for elementAdjacent in adjacent:
        elemen = elementAdjacent.replace("\n", "").split(" ")
        elemen = list(map(int, elemen))
        mat.append(elemen)
        
    for i in range(countNode):
        for j in range(countNode):
            if (mat[i][j] == 1):
                loadDictionary[listNode[i]][listNode[j]] = euclideanDistance(listNode[i], listNode[j])
    return loadDictionary