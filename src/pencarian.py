from helper import *
#Pencarian dengan algoritma UCS 
def UCS(loadDictionary, start, goal):
    try:
        # penanganan eksepsi untuk simpul start dan goal
        if start not in loadDictionary or goal not in loadDictionary:
            raise ValueError("Start atau goal tidak ada dalam graf")

        # inisialisasi variabel
        weight = {start: 0}
        simpulnotVisited = []
        visited = []
        curr = start
        simpulnotVisited.append([curr, weight[curr]])
        isTrue = True

        # algoritma UCS
        while isTrue:
            curr = min(simpulnotVisited, key=lambda x: x[1])
            hasVisited = curr[0]
            #print(curr)
            visited.append(curr)
            simpulnotVisited.remove(curr)
            if visited[-1][0] == goal:
                isTrue = False
            #Mengecek apakah simpul sudah dikunjungi, jika sudah akan dilewat
            for i in loadDictionary[hasVisited].items():
                if i[0] in [j[0] for j in visited]:
                    continue
                weight[i[0]] = weight[hasVisited] + i[1]
                simpulnotVisited.append([i[0], weight[i[0]]])

        # membangun jalur terpendek
        shortPath = []
        lastPath = goal
        shortPath.append(goal)
        for i in range(len(visited) - 2, -1, -1):
            check = visited[i][0]
            if lastPath in [k[0] for k in loadDictionary[check].items()]:
                if weight[check] + loadDictionary[check][lastPath] == weight[lastPath]:
                    shortPath.append(check)
                    lastPath = check
        shortPath.reverse()
        return shortPath, visited
        
    except ValueError as e:
        print("Error: " + str(e))
        
    except:
        print("Error : Coba Pastikan file dapat dibaca")

    
            
#main UCS 
#namaFile = str(input("Nama File tanpa ekstensi: "))
#test = readFile(namaFile)          
#print(test)
#start = str(input("start: "))
#end = str(input("end: "))
#shortPath = UCS(test,start,end)
#print(shortPath)