from time import sleep

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
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
        sleep(2)
        scrollable_popup = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div["
                                                              "2]/div/div/div[1]/div/div[2]/div/div/div")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            sleep(2)

    def follow(self):

        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

            except NoSuchElementException:
                print("Finished")
        sleep(10)


if __name__ == "__main__":
    insta_follower = InstaFollower()
    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()
