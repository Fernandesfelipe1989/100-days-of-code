import datetime as dt
import requests

from decouple import config

API_KEY = config('API_KEY')
USER_ID = config('USER_ID')
BASE_URL = 'https://trackapi.nutritionix.com//v2/natural/exercise'
SHEET_BASE_URL = config('SHEET_BASE_URL')

headers_track = {
    'x-app-id': USER_ID,
    'x-app-key': API_KEY,
}
headers_sheet = {
    'Authorization': f"Bearer {config('SHEET_AUTH_TOKEN')}",
}

if __name__ == "__main__":
    exercise = input("Tell me which exercises you did: \n")
    exercise_info = {
        'query': exercise,
    }
    response = requests.post(url=BASE_URL, json=exercise_info, headers=headers_track)
    response.raise_for_status()
    exercises_data = response.json().get('exercises')
    today = dt.datetime.today()

    for exercise in exercises_data:
        exercise_parameters = {
            'sheet1': {
                'date': today.strftime("%d/%m/%Y"),
                'time': today.time().strftime('%H:%M:%S'),
                'exercise': exercise.get('name').title(),
                'duration': exercise.get('duration_min'),
                'calories': exercise.get('nf_calories'),
            },
        }
        response = requests.post(url=SHEET_BASE_URL, json=exercise_parameters, headers=headers_sheet)
        response.raise_for_status()
        print(response.text)
