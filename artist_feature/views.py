from django.shortcuts import render
from .artist_tree import ArtistTree
from .feat_artists import FeaturedArtists


COLLECT_FEATURED_PERFORMERS = '1'
COLLECT_APPEARS_ON = '2'
COLLECT_APPEARS_ON_PERFORMERS = '3'



def index(request):
    if request.method == 'POST':
        options = request.POST.getlist('options')
        
        origin_artist = request.POST.get('search', None)
        
        if origin_artist:
            artist_tree = ArtistTree()
            search = FeaturedArtists(origin_artist)
            
            #origin_artist = search.artist_name
                        
            data = search.collectMainPerformersData()
            artist_tree.updateTreeFirstDegree(data)
            feat_performers = artist_tree.feat_performers
            #print(feat_performers)

            for num in options:
                if num == COLLECT_FEATURED_PERFORMERS:
                    
                    for artist in feat_performers:
                        #print(artist)
                        search = FeaturedArtists(artist)
                        data = search.collectMainPerformersData()
                        artist_tree.updateTreeSecondDegree(data)
                
                elif num == COLLECT_APPEARS_ON:
                    data = search.collectFeaturedPerformersData()
                    artist_tree.updateTreeSecondDegree(data)
                
                elif num == COLLECT_APPEARS_ON_PERFORMERS:
                    print(num)

            data = artist_tree.graphToJSON()
            resp = data
            return render(request, 'index.html', resp)
    
    return render(request, 'index.html', {})

