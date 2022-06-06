from time import sleep

from decouple import config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

LINKEDIN_BASE_URL = config("LINKEDIN_BASE_URL")
LINKEDIN_PASSWORD = config("LINKEDIN_PASSWORD")
LINKEDIN_USERNAME = config("LINKEDIN_USERNAME")

if __name__ == "__main__":
    # Selenium Config
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver_path = config('CHROME_DRIVER_PATH')
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.get(LINKEDIN_BASE_URL)
    # Job Pages
    sign_in_tag = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[@class="nav__button-secondary"]')
    sign_in_tag.click()

    sleep(5)

    # LinkedIn sign_in flow
    username_tag = driver.find_element(by=By.ID, value='username')
    username_tag.send_keys(LINKEDIN_USERNAME)

    password_tag = driver.find_element(by=By.ID, value='password')
    password_tag.send_keys(LINKEDIN_PASSWORD)

    sign_in_button_tag = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
    sign_in_button_tag.click()

    sleep(15)
    jobs_tags = driver.find_elements(
        by=By.CLASS_NAME,
        value="job-card-container--clickable",
    )
    for job_tag in jobs_tags:
        print("called")
    try:
        print("Entrei no try")
        # JobApplication
        job_tag.click()
        sleep(2)
        easy_apply_tag = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
        easy_apply_tag.click()
        sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")

    except Exception as error:
        print(error)

    driver.quit()




