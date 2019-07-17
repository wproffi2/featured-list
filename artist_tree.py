import networkx as nx
from feat_artists import FeaturedArtists
import matplotlib.pyplot as plt


class ArtistTree:
    def __init__(self):
        self.tree = nx.Graph()
        self.color_map = []
    
    def display(self):
        #nx.draw(self.tree, node_color = self.color_map, with_labels=True)
        nx.draw(self.tree, with_labels=True)
        plt.show()

    def updateTree(self, parent_artist, data):
        self.tree.add_node(parent_artist)
        #self.color_map.append('green')

        for x in data:
            song, artists = x[0], list(x[1])
            self.tree.add_node(song)
            #self.color_map.append('blue')

            self.tree.add_edge(parent_artist, song)

            for artist in artists:
                self.tree.add_node(artist)
                #self.color_map.append('green')
                self.tree.add_edge(song, artist)

        
        return 0


artists = ['Tyler, The Creator', "Rex Orange County", "Jaden", "Kid Cudi"] #'A$AP Rocky'
test = ArtistTree()
for artist in artists:
    parent_artist = artist
    search = FeaturedArtists(parent_artist)
    data = search.collectData()
    test.updateTree(parent_artist, data)

test.display()

