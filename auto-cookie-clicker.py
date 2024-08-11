from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
timeout = time.time() + 10
five_min = time.time() + 60*5

upgrade_items = driver.find_elements(By.CSS_SELECTOR, value="#store div" )
upgrade_items_ids = [item.get_attribute("id") for item in upgrade_items]

def select_upgrade():

    money_content = driver.find_element(By.ID, value='money').text
    money = int(money_content.replace(",", ""))

    items = driver.find_elements(By.CSS_SELECTOR, value='#store b')
    affordable_item_prices = []

    for item in items:
        text_content = item.text
        if text_content != "":
            try:
                item_money = int(text_content.split('-')[-1].strip().replace(",", ""))
                if item_money <= money:
                    affordable_item_prices.append(item_money)
            except ValueError:
                continue
    if affordable_item_prices:
        cookie_upgrades = {}
        for n in range(len(affordable_item_prices)):
            cookie_upgrades[affordable_item_prices[n]] = upgrade_items_ids[n]

        most_expensive_item = max(affordable_item_prices)

        if most_expensive_item in cookie_upgrades:
            item_id = cookie_upgrades[most_expensive_item]
            try:
                chosen_item = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, item_id))
                )
                chosen_item.click()
            except TimeoutException:
                print(f"Failed to click item {item_id} within 5 seconds. Continuing..")

while True:
    cookie.click()
    if time.time() > timeout:
        select_upgrade()
        timeout = time.time()

    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, value="cps").text
        print(cookie_per_second)
        break
