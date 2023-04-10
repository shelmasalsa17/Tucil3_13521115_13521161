import matplotlib.pyplot as plt
import networkx as nx
from helper import *
from pencarian import *
from AStar import *

def membuatGraph(start, goal, alur_terpendek, visited,kamusBeban, kamusKoordinat):
    try:
        # Inisialisasi Graph
        G = nx.Graph()
        # Initialize variables from PathFinder
        # Jarak
        distance_sum = 0
        for i in range(len(alur_terpendek) - 1):
            distance_sum += kamusBeban[alur_terpendek[i]][alur_terpendek[i + 1]]
        # Bentuk semua nodes
        for nodes in kamusBeban:
            G.add_node(nodes, pos=(kamusKoordinat[nodes]['lat'], kamusKoordinat[nodes]['long']))
        # Bentuk semua edges
        for nodes in kamusBeban:
            for children in kamusBeban[nodes]:
                G.add_edge(nodes, children, weight=kamusBeban[nodes][children])

        # Posisi
        pos = nx.get_node_attributes(G, 'pos')
        # Bobot
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        # Mewarnai node yang dikunjungi
        node_color = []
        if alur_terpendek:
            for node in G.nodes:
                node_color.append("blue")
            # Animasi penjelajahan semua node visited
            fig, ax = plt.subplots()
            for i in range(len(visited)):
                node = visited[i]
                node_color[i] = "red"
                nx.draw(G, pos, node_color=node_color, with_labels=True, node_size=1200, ax=ax)
                ax.set_title(f"Visiting {node}")
                fig.canvas.draw()
                plt.pause(0.5)
        else:
            print(f"Tidak ada lintasan dari {start} ke {goal}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


# Contoh penggunaan
#namaFile = str(input("Nama File tanpa ekstensi: "))
#test, kamus = readFile(namaFile)       
#start = str(input("start: "))
#end = str(input("end: "))
#shortPath, visited = UCS(test, start, end)
#membuatGraph(start, end, shortPath, test, kamus)
