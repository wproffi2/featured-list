import networkx as nx
from feat_artists import FeaturedArtists
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(20,0.1)
color_map = []
for node in G:
    if node <10:
        color_map.append('blue')
    else: color_map.append('green')      
nx.draw(G,node_color = color_map,with_labels = True)
plt.show()