import networkx as nx
from feat_artists import FeaturedArtists
import matplotlib.pyplot as plt


parent_artist = 'Tyler, The Creator'
search = FeaturedArtists(parent_artist)
data = search.collectData()
G = nx.Graph()
G.add_node(parent_artist)
for x in data:
    song, artists = x[0], list(x[1])
    G.add_node(song)
    G.add_edge(parent_artist, song)

    for artist in artists:
        G.add_node(artist)
        G.add_edge(song, artist)

nx.draw(G)
plt.show()