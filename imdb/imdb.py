from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDBSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/name/"
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get(self.url)

    def fill_search_criteria(self, name):
        name_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        name_input.send_keys(name)

    def perform_search(self):
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        search_button.click()
