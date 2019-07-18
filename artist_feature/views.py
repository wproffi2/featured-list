from django.shortcuts import render
from .artist_tree import ArtistTree
from .feat_artists import FeaturedArtists


def index(request):
    if request.method == 'POST':
        parent_artist = request.POST.get('textfield', None)
        
        if parent_artist:
            artist_tree = ArtistTree()
            search = FeaturedArtists(parent_artist)
            data = search.collectData()
            artist_tree.updateTree(parent_artist, data)
            data = artist_tree.graphToJSON()
            #artist_tree.display()
            
            resp = data
            return render(request, 'index.html', resp)
    
    return render(request, 'index.html', {})

