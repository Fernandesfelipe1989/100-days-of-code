import requests

from decouple import config

API_KEY = config('API_KEY')
BASE_URL = config('BASE_URL')

if __name__ == "__main__":
    parameters = {
        'lat': -23.482050,
        'lon': -47.414291,
        'appid': API_KEY,
        'exclude': 'minutely,daily'
    }
    response = requests.get(url=BASE_URL, params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    will_rain = False
    for hourly_weather in weather_data.get("hourly")[:12]:
        weather_info = hourly_weather.get('weather')
        condition_code = weather_info and int(weather_info[0].get('id'))
        will_rain = True if condition_code and condition_code < 700 else False
    if will_rain:
        print("It's going to rain.")

