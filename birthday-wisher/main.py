import smtplib
from decouple import config

connect = smtplib.SMTP()
host = config('EMAIL_HOST', default="smtp.mailtrap.io")
port = config('EMAIL_PORT', default="2525")
user = config('EMAIL_HOST_USER', default="")
password = config('EMAIL_HOST_PASSWORD', default="")


sender = config("EMAIl_SENDER", default="teste@gmail.com")
receiver = config("EMAIl_RECEIVER", default="teste@gmail.com")
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""
with smtplib.SMTP(host, port) as server:
    server.login(user, password)
    server.sendmail(sender, receiver, message)
