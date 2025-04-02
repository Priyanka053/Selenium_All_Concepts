import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def handling_check_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://letcode.in/test")
    driver.find_element(By.LINK_TEXT, "Toggle").click()
    check_box = driver.find_element(By.XPATH, "//label[@class='checkbox'][contains(text(),'Remember me')]/input")
    if check_box.is_selected():
        print("The check box is already selected")
    else:
        check_box.click()

    time.sleep(5)


handling_check_box()
