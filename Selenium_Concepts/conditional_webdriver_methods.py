import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def conditional_webdriver_methods():
    # driver initialization
    driver = webdriver.Chrome()
    # get/open the url
    driver.get("https://www.youtube.com")

    # Conditional Methods - Wait for an element to be visible
    search_box=WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        ((By.XPATH, '//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]'))))
    # search_box.send_keys("Selenium with Python")

    # Visibility of web element
    search_box = driver.find_element(By.XPATH, '//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')
    if search_box.is_displayed():
        print("The search box is visible.")
    else:
        print("The search box is not visible.")

    # Checking if the web element is enabled or disabled
    search_button = driver.find_element(By.XPATH,'//button[contains(@class, "ytSearchboxComponentSearchButton")]')
    if search_button.is_enabled():
        print("The search button is enabled.")
    else:
        print("The search button is not enabled.")

    time.sleep(2)
    driver.quit()


conditional_webdriver_methods()
