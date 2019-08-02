from django.shortcuts import render
from django.http import HttpResponse
from .artist_tree import ArtistTree
from .feat_artists import FeaturedArtists


COLLECT_FEATURED_PERFORMERS = '1'
COLLECT_APPEARS_ON = '2'
COLLECT_APPEARS_ON_PERFORMERS = '3'



def index(request):
    if request.method == 'POST':
        options = request.POST.getlist('options')
        
        origin_artist = request.POST.get('search', None)
        print(origin_artist)
        
        if origin_artist:
            artist_tree = ArtistTree()
            search = FeaturedArtists(origin_artist)
                        
            data = search.collectMainPerformersData()
            if type(data) == list:
                artist_tree.updateTreeFirstDegree(data)
                feat_performers = artist_tree.feat_performers

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

            else:
                return HttpResponse(str(data))
    
    return render(request, 'index.html', {})

