import datetime as dt
from random import choice
import smtplib

from decouple import config

DAY_WEEK = {
    0: 'Monday',
    1: "Tuesday",
    2: "Wednesday",
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


with open('quotes.txt', 'r') as file:
    messages = [line for line in file]

host = config('EMAIL_HOST', default="smtp.mailtrap.io")
port = config('EMAIL_PORT', default="2525")
user = config('EMAIL_HOST_USER', default="")
password = config('EMAIL_HOST_PASSWORD', default="")

sender = config("EMAIl_SENDER", default="teste@gmail.com")
receiver = config("EMAIl_RECEIVER", default="teste@gmail.com")

message = f"""\
Subject: Motivational quote
To: {receiver}
From: {sender}

{choice(messages)}"""
current_day = dt.datetime.now()
day_of_week = current_day.weekday()
if DAY_WEEK.get(day_of_week).lower() == "monday":
    with smtplib.SMTP(host=host, port=port) as server:
        server.login(user=user, password=password)
        print('Send Email')
        server.sendmail(sender, receiver, message)
