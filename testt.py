from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_js_alert():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="jsPrompt()"]').click()
    time.sleep(5)

    alert = driver.switch_to.alert      # ← changed line
    alert.send_keys("hello moni")        # ← changed line

    time.sleep(10)
    driver.switch_to.alert.accept()
    driver.quit()

test_js_alert()
