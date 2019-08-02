import spotipy
from artist_feature.config import Creds

client_credentials_manager = Creds().client_credentials_manager
spotifyObject = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song = spotifyObject.album_tracks('4GNIhgEGXzWGAefgN5qjdU')
print(song)