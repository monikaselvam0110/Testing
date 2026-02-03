from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_check_box():

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open Check Box page
    driver.get("https://demoqa.com/checkbox")
    time.sleep(2)

    # Expand Home
    driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']").click()
    time.sleep(1)

    # Click Desktop checkbox
    driver.find_element(
        By.XPATH, "//span[text()='Desktop']/preceding-sibling::span[@class='rct-checkbox']"
    ).click()
    time.sleep(1)

    # Click Documents checkbox
    driver.find_element(
        By.XPATH, "//span[text()='Documents']/preceding-sibling::span[@class='rct-checkbox']"
    ).click()
    time.sleep(1)

    # Click Downloads checkbox
    driver.find_element(
        By.XPATH, "//span[text()='Downloads']/preceding-sibling::span[@class='rct-checkbox']"
    ).click()
    time.sleep(2)

    driver.quit()