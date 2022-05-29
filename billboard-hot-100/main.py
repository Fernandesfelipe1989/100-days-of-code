import requests
from re import sub

import spotipy
from bs4 import BeautifulSoup
from decouple import config
from spotipy import SpotifyOAuth

SUB_PATTERN = r'[\n\t]'
BASE_URL = 'https://www.billboard.com/charts/hot-100/'
SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/'
REDIRECT_URI = config('REDIRECT_URI')
SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_SCOPES = config('SPOTIFY_SCOPES')
SPOTIFY_GRANT_TYPE = config('SPOTIFY_GRANT_TYPE')

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")

url = f'{BASE_URL}{date}/'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
song_titles = soup.select("li ul li h3")
top_100_songs = [sub(pattern=SUB_PATTERN, string=song_title.getText(), repl="") for song_title in song_titles]

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SPOTIFY_CLIENT_ID,
    'client_secret': SPOTIFY_CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

SPOTIFY_HEADER = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
TRACK_SEARCH = f'{SPOTIFY_BASE_URL}search'
parameters = {
    'type': 'track',
    'limit': 1,
    'q': ""
}
top_100_songs_uri = []
for song in top_100_songs:
    parameters['q'] = song
    response = requests.get(url=TRACK_SEARCH, params=parameters, headers=SPOTIFY_HEADER)
    try:
        response.raise_for_status()
    except:
        pass
    else:
        track_info = response.json()
        track = track_info.get('tracks')
        track = track and track.get('items')
        if track:
            track_uri = track[0].get('uri')
            top_100_songs_uri.append(track_uri)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SPOTIFY_SCOPES,
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=top_100_songs_uri)
