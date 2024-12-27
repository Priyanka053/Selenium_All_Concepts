import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def implicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    driver.implicitly_wait(5)

    search_box = driver.find_element(By.XPATH, '//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')
    search_box.send_keys("Selenium with Python")

    driver.quit()


implicit_wait()


def explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')))
    search_box.send_keys("Selenium with Python")

    driver.quit()


explicit_wait()


# visibility_of_element_located: Waits until the element is visible.
# presence_of_element_located: Waits until the element is present in the DOM.
# element_to_be_clickable: Waits until the element is clickable.
# text_to_be_present_in_element: Waits until the text is present in the element.


def page_load_wait():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)
    try:
        driver.get("https://www.youtube.com")
    except:
        print("Page Load Timeout")

    driver.quit()


page_load_wait()

# page load timeout is for controlling the overall page load time.
# Prevents tests from running too long if the page is taking too much time to load.
