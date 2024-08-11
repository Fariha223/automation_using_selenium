from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

#if no linkedIn acc then create acc
Email = "your_login_email"
password = "your_pass"
phone = "your_num"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer&location=London%2C%20England%2C%20"
    "United%20Kingdom&redirect=false&position=1&pageNum=0"
)

def close_and_discard():

    close = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close.click()

    time.sleep(2)
    discard = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard.click()



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

input("Press Enter when you have solved the Puzzle")

time.sleep(3)
list_of_jobs = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in list_of_jobs:
    job.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        number = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if number.text == "":
            number.send_keys(phone)

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        submit_button_attribute = submit_button.get_attribute("aria-label")

        if submit_button_attribute == "Continue to next step":
            close_and_discard()
            continue

        else:
            submit_button.click()

        time.sleep(2)
        close = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close.click()

    except NoSuchElementException:
        close_and_discard()
        continue

time.sleep(5)
driver.quit()
