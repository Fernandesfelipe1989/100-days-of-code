from time import sleep

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
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
        sleep(5)
        username_tag = self.driver.find_element(by=By.NAME, value='username')
        username_tag.send_keys(self.INSTAGRAM_USERNAME)

        password_tag = self.driver.find_element(by=By.NAME, value="password")
        password_tag.send_keys(self.INSTAGRAM_PASSWORD)

        login_button_tag = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button_tag.click()
        sleep(5)

    def find_followers(self):
        self.driver.get(url=self.INSTAGRAM_FOLLOW_URL)
        sleep(10)
        followers_button_tag = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div['
                                                                        '1]/div/div/div[1]/div['
                                                                        '1]/section/main/div/header/section/ul/li['
                                                                        '2]/a')
        followers_button_tag.click()

        follows_button_tag = self.driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[1]/div/div[@class="_aaen"]/button')
        for follow_button in follows_button_tag:
            try:
                follow_button.click()

            except NoSuchElementException:
                print("No follow button, skipped.")

            except Exception as error:
                print(error)
        sleep(10)

    def follow(self):
        pass


if __name__ == "__main__":
    insta_follower = InstaFollower()
    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()
