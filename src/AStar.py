from helper import *

def makeHeuristicDict(goal, loadDictionary):
    heuristicValue = dict()
    for nodes in loadDictionary:
        heuristicValue[nodes] = eucleudianDistance(nodes, goal,coordinateDictionary)
    return heuristicValue

#Pencarian dengan algoritma A*
def A_star(loadDictionary, start, goal):
    # inisialisasi variabel
    heuristicValue = makeHeuristicDict(goal,loadDictionary)
    weight = {start: 0}
    simpulnotVisited = []
    visited = []
    curr = start
    simpulnotVisited.append([curr, weight[curr]])
    isTrue = True

    # algoritma A*
    while isTrue:
        curr = min(simpulnotVisited, key=lambda x: x[1])
        hasVisited = curr[0]
        print(curr)
        visited.append(curr)
        simpulnotVisited.remove(curr)
        if visited[-1][0] == goal:
            isTrue = False
            #Mengecek apakah simpul sudah dikunjungi, jika sudah akan dilewat
        for i in loadDictionary[hasVisited].items():
            if i[0] in [j[0] for j in visited]:
                continue
            weight.update({i[0]: weight[hasVisited] + i[1]})
            weight[i[0]] = weight[hasVisited] + heuristicValue[i[0]] + i[1]
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


#main ASTAR
#namaFile = str(input("Nama File tanpa ekstensi: "))
test = readFile("test/itb.txt")          
print(test)
start = str(input("start: "))
end = str(input("end: "))
shortPath = A_star(test,start,end)
print(shortPath)

