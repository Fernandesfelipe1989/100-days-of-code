import time

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


cookie_per_seconds = {
    'grandma': 0.8,
    'factory': 4.0,
    'mine': 10.0,
    'shipment': 20,
    'lab': 100,
    'portal': 6666/5,
    'time': 123456/5,
}


def buy_element():
    # --------- Get HTMl Elements ---------
    money_tag = driver.find_element(by=By.ID, value='money')
    money = int(money_tag.text.replace(",", ""))

    cursor_cost_tag = driver.find_element(by=By.CSS_SELECTOR, value='#buyCursor b')
    cursor_cost = int(cursor_cost_tag.text.split(" - ")[1].replace(",", ""))

    grandma_cost_tag = driver.find_element(by=By.CSS_SELECTOR, value='#buyGrandma b')
    grandma_cost = int(grandma_cost_tag.text.split(" - ")[1].replace(",", ""))

    factory_cost_tag = driver.find_element(by=By.CSS_SELECTOR, value='#buyFactory b')
    factory_cost = int(factory_cost_tag.text.split(" - ")[1].replace(",", ""))

    mine_cost_tag = driver.find_element(by=By.CSS_SELECTOR, value='#buyMine b')
    mine_cost = int(mine_cost_tag.text.split(" - ")[1].replace(",", ""))

    shipment_cost_tag = driver.find_element(by=By.CSS_SELECTOR, value='#buyShipment b')
    shipment_cost = int(shipment_cost_tag.text.split(" - ")[1].replace(",", ""))

    alchemy_lab_cost_tag = driver.find_element(by=By.XPATH, value="//div[@id='buyAlchemy lab']/b")
    alchemy_lab_cost = int(alchemy_lab_cost_tag.text.split(" - ")[1].replace(",", ""))

    portal_cost_tag = driver.find_element(by=By.CSS_SELECTOR, value='#buyPortal b')
    portal_cost = int(portal_cost_tag.text.split(" - ")[1].replace(",", ""))

    time_machine_cost_tag = driver.find_element(by=By.XPATH, value="//div[@id='buyTime machine']/b")
    time_machine_cost = int(time_machine_cost_tag.text.split(" - ")[1].replace(",", ""))

    # --------- Check Buy Elements ---------
    if money >= time_machine_cost and (money//time_machine_cost) < cookie_per_seconds['time']:
        time_machine_cost_tag.click()
    if portal_cost <= money < time_machine_cost and (money//portal_cost) < cookie_per_seconds['portal']:
        portal_cost_tag.click()
    if alchemy_lab_cost <= money < portal_cost and (money//alchemy_lab_cost) < cookie_per_seconds['lab']:
        alchemy_lab_cost_tag.click()
    if shipment_cost <= money < alchemy_lab_cost and (money//mine_cost) < cookie_per_seconds['shipment']:
        shipment_cost_tag.click()
    if mine_cost <= money < shipment_cost and (money//mine_cost) < cookie_per_seconds['mine']:
        mine_cost_tag.click()
    if factory_cost <= money < mine_cost and (money//mine_cost) < cookie_per_seconds['factory']:
        factory_cost_tag.click()
    if grandma_cost <= money < factory_cost and (money//factory_cost) < cookie_per_seconds['grandma']:
        grandma_cost_tag and grandma_cost_tag.click()
    # if money >= cursor_cost:
    #     cursor_cost_tag and cursor_cost_tag.click()


if __name__ == "__main__":

    # Selenium Config
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver_path = config('CHROME_DRIVER_PATH')
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.get('http://orteil.dashnet.org/experiments/cookie/')

    cookie = driver.find_element(by=By.ID, value='cookie')

    # Time Config
    last_seconds = time.time()
    start_seconds = time.time()
    now_seconds = time.time()

    while (now_seconds - start_seconds) <= 300:
        cookie.click()
        if now_seconds - last_seconds > 5:
            buy_element()
            last_seconds = now_seconds
        now_seconds = time.time()
    driver.quit()

