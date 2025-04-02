import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def handling_radio_button():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://letcode.in/test")
    driver.find_element(By.LINK_TEXT, "Toggle").click()
    radio_button = driver.find_element(By.XPATH, "//input[@id='one']")
    if radio_button.is_selected():
        print("The radio button is already selected")
    else:
        radio_button.click()

    time.sleep(5)


handling_radio_button()