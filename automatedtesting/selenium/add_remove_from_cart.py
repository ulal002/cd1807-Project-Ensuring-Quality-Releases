# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

def timestamp():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")

# Start the browser and login with standard_user
def login(user, password):
    print(timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options, executable_path="/usr/local/bin/chromedriver")
    print(timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    return driver

def add_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text
        print(timestamp() + product + " added to the shopping cart.")
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items added to the shopping cart successfully.'.format(n_items))

def remove_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text
        print(timestamp() + product + " removed from the shopping cart.")
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
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
