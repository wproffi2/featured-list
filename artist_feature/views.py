from django.shortcuts import render
from .artist_tree import ArtistTree
from .feat_artists import FeaturedArtists


def index(request):
    if request.method == 'POST':
        options = request.POST.getlist('options')
        
        origin_artist = request.POST.get('search', None)
        
        if origin_artist:
            #artist_tree = ArtistTree()
            for num in options:
                print(num)
            
            #"""
            if 2 in options:
                artist_tree = ArtistTree()
                search = FeaturedArtists(origin_artist)
                data = search.collectData(appears_on=True)
                artist_tree.updateTree(data)
                data = artist_tree.graphToJSON()

            else:
                artist_tree = ArtistTree()
                
                search = FeaturedArtists(origin_artist)
                data = search.collectData()
                
                artist_tree.updateTree(data)
                data = artist_tree.graphToJSON()
            #"""
            
            
            resp = data
            return render(request, 'index.html', resp)
    
    return render(request, 'index.html', {})

