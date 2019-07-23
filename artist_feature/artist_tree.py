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
        self.tree.add_node(parent_artist, type='parent_artist')
        #self.color_map.append('green')

        for x in data:
            song, artists = x[0], list(x[1])
            self.tree.add_node(song, type='song')
            
            
            self.tree.add_edge(parent_artist, song)

            for artist in artists:
                self.tree.add_node(artist, type='feat_artist')
                
                self.tree.add_edge(song, artist)

        return 0


