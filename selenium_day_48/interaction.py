
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
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Teste")
last_name = driver.find_element(by=By.NAME, value='lName')
last_name.send_keys("Da Silva")
email = driver.find_element(by=By.NAME, value='email')
email.send_keys("test@gmail.com")
sing_up = driver.find_element(by=By.CSS_SELECTOR, value="button")
sing_up.click()

driver.quit()

