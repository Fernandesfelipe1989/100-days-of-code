from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
chrome_driver_path = config('CHROME_DRIVER_PATH')
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service, options=options)

driver.get("https://www.amazon.com")
driver.quit()