import requests
import re

from bs4 import BeautifulSoup
from decouple import config


class ZillowRentalResearch:
    ZILLOW_URL = config('ZILLOW_URL')
    FORM_URL = config('FORM_URL')
    ZILLOW_HEADER = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'Accept-Language': 'en-US;q=0.9',
    }

    def __init__(self):
        self.listings = []
        self.prices = []
        self.address = []
        self.ZILLOW_URL_PATTERN = 'https://www.zillow.com'
        self.PRICE_PATTERN = r'([0-9].[0-9]+)'
        self.URL_PATTERN = r'(http..//)'

    def clean_price(self, price):
        price_cleaned = re.findall(self.PRICE_PATTERN, price)
        return price_cleaned and float(price_cleaned[0].replace(',', ""))

    def clean_url(self, url):
        url_cleaned = re.match(self.URL_PATTERN, url)
        if url_cleaned and url_cleaned.group():
            return url
        return self.ZILLOW_URL_PATTERN + url

    def get_renting_info(self):
        response = requests.get(url=self.ZILLOW_URL, headers=self.ZILLOW_HEADER)
        try:
            response.raise_for_status()
        except Exception as error:
            print(error)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            prices = soup.find_all(name='div', class_="list-card-price")
            self.prices = [self.clean_price(price.getText()) for price in prices]
            addresses = soup.find_all(name='address', class_="list-card-addr")
            self.address = [address.getText() for address in addresses]
            listings = soup.find_all(name='a', class_="list-card-link", href=True)
            self.listings = [self.clean_url(listing['href']) for listing in listings]


if __name__ == "__main__":
    rental_research = ZillowRentalResearch()
    rental_research.get_renting_info()
