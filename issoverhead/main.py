from email.mime.text import MIMEText
import datetime as dt
import requests
import smtplib
import time

from decouple import config

host = config("EMAIL_HOST", default="")
port = config('EMAIL_PORT', cast=int, default=2525)
user = config("EMAIL_HOST_USER")
password = config("EMAIL_HOST_PASSWORD")
receiver = config("RECEIVER", default="test@gmail.com")
sender = config("SENDER", default="test@gmail.com")

ERROR_MARGIN = 5
MY_LAT = -23.482050
MY_LNG = -47.414290
URL_BASE_ISS = "http://api.open-notify.org/iss-now.json"
URL_BASE_SUNRISE = 'https://api.sunrise-sunset.org/json'

MESSAGE = "Look Up. The Iss is close to your position"


def is_iss_overhead():
    response_iss = requests.get(url=URL_BASE_ISS)
    response_iss.raise_for_status()
    iss_information = response_iss.json()
    iss_latitude = float(iss_information['iss_position']['latitude'])
    iss_longitude = float(iss_information['iss_position']['longitude'])

    return (MY_LAT - ERROR_MARGIN <= iss_latitude <= MY_LAT + ERROR_MARGIN) and \
           (MY_LNG - ERROR_MARGIN <= iss_longitude <= MY_LNG + ERROR_MARGIN)


def is_night(hour):
    sunrise_parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }
    response_sunrise = requests.get(url=URL_BASE_SUNRISE, params=sunrise_parameters)
    hour_sunrise = int(response_sunrise.json()['results']['sunrise'].split('T')[1].split(":")[0])
    hour_sunset = int(response_sunrise.json()['results']['sunset'].split('T')[1].split(":")[0])
    return hour_sunset <= hour <= hour_sunrise


def create_message(subject, content, sender, receiver):
    message = MIMEText(content)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    return message


def send_email(sender, receiver, message):
    with smtplib.SMTP(host=host, port=port) as server:
        print("Connection")
        server.login(user=user, password=password)
        print("Sending email")
        server.sendmail(sender, receiver, message.as_string())


if __name__ == "__main__":
    while True:
        time.sleep(60)
        time_now = dt.datetime.now()
        if is_iss_overhead():
            if is_night(time_now.hour):
                message = create_message("Look UP", MESSAGE, sender, receiver)
                send_email(sender=sender, receiver=receiver, message=message)
