import time
from selenium import webdriver


def driver_initialization():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    assert driver.title == 'YouTube'

    time.sleep(20)


driver_initialization()
