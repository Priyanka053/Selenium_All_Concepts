import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def backward_forward_navigation():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    time.sleep(3)
    search_box = driver.find_element(By.XPATH, '//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')
    search_box.send_keys("Python")
    search_button = driver.find_element(By.XPATH, '//button[contains(@class, "ytSearchboxComponentSearchButton")]')
    search_button.click()
    driver.back()
    time.sleep(10)
    driver.forward()
    time.sleep(10)
    driver.quit()


backward_forward_navigation()


def refresh_window():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    time.sleep(3)
    driver.refresh()
    driver.quit()


refresh_window()
