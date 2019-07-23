import networkx as nx
from networkx.readwrite import json_graph
import json
import matplotlib.pyplot as plt
try:
    from .feat_artists import FeaturedArtists
except:
    from feat_artists import FeaturedArtists

#pls work
class ArtistTree:
    def __init__(self):
        self.tree = nx.Graph()
        self.color_map = []
    
    def display(self):
        #nx.draw(self.tree, node_color = self.color_map, with_labels=True)
        nx.draw(self.tree, with_labels=True)
        plt.show()

    def graphToJSON(self):
        data = json_graph.node_link_data(self.tree)
        #with open('graph.json', 'w') as f:
            #json.dump(data, f, indent=4)
        json.dumps(data)
        return data

    def updateTree(self, parent_artist, data):
        self.tree.add_node(parent_artist, type=0)
        #self.color_map.append('green')

        for x in data:
            song, artists = x[0], list(x[1])
            self.tree.add_node(song, type=1)
            
            
            self.tree.add_edge(parent_artist, song)

            for artist in artists:
                self.tree.add_node(artist, type=2)
                
                self.tree.add_edge(song, artist)

        return 0


