import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        with self.driver as browser:
            browser.get(link)
            test_values = zip(("first", "second", "third"), ("Michael", "Wilcox", "parkerchelsea@example.com"))
            for selector, value in test_values:
                field = browser.find_element(By.CSS_SELECTOR, f".first_block input.{selector}")
                field.send_keys(value)

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            congratulations_text = browser.find_element(By.TAG_NAME, "h1").text

            return congratulations_text
    def test_form1(self):
        link = "https://suninjuly.github.io/registration1.html"
        text = self.fill_form(link)

        self.assertEqual(text, "Congratulations! You have successfully registered!")

    def test_form2(self):
        link = "https://suninjuly.github.io/registration2.html"
        text = self.fill_form(link)

        self.assertEqual(text, "Congratulations! You have successfully registered!")



if __name__ == "__main__":
    unittest.main()