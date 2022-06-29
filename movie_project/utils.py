from datetime import datetime as dt
import requests
from typing import Dict, List
from decouple import config


class MovieAPI:
    AUTH_TOKEN = config("AUTH_TOKEN")
    BASE_URL = config("BASE_URL")
    IMAGE_URL = config('IMAGE_URL')
    HEADERS = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8',
    }

    def api_request(self, endpoint, params: dict = None):
        parameters = {
            'api_key': self.AUTH_TOKEN,
        }
        if isinstance(params, dict):
            parameters = dict(parameters, **params)

        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url=url, params=parameters)
        print(response.url)
        response.raise_for_status()
        return response.json()

    def search_movie(self, title: str) -> List[Dict]:
        endpoint = 'search/movie'
        movies = []
        parameters = {
            'query': title,
        }
        data = self.api_request(endpoint=endpoint, params=parameters)
        for movie in data['results']:
            movie_info = dict(
                title=movie.get("title"),
                release_date=movie.get("release_date"),
                id=movie.get('id'),
            )

            movies.append(movie_info)
        return movies

    def get_movie(self, id):
        endpoint = f"movie/{id}"
        data = self.api_request(endpoint=endpoint)
        movie = dict(
            title=data.get('title'),
            img_url=f'{self.IMAGE_URL}{data.get("poster_path")}',
            year=data.get('release_date', "").split("-")[0],
            description=data.get("overview")
        )
        return movie


if __name__ == "__main__":
    print(MovieAPI().search_movie(title="The Matrix"))
    print(MovieAPI().get_movie(id=157336))
