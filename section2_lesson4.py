import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.ID, "input_value").text)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(calc(x))

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    time.sleep(5)
    pyperclip.copy(browser.switch_to.alert.text.split(":")[-1].strip())