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
        
        artists = [artist[1:] for artist in artists]
        
        artists = [self.artist_data(artist) for artist in artists]
        
        data = list(zip(songs, artists))
        return data

    def collectAppearsOnSongs(self, album_id):
        track_results = FeaturedArtists.spotifyObject.album_tracks(album_id)
        tracks = track_results['items']
        
        songs = [track['name'] for track in tracks]
        
        artists = [track['artists'] for track in tracks]
        
        #artists = [artist[1:] for artist in artists]
        
        artists = [self.artist_data(artist) for artist in artists]
        
        data = list(zip(songs, artists))
        return data
    
    def collectData(self, appears_on=False):
        album_Results = FeaturedArtists.spotifyObject.artist_albums(self.artist_id)
        albums = album_Results['items']
        
        artist_albums = [album for album in albums if album['album_group'] != 'appears_on']
        tracks = [album['id'] for album in artist_albums]
        data = tuple(map(self.collectSongs, tracks))
        
        if appears_on:
            appears_on = [album for album in albums if album['album_group'] == 'appears_on']
            appears_on_tracks = [album['id'] for album in appears_on]
            appears_on_data = tuple(map(self.collectAppearsOnSongs, appears_on_tracks))
            ls = []
            for songs in appears_on_data:
                
                for song in songs:
                    if self.artist_name in song[1]:
                        ls.append(song)
            ls = list(set(ls))
            
            appears_on_data = []
            for song in ls:
                x = tuple(filter(lambda a: a!=self.artist_name, song[1]))
                appears_on_data.append((song[0], x))

        
        data = [x for row in data for x in row]
        if appears_on:
            data = data + appears_on_data
            #merge data and appears_on_data

        data = list(set(data))
        return(data)
        

    def getID(self):
        results = FeaturedArtists.spotifyObject.search(q='artist:' + self.artist_name, type='artist')
        results = results['artists']['items'][0]
        artist_id = results['id']
        return artist_id

"""
parent_artist='Rex Orange County'

search = FeaturedArtists(parent_artist)
data = search.collectData(appears_on=True)
print(data)
"""
