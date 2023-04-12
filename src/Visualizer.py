import matplotlib.pyplot as plt
import networkx as nx
from helper import *
from pencarian import *
from AStar import *

def membuatGraph(start, goal, alur_terpendek, visited, kamusBeban, kamusKoordinat):
    try:
        # Inisialisasi Graph
        G = nx.Graph()

        # Bentuk semua nodes
        for nodes in kamusBeban:
            G.add_node(nodes, pos=(kamusKoordinat[nodes]['lat'], kamusKoordinat[nodes]['long']))

        # Bentuk semua edges
        for nodes in kamusBeban:
            for children in kamusBeban[nodes]:
                G.add_edge(nodes, children, weight=kamusBeban[nodes][children])

        # Animasi penjelajahan semua node visited
        fig, ax = plt.subplots()
        for i in range(len(visited)):
            node = visited[i]
            node_color = ["blue" if n == node or n in alur_terpendek else "red" for n in G.nodes]
            nx.draw(G, nx.get_node_attributes(G, 'pos'), node_color=node_color, with_labels=True, node_size=1200, ax=ax)
            ax.set_title(f"Visiting {node}")
            fig.canvas.draw()
            plt.pause(0.5)

        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
