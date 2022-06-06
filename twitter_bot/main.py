from time import sleep

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    CHROME_DRIVER_PATH = config("CHROME_DRIVER_PATH")
    TWITTER_EMAIL = config('TWITTER_EMAIL')
    TWITTER_PASSWORD = config("TWITTER_PASSWORD")
    TWITTER_USERNAME = config("TWITTER_USERNAME")
    TWITTER_BASE_URL = 'https://twitter.com/i/flow/login'
    INTERNET_SPEED_URL = 'https://www.brasilbandalarga.com.br/bbl/'
    DEFAULT_MESSAGE = "Hey Internet Provider, why is my internet speed {} down/ {} up when I pay for 150 down/10 up?"

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
        print("Enter in the internet speed site")
        start_test_tag = self.driver.find_element(by=By.ID, value="btnIniciar")
        start_test_tag.click()
        sleep(60)
        speed_tag = self.driver.find_elements(by=By.CLASS_NAME, value='textao')
        self.down = float(speed_tag[0].text)
        self.up = float(speed_tag[1].text)

    def tweet_at_provider(self):
        print("Enter in the twitter site")
        self.driver.get(bot.TWITTER_BASE_URL)
        sleep(10)
        email_tag = self.driver.find_element(by=By.NAME, value='text')
        email_tag.send_keys(self.TWITTER_EMAIL)
        next_button_tag = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button_tag.click()
        sleep(10)
        username_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                   '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                                   '2]/label/div/div[2]/div/input')
        username_tag.send_keys(self.TWITTER_USERNAME)
        next_button_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                      '2]/div[2]/div/div/div[2]/div[2]/div['
                                                                      '2]/div/div/div')
        next_button_tag.click()
        sleep(10)
        password_tag = self.driver.find_element(by=By.NAME, value='password')
        password_tag.send_keys(self.TWITTER_PASSWORD)
        login_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                '2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                                                                '1]/div/div/div')
        login_tag.click()
        sleep(10)

        tweet_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                '2]/main/div/div/div/div[1]/div/div[2]/div/div['
                                                                '2]/div[1]/div/div/div/div[2]/div['
                                                                '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                                '1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_tag.send_keys(self.DEFAULT_MESSAGE.format(self.down, self.up))
        tweet_button_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                       '2]/main/div/div/div/div[1]/div/div['
                                                                       '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                                       '3]/div/div/div[2]/div[3]')
        tweet_button_tag.click()
        sleep(10)
        self.driver.close()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
