from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_action2:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


        
        self.finish_button = (By.XPATH, '//*[@id="finish"]')
        self.back_home_button = (By.XPATH, '//*[@id="back-to-products"]')
        self.generate_report = (By.XPATH, '//*[@id="generate-pdf-order"]')


    def click_finish_button(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def generate_reporrt(self):
        self.wait.until(EC.element_to_be_clickable(self.generate_report)).click()

    def back_home(self):
        self.wait.until(EC.element_to_be_clickable(self.back_home_button)).click()