from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_action:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


        self.first_name = (By.XPATH, '//*[@id="first-name"]')
        self.last_name = (By.XPATH, '//*[@id="last-name"]')
        self.postal_code = (By.XPATH, '//*[@id="postal-code"]')
        self.continue_button = (By.XPATH, '//*[@id="continue"]')
        self.cancel_button = (By.XPATH, '//*[@id="cancel"]')
        self.error = (By.XPATH, '//*[@data-test="error"]')


    def enter_first_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(name)

    def enter_last_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys(name)

    def enter_postal_code(self, code):
        self.wait.until(EC.visibility_of_element_located(self.postal_code)).send_keys(code)

    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()