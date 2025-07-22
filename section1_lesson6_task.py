from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# https://suninjuly.github.io/registration1.html

link = "https://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    selectors = ("first", "second", "third")
    values = ("Michael", "Wilcox", "parkerchelsea@example.com")

    for selector, value in zip(selectors, values):
        # Селектор ".CLASS TAG.CLASS"
        field = browser.find_element(By.CSS_SELECTOR, f".first_block input.{selector}")
        field.send_keys(value)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    sleep(1)

    congratulations_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == congratulations_text


