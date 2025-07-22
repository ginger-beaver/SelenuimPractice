from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import pyperclip

def calc(x):

    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn").click()

    browser.switch_to.alert.accept()

    parsed_x = int(browser.find_element(By.ID, "input_value").text)

    browser.find_element(By.ID, "answer").send_keys(calc(parsed_x))

    browser.find_element(By.CLASS_NAME, "btn").click()

    alert_text = browser.switch_to.alert.text
    accept_code = alert_text.split(':')[-1].strip()
    print(pyperclip.copy(accept_code))











