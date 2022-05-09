import smtplib
from decouple import config


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
connection = smtplib.SMTP(host=host, port=port)
connection.starttls()
connection.login(user=user, password=password)
connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
connection.close()

