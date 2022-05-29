import requests
from re import sub

from bs4 import BeautifulSoup
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

track_id = '6y0igZArWVi6Iz0rj35c1Y'

r = requests.get(SPOTIFY_BASE_URL + 'audio-features/' + track_id, headers=SPOTIFY_HEADER)
