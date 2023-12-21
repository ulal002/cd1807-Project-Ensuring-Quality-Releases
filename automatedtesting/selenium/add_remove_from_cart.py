# #!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

def timestamp():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")

# Start the browser and login with standard_user
def login(user, password):
    print("Current working directory:", os.getcwd())
    print(timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"executable_path={chromedriver_path}")
    chromedriver_path = '/usr/local/bin/chromedriver'
    print(timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    
    # Login
    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    
    return driver

def add_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        item_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        item_link.click()
        
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn_primary.btn_inventory"))
        )
        add_to_cart_button.click()
        
        product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.inventory_details_name"))
        ).text
        
        print(timestamp() + product + " added to the shopping cart.")
        
        back_button = driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button")
        back_button.click()
    print(timestamp() + '{:d} items added to the shopping cart successfully.'.format(n_items))

def remove_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        item_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        item_link.click()
        
        remove_from_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn_secondary.btn_inventory"))
        )
        remove_from_cart_button.click()
        
        product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.inventory_details_name"))
        ).text
        
        print(timestamp() + product + " removed from the shopping cart.")
        
        back_button = driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button")
        back_button.click()
    print(timestamp() + '{:d} items removed from the shopping cart successfully.'.format(n_items))

if __name__ == "__main__":
    N_ITEMS = 6
    TEST_USERNAME = 'standard_user'
    TEST_PASSWORD = 'secret_sauce'
    driver = login(TEST_USERNAME, TEST_PASSWORD)
    add_cart(driver, N_ITEMS)
    remove_cart(driver, N_ITEMS)
    print(timestamp() + 'Selenium tests are all successfully completed!')
    driver.quit()
