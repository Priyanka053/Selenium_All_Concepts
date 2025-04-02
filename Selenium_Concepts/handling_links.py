import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def handling_link():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://letcode.in/test")
    driver.find_element(By.LINK_TEXT, "Edit").click()
    time.sleep(5)


handling_link()
