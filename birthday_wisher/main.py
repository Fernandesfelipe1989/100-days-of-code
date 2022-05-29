import datetime as dt
from email.mime.text import MIMEText
import smtplib
from random import choice

from decouple import config
import pandas as pd

PATTERN_MESSAGE = '[NAME]'
PATH_LETTERS = [
    './letter_templates/letter_1.txt',
    './letter_templates/letter_2.txt',
    './letter_templates/letter_3.txt',
]
PATH_BIRTHDAY = "birthdays.csv"


def make_message(subject, content):
    message = MIMEText(content)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    return message


def send_email(message):
    with smtplib.SMTP(host=host, port=port) as server:
        server.login(user=user, password=password)
        server.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=message.as_string(),
        )


if __name__ == "__main__":
    birthdays = pd.read_csv('birthdays.csv').to_dict(orient='records')
    current_day = dt.datetime.now()
    letter = ""
    person_birthday = None

    host = config("EMAIL_HOST", default='smtp.mailtrap.io')
    port = config("EMAIL_PORT", default=2525)
    user = config("EMAIL_HOST_USER", default="")
    password = config("EMAIL_HOST_PASSWORD", default="")
    sender = config("EMAIl_SENDER", default="test@gmail.com")
    receiver = config("EMAIl_RECEIVER", default="test@gmail.com")

    for birthday in birthdays:
        if birthday['day'] == current_day.day and birthday['month'] == current_day.month:
            person_birthday = birthday

    if person_birthday:
        path_letter = choice(PATH_LETTERS)
        try:
            with open(path_letter, 'r') as message:
                letter = message.read()
        except FileNotFoundError:
            letter = f"Happy Birthday {PATTERN_MESSAGE}"

        letter = letter.replace(PATTERN_MESSAGE, person_birthday['name'])
        message = make_message('Happy Birthday', letter)
        send_email(message=message)



