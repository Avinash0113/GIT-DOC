import time
from selenium import webdriver
from selenium.webdriver.common.by import By

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.facebook.com/")

time.sleep(1)

phone_number = local_driver.find_element(By.XPATH, "//*[@id='email']")
phone_number.send_keys("9392132411")

time.sleep(2)

password = local_driver.find_element(By.XPATH, "//*[@id='pass']")
password.send_keys("Avinash@1")

time.sleep(2)

login = local_driver.find_element(By.XPATH, "//*[text()='Log In']")#//*[@id="loginbutton"] //*[@id="u_0_d_dS"]
login.click()

time.sleep(2)


# local_driver.close()

