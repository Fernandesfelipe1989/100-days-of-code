from time import sleep

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InstaFollower:
    INSTAGRAM_LOGIN_URL = config('INSTAGRAM_LOGIN_URL')
    INSTAGRAM_FOLLOW_URL = config('INSTAGRAM_FOLLOW_URL')
    INSTAGRAM_USERNAME = config('INSTAGRAM_USERNAME')
    INSTAGRAM_PASSWORD = config('INSTAGRAM_PASSWORD')

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        chrome_driver_path = config('CHROME_DRIVER_PATH')
        driver_service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=driver_service, options=options)

    def login(self):
        self.driver.get(url=self.INSTAGRAM_LOGIN_URL)
        sleep(10)

    def find_followers(self):
        self.driver.get(url=self.INSTAGRAM_FOLLOW_URL)
        sleep(10)

    def follow(self):
        pass


if __name__ == "__main__":
    insta_follower = InstaFollower()
    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()
