import datetime as dt
import requests
import typing

from decouple import config
from twilio.rest import Client


COMPANY_NAME = "Tesla Inc"
STOCK = "TSLA"


class StockInformation:
    ALPHAVANTAGE_API_KEY = config('ALPHAVANTAGE_API_KEY')
    ALPHAVANTAGE_BASE_URL = config("ALPHAVANTAGE_BASE_URL")

    NEWSAPI_API_KEY = config('NEWSAPI_API_KEY')
    NEWSAPI_BASE_URL = config("NEWSAPI_BASE_URL")

    TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
    TWILIO_SEND_NUMBER = config("TWILIO_SEND_NUMBER")
    TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER")

    def __init__(self, company: str, stock: str, stock_range: int):
        self.COMPANY_NAME = company
        self.STOCK = stock
        self.stock_range = stock_range
        self.stock_rate_percent = 0
        self.articles = None
        self.message = None

    def get_stock_price(self, **kwargs) -> requests.Response:
        default_parameter = {
            'apikey': self.ALPHAVANTAGE_API_KEY,
            'symbol': STOCK,
            'function': 'TIME_SERIES_DAILY',
        }
        parameters = dict(default_parameter, **kwargs)
        response = requests.get(url=self.ALPHAVANTAGE_BASE_URL, params=parameters)
        response.raise_for_status()
        return response and response.json()

    def get_company_information(self, **kwargs) -> typing.Union[dict, None]:
        default_parameters = {
            'apiKey': self.NEWSAPI_API_KEY,
            'q': self.COMPANY_NAME,
            'from': str(dt.date.today()) + '&',
            'sortBy': 'popularity&',
        }
        parameters = dict(default_parameters, **kwargs)
        response = requests.get(url=self.NEWSAPI_BASE_URL, params=parameters)
        response.raise_for_status()
        return response and response.json()

    def get_company_articles(self) -> typing.Union[typing.List[tuple], None]:
        company_name_information = self.get_company_information()
        if company_name_information:
            company_articles = company_name_information['articles']
            return company_articles and [(article['title'], article['description']) for article in company_articles[:3]]

    def create_message(self) -> str:
        company_name = f"{self.COMPANY_NAME}:"
        stock_message = f"🔺{self.stock_rate_percent:.0f}%" \
            if self.stock_rate_percent > 0 else f'🔻{self.stock_rate_percent:.0f}%'
        articles = [f"Headline: {article[0]},\n Brief: {article[1]}" for article in self.articles]
        message = "\n".join(articles)
        return "\n".join([company_name + stock_message, message])

    def send_sms(self, body: str):
        client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)
        sms_obj = client.messages.create(
            body=body,
            from_=self.TWILIO_SEND_NUMBER,
            to=self.TWILIO_TO_NUMBER
        )
        self.message = sms_obj.body

    def get_stock_information(self) -> str:
        last_day = 1
        before_last_day = 2
        today = dt.datetime.now().date()
        weekday = today.weekday()
        stock_data = self.get_stock_price()
        if stock_data:
            if weekday == 6:
                last_day = 2
                before_last_day = 3
            stock_yesterday = stock_data['Time Series (Daily)'].get(str(today - dt.timedelta(days=last_day)))
            stock_yesterday_price = float(stock_yesterday['4. close'])
            stock_before_yesterday = stock_data['Time Series (Daily)'].get(
                str(today - dt.timedelta(days=before_last_day)))
            stock_before_yesterday_price = float(stock_before_yesterday['4. close'])
            rate = (stock_yesterday_price - stock_before_yesterday_price) / stock_yesterday_price
            self.stock_rate_percent = rate * 100
            if self.stock_rate_percent > self.stock_range or self.stock_rate_percent < -self.stock_range:
                self.articles = self.get_company_articles()
                self.send_sms(body=self.create_message())
        return self.message


if __name__ == "__main__":
    stock = StockInformation(company=COMPANY_NAME, stock=STOCK, stock_range=5)
    print(stock.get_stock_information())
