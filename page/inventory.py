
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

class inventory_action:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.inventory_item = (By.XPATH, '//*[@class="inventory_item"]')
        self.addtocart = (By.XPATH,'//button[text()="Add to cart"]')
        self.badge = (By.XPATH,'//*[@class="shopping_cart_badge"]')
        self.removeitem = (By.XPATH,'//button[text()="Remove"]')
        self.prices = (By.XPATH, '//*[@class="inventory_item_price"]')
        self.images = (By.XPATH, '//img[@class="inventory_item_img"]')
        self.sortbutton = (By.XPATH, '//*[@class="product_sort_container"]')
        self.inventory_item_name = (By.CSS_SELECTOR, ".inventory_item_name")


    def add_single_product(self):
        self.wait.until(EC.element_to_be_clickable(self.addtocart)).click()

    def add_multiple_product(self, amount):
        for _ in range(amount):
            self.wait.until(EC.element_to_be_clickable(self.addtocart)).click()

    def remove_single_product(self):
        self.wait.until(EC.element_to_be_clickable(self.removeitem)).click()

    def remove_multiple_product(self, amount):
        for _ in range(amount):
            self.wait.until(EC.element_to_be_clickable(self.removeitem)).click()

    def sort_low_to_high(self):
        Select(self.wait.until(EC.visibility_of_element_located(self.sortbutton))).select_by_value("lohi")
    
    def sort_high_to_low(self):
        Select(self.wait.until(EC.visibility_of_element_located(self.sortbutton))).select_by_value("hilo")


    def sort_name_asc(self):
        Select(self.wait.until(EC.visibility_of_element_located(self.sortbutton))).select_by_value("az")


    def sort_name_desc(self):
        Select(self.wait.until(EC.visibility_of_element_located(self.sortbutton))).select_by_value("za")


    def get_prices(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.prices))
        return [
            float(element.text.replace("$", ""))
            for element in elements
        ]

    def get_names(self):

        elements = self.wait.until(EC.visibility_of_all_elements_located(self.inventory_item_name))
        return [element.text for element in elements]



    def add_certain_item(self, product_name):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.inventory_item))

        for item in items:
            name = item.find_element(*self.inventory_item_name).text

            if name == product_name:
                item.find_element(By.TAG_NAME, "button").click()
                break



    def get_product_price(self, product_name):
        item = self._find_product(product_name)
        return item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text

    def add_multiple_items_with_name(self, product_group):
        for product_name in product_group:
            self.add_certain_item(product_name)

    def _find_product(self, product_name):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.inventory_item))

        for item in items:
            name = item.find_element(*self.inventory_item_name).text

            if name == product_name:
                return item

        raise ValueError(f"Product not found: {product_name}")
