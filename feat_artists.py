import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas
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

    def collectData(self):
        album_Results = FeaturedArtists.spotifyObject.artist_albums(self.artist_id)
        albums = album_Results['items']
        
        
        tracks = [album['id'] for album in albums]
        data = tuple(map(self.collectSongs, tracks))

        data = [x for row in data for x in row]
        data = list(set(data))
        return(data)
        

    def getID(self):
        results = FeaturedArtists.spotifyObject.search(q='artist:' + self.artist_name, type='artist')
        results = results['artists']['items'][0]
        artist_id = results['id']
        return artist_id




