from email.mime.text import MIMEText
import requests
import smtplib

from bs4 import BeautifulSoup
from decouple import config

HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'Accept-Language': 'en-US;q=0.9',
}
AMAZON_BASE_URL = config('AMAZON_BASE_URL')
EMAIL_RECEIVER = config('EMAIL_RECEIVER')
EMAIL_SENDER = config('EMAIL_SENDER')
EXPECT_PRICE = config('EXPECT_PRICE', cast=float)

EMAIL_HOST = config('EMAIL_HOST', default='smtp.mailtrap.io')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=2525)


def send_email(sender, receiver, message):
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)
        server.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=message.as_string())


def make_message(subject, content):
    message = MIMEText(content)
    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER
    return message


if __name__ == "__main__":

    amazon_response = requests.get(url=AMAZON_BASE_URL, headers=HEADERS)
    amazon_response.raise_for_status()
    try:
        soup = BeautifulSoup(amazon_response.text, 'html.parser')
    except Exception as error:
        print(error)
    else:
        product_tag = soup.find(name='span', class_="a-offscreen")
        product_name_tag = soup.find(name='span', id="productTitle")
        product_name = product_name_tag and product_name_tag.getText()
        if product_tag:
            product_price = product_tag.getText().split("R$")[1]
            price = float(product_price.replace(".", '').replace(",", "."))
            if price <= EXPECT_PRICE:
                print("Sending Email")
                content = f'{product_name}\nnow R$: {price:0.2}\n{AMAZON_BASE_URL}'
                message = make_message(subject="Amazon Price Alert", content=content)
                send_email(sender=EMAIL_SENDER, receiver=EMAIL_RECEIVER, message=message)
