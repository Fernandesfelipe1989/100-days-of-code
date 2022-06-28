import requests
from typing import Dict, List
from decouple import config


class MovieAPI:
    AUTH_TOKEN = config("AUTH_TOKEN")
    BASE_URL = config("BASE_URL")
    HEADERS = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json;charset=utf-8',
    }

    def api_request(self, parameters):
        response = requests.get(url=self.BASE_URL, params=parameters)
        response.raise_for_status()
        return response.json()

    def search_movie(self, title: str) -> List[Dict]:
        movies = []
        parameters = {
            'query': title,
            'api_key': self.AUTH_TOKEN,
        }
        data = self.api_request(parameters=parameters)
        for movie in data['results']:
            movie_info = dict(
                title=movie.get("title"),
                release_date=movie.get("release_date"),
                description=movie.get('overview'),
                rating=movie.get("vote_average"),
            )

            movies.append(movie_info)
        return movies


if __name__ == "__main__":
    print(MovieAPI().search_movie(title="The Matrix"))
