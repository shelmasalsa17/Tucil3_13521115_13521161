from helper import *
#Pencarian dengan algoritma UCS 
def UCS(loadDictionary, start, goal):
    weight = {start : 0}   #Bobot yang selalu di update 
    simpulnotVisited = []
    visited = []
    curr = start 
    simpulnotVisited.append([curr,weight[curr]])
    isTrue = True
    while isTrue:
        curr = min(simpulnotVisited, key=lambda x: x[1])
        hasVisited = curr[0]
        visited.append(curr)
        simpulnotVisited.remove(curr)
        #Jika sampai goal 
        if(visited[-1][0] == goal):
            isTrue = False
        #Memeriksa apakah simpul anak sudah dikunjungi sebelumnya
        for i in loadDictionary[hasVisited].items():
            if i[0] in [j[0] for j in visited]:
                continue
            weight[i[0]] = weight[hasVisited] + i[1]
            simpulnotVisited.append([i[0], weight[i[0]]])
    shortPath = []
    lastPath = goal 
    shortPath.append(goal)
    for i in range(len(visited) - 2, -1, -1):
        check = visited[i][0]
        if lastPath in [k[0] for k in loadDictionary[check].items()]:
            if (weight[check] + loadDictionary[check][lastPath] == weight[lastPath]):
                shortPath.append(check)
                lastPath = check
    shortPath.reverse()
    return shortPath

    
            
#main UCS 
namaFile = str(input("Nama File tanpa ekstensi: "))
test = readFile(namaFile)          
print(test)
start = str(input("start: "))
end = str(input("end: "))
shortPath = UCS(test,start,end)
print(shortPath)



