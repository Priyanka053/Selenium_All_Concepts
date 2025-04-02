import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def handling_text_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://letcode.in/test")
    driver.find_element(By.LINK_TEXT, "Edit").click()
    text_box = driver.find_element(By.ID, "fullName")
    text_box.send_keys("Priyanka")

    time.sleep(5)


handling_text_box()
