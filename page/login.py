
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Auth_action:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username = (By.XPATH, '//*[@id="user-name"]')
        self.password = (By.XPATH, '//*[@id="password"]')
        self.loginbutton = (By.XPATH, '//*[@id="login-button"]')
        self.error = (By.XPATH, '//*[@data-test="error"]')


    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.wait.until(EC.visibility_of_element_located(self.username))
        username_input.send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginbutton).click()

    def login_with_enter(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.wait.until(EC.visibility_of_element_located(self.username))
        username_input.send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.password).send_keys(Keys.ENTER)

    def verify_login_success(self):
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))


    def verify_login_failed(self):
        self.wait.until(EC.visibility_of_element_located(self.error))
