from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

# Define the Instagram URL
url = "https://www.instagram.com/guviofficial/"

# Set up the webdriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

try:
    # Navigate to the Instagram profile page
    driver.maximize_window()
    driver.get(url)
    time.sleep(6)  # Allow some time for the page to load

    # Extract followers count 
    followers_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[2]/div/button/span/span'
    followers_element = wait.until(presence_of_element_located((By.XPATH, followers_xpath)))
    followers_count = followers_element.text  
    print(f"Followers: {followers_count}")

    # Extract following count 
    following_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[3]/div/button/span/span'
    following_element = wait.until(presence_of_element_located((By.XPATH, following_xpath)))
    following_count = following_element.text
    print(f"Following: {following_count}")

finally:
    # Close the webdriver
    driver.quit()
