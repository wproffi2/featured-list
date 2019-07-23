from django.shortcuts import render
from .artist_tree import ArtistTree
from .feat_artists import FeaturedArtists


def index(request):
    if request.method == 'POST':
        appears_on = request.POST.getlist('appears_on')
        
        parent_artist = request.POST.get('textfield', None)
        
        if parent_artist:
            if appears_on != ['1']:
                artist_tree = ArtistTree()
                search = FeaturedArtists(parent_artist)
                data = search.collectData()
                artist_tree.updateTree(parent_artist, data)
                data = artist_tree.graphToJSON()
            else:
                artist_tree = ArtistTree()
                search = FeaturedArtists(parent_artist)
                data = search.collectData(appears_on=True)
                artist_tree.updateTree(parent_artist, data)
                data = artist_tree.graphToJSON()
            
            resp = data
            return render(request, 'index.html', resp)
    
    return render(request, 'index.html', {})

