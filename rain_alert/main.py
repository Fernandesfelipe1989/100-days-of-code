import requests

from decouple import config
from twilio.rest import Client


ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
API_KEY = config('API_KEY')
BASE_URL = config('BASE_URL')
TWILIO_SEND_NUMBER = config("TWILIO_SEND_NUMBER")
TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER")
LAT = config("LAT", cast=float)
LON = config("LON", cast=float)

client = Client(ACCOUNT_SID, AUTH_TOKEN)


if __name__ == "__main__":
    parameters = {
        'lat': LAT,
        'lon': LON,
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
        pass
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_=TWILIO_SEND_NUMBER,
            to=TWILIO_TO_NUMBER
            )
        print(message.status)
        print(message.body)
