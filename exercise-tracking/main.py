import requests

from decouple import config

API_KEY = config('API_KEY')
USER_ID = config('USER_ID')
BASE_URL = 'https://trackapi.nutritionix.com//v2/natural/exercise'
headers = {
    'x-app-id': USER_ID,
    'x-app-key': API_KEY,
}

if __name__ == "__main__":
    exercise = input("Tell me which exercises you did: \n")
    exercise_info = {
        'query': exercise,
    }
    response = requests.post(url=BASE_URL, json=exercise_info, headers=headers)
    response.raise_for_status()
    print(response.json())

