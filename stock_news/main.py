from typing import Union

import requests
import datetime as dt

from decouple import config

API_KEY = config('API_KEY')
COMPANY_NAME = "Tesla Inc"
BASE_URL = config("BASE_URL")
STOCK = "TSLA"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_price(**kwargs) -> requests.Response:

    default_parameter = {
        'apikey': API_KEY,
        'symbol': STOCK,
        'function': 'TIME_SERIES_DAILY',
    }
    parameters = dict(default_parameter, **kwargs)
    response = requests.get(url=BASE_URL, params=parameters)
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
            print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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
    print(get_stock_behavior())
