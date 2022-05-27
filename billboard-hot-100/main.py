import requests
from re import sub

from bs4 import BeautifulSoup

SUB_PATTERN = r'[\n\t]'
BASE_URL = 'https://www.billboard.com/charts/hot-100/'

SPOTIFY_HEADER = ""
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")

url = f'{BASE_URL}{date}/'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
song_titles = soup.select("li ul li h3")
top_100_songs = [sub(pattern=SUB_PATTERN, string=song_title.getText(), repl="") for song_title in song_titles]
print(top_100_songs)
