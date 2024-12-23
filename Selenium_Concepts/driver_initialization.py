import time
from selenium import webdriver


def driver_initialization():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    time.sleep(20)
driver_initialization()