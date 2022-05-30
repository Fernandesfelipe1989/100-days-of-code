from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
chrome_driver_path = config('CHROME_DRIVER_PATH')
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get("https://www.python.org/")
events_names = driver.find_elements(by="xpath", value="//div/section/div[3]/div[@class='medium-widget event-widget "
                                                      "last']/div/ul[@class='menu']/li/a")

events_dates = driver.find_elements(by="css selector", value='div.last div ul li time')


events_info = {index: {'time': events_dates[index].get_attribute('datetime').split("T")[0], 'name': event_name.text}
               for index, event_name in enumerate(events_names)}

print(events_info)
driver.close()
