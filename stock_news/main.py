import datetime as dt
import os
import requests
import typing

from decouple import config
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

ALPHAVANTAGE_API_KEY = config('ALPHAVANTAGE_API_KEY')
ALPHAVANTAGE_BASE_URL = config("ALPHAVANTAGE_BASE_URL")

NEWSAPI_API_KEY = config('NEWSAPI_API_KEY')
NEWSAPI_BASE_URL = config("NEWSAPI_BASE_URL")

TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
TWILIO_SEND_NUMBER = config("TWILIO_SEND_NUMBER")
TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER")

COMPANY_NAME = "Tesla Inc"
STOCK = "TSLA"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_price(**kwargs) -> requests.Response:
    default_parameter = {
        'apikey': ALPHAVANTAGE_API_KEY,
        'symbol': STOCK,
        'function': 'TIME_SERIES_DAILY',
    }
    parameters = dict(default_parameter, **kwargs)
    response = requests.get(url=ALPHAVANTAGE_BASE_URL, params=parameters)
    response.raise_for_status()
    return response and response.json()


def get_stock_information():
    last_day = 1
    before_last_day = 2
    today = dt.datetime.now().date()
    weekday = today.weekday()
    stock_data = get_stock_price()
    if stock_data:
        if weekday == 6:
            last_day = 2
            before_last_day = 3
        stock_yesterday = stock_data['Time Series (Daily)'].get(str(today - dt.timedelta(days=last_day)))
        stock_yesterday_price = float(stock_yesterday['4. close'])
        stock_before_yesterday = stock_data['Time Series (Daily)'].get(str(today - dt.timedelta(days=before_last_day)))
        stock_before_yesterday_price = float(stock_before_yesterday['4. close'])
        rate_percent = ((stock_yesterday_price - stock_before_yesterday_price) / stock_yesterday_price) * 100
        if rate_percent > 5 or rate_percent < -5:
            articles = get_company_articles(company_name=COMPANY_NAME)
            body = create_message(company_name=COMPANY_NAME, rate=rate_percent, articles=articles)
            send_sms(body=body)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_company_information(company_name: str, **kwargs) -> typing.Union[dict, None]:
    default_parameters = {
        'apiKey': NEWSAPI_API_KEY,
        'q': company_name,
        'from': str(dt.date.today()) + '&',
        'sortBy': 'popularity&',
    }
    parameters = dict(default_parameters, **kwargs)
    response = requests.get(url=NEWSAPI_BASE_URL, params=parameters)
    response.raise_for_status()
    return response and response.json()


def get_company_articles(company_name: str) -> typing.Union[typing.List[tuple], None]:
    company_name_information = get_company_information(company_name=company_name)
    if company_name_information:
        company_articles = company_name_information['articles']
        return company_articles and [(article['title'], article['description']) for article in company_articles[:3]]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def create_message(company_name: str, rate: float, articles: list) -> str:
    company_name = f"{company_name}:" + f"🔺{rate:.0f}%" if rate > 0 else f'🔻{rate:.0f}%'
    articles = [f"Headline: {article[0]},\n Brief: {article[1]}" for article in articles]
    message = "\n".join(articles)
    return "\n".join([company_name, message])


def send_sms(body: str):
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ['https_proxy']}
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=TWILIO_SEND_NUMBER,
        to=TWILIO_TO_NUMBER
    )
    print(message.status)
    print(message.body)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":
    get_stock_information()
