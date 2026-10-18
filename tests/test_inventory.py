import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

def test_item_not_empty(inventory_page):
    items = inventory_page.wait.until(EC.visibility_of_all_elements_located(inventory_page.inventory_item))
    assert len(items) > 0


def test_product_price_not_empty(inventory_page):
    prices = inventory_page.wait.until(EC.visibility_of_all_elements_located(inventory_page.prices))
    assert len(prices) > 0

def test_every_product_image_loaded(inventory_page):

    items = inventory_page.wait.until(EC.visibility_of_all_elements_located(inventory_page.inventory_item))
    images = inventory_page.wait.until(EC.visibility_of_all_elements_located(inventory_page.images))

    assert len(items) == len(images)

    for img in images:
        assert img.is_displayed()
        loaded = inventory_page.driver.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0",img)
        assert loaded

def test_check_add_to_cart_button(inventory_page):
    buttons = inventory_page.wait.until(EC.visibility_of_all_elements_located(inventory_page.addtocart))
    assert len(buttons) > 0


def test_add_product_to_cart(inventory_page):
    inventory_page.add_single_product()
    badge = inventory_page.wait.until(EC.visibility_of_element_located(inventory_page.badge))
    assert badge.text == "1"


def test_add_certain_item(inventory_page):
    inventory_page.add_certain_item("Sauce Labs Bike Light")
    badge = inventory_page.wait.until(EC.visibility_of_element_located(inventory_page.badge))
    assert badge.text == "1"


def test_add_multiple_product_to_cart(inventory_page):
    inventory_page.add_multiple_product(3)
    badge = inventory_page.wait.until(EC.visibility_of_element_located(inventory_page.badge))
    assert badge.text == "3"


def test_add_multiple_item_with_name(inventory_page):
    product_group = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    inventory_page.add_multiple_items_with_name(product_group)
    badge = inventory_page.wait.until(EC.visibility_of_element_located(inventory_page.badge))
    assert badge.text == "3"


def test_remove_product_to_cart(inventory_page):

    inventory_page.add_single_product()
    badge = inventory_page.wait.until(EC.visibility_of_element_located(inventory_page.badge))
    assert badge.text == "1"

    inventory_page.remove_single_product()
    assert inventory_page.wait.until(EC.invisibility_of_element_located(inventory_page.badge))


def test_remove_multiple_product_to_cart(inventory_page):
    inventory_page.add_multiple_product(3)
    inventory_page.remove_multiple_product(2)

    badge = inventory_page.wait.until(EC.visibility_of_element_located(inventory_page.badge))
    assert badge.text == "1"

def test_sort_low_to_high(inventory_page):
    inventory_page.sort_low_to_high()
    prices = inventory_page.get_prices()

    assert prices == sorted(prices)


def test_sort_high_to_low(inventory_page):
    inventory_page.sort_high_to_low()
    prices = inventory_page.get_prices()
    assert prices == sorted(prices, reverse=True)


def test_sort_name_asc(inventory_page):
    inventory_page.sort_name_asc()
    names = inventory_page.get_names()

    assert names == sorted(names)


def test_sort_name_desc(inventory_page):
    inventory_page.sort_name_desc()
    names = inventory_page.get_names()

    assert names == sorted(names, reverse=True)
