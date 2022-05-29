import requests

from decouple import config

TOKEN = config('SHEET_TOKEN')
BASE_URL = config("SHEET_BASE_URL")


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self, token, url):
        self.TOKEN = token
        self.BASE_URL = url
        self.HEADERS = {
            'Authorization': f'Bearer {self.TOKEN}'
        }
        self.cities = []

    def get_cities_information(self):
        response = requests.get(url=self.BASE_URL, headers=self.HEADERS)
        response.raise_for_status()
        self.cities = response.json().get('prices')
        return self.cities

    def put_city_information(self, city_id,  parameters):
        url = f'{BASE_URL}/{city_id}'
        response = requests.put(url=url, params=parameters, headers=self.HEADERS)
        return response.text


if __name__ == "__main__":
    data = DataManager(token=TOKEN, url=BASE_URL)
    print(data.get_cities_information())
