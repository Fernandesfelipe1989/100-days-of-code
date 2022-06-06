from time import sleep

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    CHROME_DRIVER_PATH = config("CHROME_DRIVER_PATH")
    TWITTER_EMAIL = config('TWITTER_EMAIL')
    TWITTER_PASSWORD = config("TWITTER_PASSWORD")
    TWITTER_BASE_URL = 'https://twitter.com/i/flow/login'
    INTERNET_SPEED_URL = 'https://www.brasilbandalarga.com.br/bbl/'

    def __init__(self):
        self.up = 0
        self.down = 0

        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chrome_driver_path = self.CHROME_DRIVER_PATH
        driver_service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=driver_service, options=options)

    def get_internet_speed(self):
        self.driver.get(bot.INTERNET_SPEED_URL)
        print("Entrei internet")
        start_test_tag = self.driver.find_element(by=By.ID, value="btnIniciar")
        start_test_tag.click()
        sleep(60)
        speed_tag = self.driver.find_elements(by=By.CLASS_NAME, value='textao')
        self.down = float(speed_tag[0].text)
        self.up = float(speed_tag[1].text)
        print(self.down, self.up)

    def tweet_at_provider(self):
        print("Entrei twitter")
        self.driver.get(bot.TWITTER_BASE_URL)
        sleep(10)
        self.driver.close()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
