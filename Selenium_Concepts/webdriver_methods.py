from selenium import webdriver
import time


def webdriver_methods():
    driver = webdriver.Chrome()
    # opening_page_url
    driver.get("https://www.youtube.com/")
    # verifying_page_title
    assert driver.title == "YouTube"
    # getting_page_source
    print(driver.page_source)
    # getting_page_url
    print(driver.current_url)

    time.sleep(2)


webdriver_methods()
