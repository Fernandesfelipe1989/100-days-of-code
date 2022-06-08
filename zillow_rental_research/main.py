import requests
import re
from time import sleep

from bs4 import BeautifulSoup
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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

        # Clean string config
        self.ZILLOW_URL_PATTERN = 'https://www.zillow.com'
        self.PRICE_PATTERN = r'([0-9].[0-9]+)'
        self.URL_PATTERN = r'(http..//)'

        # Selenium Config
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        chrome_driver_path = config('CHROME_DRIVER_PATH')
        driver_service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=driver_service, options=options)

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

    def post_renting_form(self):
        self.driver.get(url=config('FORM_URL'))
        for rent_index in range(0, len(self.address)):
            try:
                address_tag = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div['
                                                                          '2]/div[1]/div/div/div[2]/div/div['
                                                                          '1]/div/div[1]/input')
                address_tag.send_keys(self.address[rent_index])
                price_tag = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div['
                                                                        '2]/div[2]/div/div/div[2]/div/div[1]/div/div['
                                                                        '1]/input')
                price_tag.send_keys(self.prices[rent_index])
                link_tag = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div['
                                                                       '2]/div[3]/div/div/div[2]/div/div[1]/div/div['
                                                                       '1]/input')
                link_tag.send_keys(self.listings[rent_index])

                button_tag = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div['
                                                                         '3]/div[1]/div[1]/div')
                button_tag.click()
                sleep(2)
                return_tag = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                return_tag.click()
                sleep(2)
            except Exception as error:
                print(error)


if __name__ == "__main__":
    rental_research = ZillowRentalResearch()
    rental_research.get_renting_info()
    rental_research.post_renting_form()
