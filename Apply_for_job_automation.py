from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

Email = "your_login"
password = "your_pass"
phone = "your_num"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
)

time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()


time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(Email)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(5)
number = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if number.text == "":
    number.send_keys(phone)

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
