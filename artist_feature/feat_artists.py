import spotipy
import json
import pandas
try:
    from .config import Creds
except:
    from config import Creds
    

class FeaturedArtists:
    client_credentials_manager = Creds().client_credentials_manager
    spotifyObject = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    def __init__(self, search_name):
        self.artist_name = search_name
        self.artist_id = self.getID()

        
    def artist_data(self, artists):
        artists = [artist['name'] for artist in artists if 'name' in artist]
        artists = tuple(artists)
        
        return(artists)

    def collectSongs(self, album_id):
        track_results = FeaturedArtists.spotifyObject.album_tracks(album_id)
        
        tracks = track_results['items']
    
        songs = [track['name'] for track in tracks]
        
        artists = [track['artists'] for track in tracks]
        
        artists = [self.artist_data(artist) for artist in artists]
        
        preview_urls = [track['preview_url'] for track in tracks]

        data = list(zip(songs, artists, preview_urls))
        return data
    
    def collectFeaturedPerformersData(self):
        album_Results = FeaturedArtists.spotifyObject.artist_albums(self.artist_id, album_type='appears_on')
        albums = album_Results['items']
        appears_on = [album for album in albums if album['album_group'] == 'appears_on']
        appears_on_tracks = [album['id'] for album in appears_on]
        
        appears_on_data = tuple(map(self.collectSongs, appears_on_tracks))
        
        data = []
        for songs in appears_on_data:
            for song in songs:
                if self.artist_name in song[1]:
                    data.append(song)
        
        data = list(set(data))
        return data


    def collectMainPerformersData(self):
        try:
            album_Results = FeaturedArtists.spotifyObject.artist_albums(self.artist_id)
            albums = album_Results['items']
            
            artist_albums = [album for album in albums if album['album_group'] != 'appears_on']
            tracks = [album['id'] for album in artist_albums]
            data = tuple(map(self.collectSongs, tracks))
            data = [x for row in data for x in row]
            
            ls = []
            for song in data:
                if self.artist_name in song[1]:
                    ls.append(song)
            
            
            data = list(set(ls))
            
            return(data)
        except Exception as e:
            return e
        

    def getID(self):
        try:
            results = FeaturedArtists.spotifyObject.search(q='artist:' + self.artist_name, type='artist')
            #if results['artists']['total'] !=0
            results = results['artists']['items'][0]
            artist_id = results['id']
            self.artist_name = results['name']
            return artist_id
        except Exception as e:
            return e

"""
parent_artist='Rex Orange County'

search = FeaturedArtists(parent_artist)
data = search.collectData(appears_on=True)
print(data)
"""
