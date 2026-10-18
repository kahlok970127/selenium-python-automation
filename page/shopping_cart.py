
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_action:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cart_button = (By.XPATH, '//a[@class="shopping_cart_link"]')
        self.cart_items = (By.XPATH, '//*[@class="cart_item"]')
        self.shopping_cart_badge = (By.XPATH, '//*[@class="shopping_cart_badge"]')
        self.inventory_item_name = (By.XPATH, '//*[@class="inventory_item_name"]')
        self.inventory_item_price = (By.XPATH, '//*[@class="inventory_item_price"]')
        self.checkout_button = (By.XPATH, '//*[@id="checkout"]')
        self.continue_shopping_button = (By.XPATH, '//*[@id="continue-shopping"]')


    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()

    
            
    def remove_certain_product(self, product_name):
        if isinstance(product_name, str):
            product_name = [product_name]

        for name in product_name:
            target_locator = (By.XPATH,f"//div[@class='cart_item'][.//div[@class='inventory_item_name' and normalize-space()='{name}']]")
            target_item = self.wait.until(EC.visibility_of_element_located(target_locator))
            target_item.find_element(By.TAG_NAME, "button").click()
            self.wait.until(EC.invisibility_of_element_located(target_locator))

    def checkout_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()

    def continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_shopping_button)).click()
