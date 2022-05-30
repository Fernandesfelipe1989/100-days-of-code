
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
chrome_driver_path = config('CHROME_DRIVER_PATH')
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by="css selector", value="#articlecount a")
# article_count.click()

wikidata = driver.find_element(by="link text", value='Wikidata')
# wikidata.click()

search = driver.find_element(by=By.NAME, value='search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)


driver.quit()

