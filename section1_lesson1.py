import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin

link = "https://suninjuly.github.io/get_attribute.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    
    found_expression = browser.find_element(By.CSS_SELECTOR, "h2 span.nowrap")
    parsed_expression = found_expression.text.split()[2].replace("ln", "log")

    found_x = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = int(found_x.get_attribute("valuex"))

    result = eval(parsed_expression)[0]

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(result)
    

    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_box.click()
    

    radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_button.click()
    

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    print(browser.switch_to.alert.text)



