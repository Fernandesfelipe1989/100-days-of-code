import requests

from bs4 import BeautifulSoup

BASE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=BASE_URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all(name="h3", class_='title')
movies_title = [movie.getText() for movie in movies]

with open("movies.txt", 'w') as file:
    for movie in movies_title[::-1]:
        file.write(movie)
        file.write('\n')

print(movies_title)
