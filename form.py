from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/text-box")
   
    driver.find_element(By.ID, "userName").send_keys("Moni")
    driver.find_element(By.ID, "userEmail").send_keys("Moni@test.com")
    driver.find_element(By.ID,"currentAddress").send_keys("anna nagar");
    driver.find_element(By.ID,"permanentAddress").send_keys("T nagar");

    # scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sub_btn = driver.find_element(By.ID, "submit")

    # FIXED LINE
    driver.execute_script("arguments[0].click();", sub_btn)
   

    time.sleep(15)