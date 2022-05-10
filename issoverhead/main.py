import datetime as dt
import requests

MY_LAT = -23.482050
MY_LNG = -47.414290
URL_BASE_ISS = "http://api.open-notify.org/iss-now.json"
URL_BASE_SUNRISE = 'https://api.sunrise-sunset.org/json'

if __name__ == "__main__":
    time_now = dt.datetime.now()
    sunrise_parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }
    response_iss = requests.get(url=URL_BASE_ISS)
    response_iss.raise_for_status()
    iss_information = response_iss.json()

    response_sunrise = requests.get(url=URL_BASE_SUNRISE, params=sunrise_parameters)
    print(response_sunrise.json())
    date_sunrise, hour_sunrise = response_sunrise.json()['results']['sunrise'].split('T')
    date_sunset, hour_sunset = response_sunrise.json()['results']['sunset'].split('T')
    print(date_sunrise)



