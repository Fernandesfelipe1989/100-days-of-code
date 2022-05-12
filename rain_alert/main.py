import requests

from decouple import config

API_KEY = config('API_KEY')
BASE_URL = config('BASE_URL')

if __name__ == "__main__":
    parameters = {
        'lat': -23.482050,
        'lon': -47.414291,
        'appid': API_KEY,
    }
    response = requests.get(url=BASE_URL, params=parameters)
    print(response.json())
