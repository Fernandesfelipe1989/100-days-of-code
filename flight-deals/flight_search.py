import requests

from decouple import config


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, api_key, location_url, search_url):
        self.API_KEY = api_key
        self.LOCATION_BASE_URL = location_url
        self.SEARCH_BASE_URL = search_url
        self.HEADERS = {
            'apikey': self.API_KEY,
        }

    def get_city_iata_information(self, city_name):
        url = f"{self.LOCATION_BASE_URL}/locations/query"
        parameters = {
            'term': city_name
        }
        response = requests.get(url=url, params=parameters, headers=self.HEADERS)
        response.raise_for_status()
        cities_information = response.json()['locations']
        if cities_information:
            city = cities_information[0]
            return city.get('code')




