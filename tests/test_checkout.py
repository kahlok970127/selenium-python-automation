from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_submit_order(driver, cart_page, checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.enter_first_name("firstname")
    checkout_page.enter_last_name("lastname")
    checkout_page.enter_postal_code("postal_code")
    checkout_page.click_continue_button()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))


def test_empty_all(driver, cart_page, checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.click_continue_button()
    error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(checkout_page.error))
    assert error.text == "Error: First Name is required"


def test_empty_lastname_and_postal(driver, cart_page, checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.enter_first_name("firstname")
    checkout_page.click_continue_button()
    error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(checkout_page.error))
    assert error.text == "Error: Last Name is required"


def test_empty_postal(driver, cart_page, checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.enter_first_name("firstname")
    checkout_page.enter_last_name("lastname")
    checkout_page.click_continue_button()
    error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(checkout_page.error))
    assert error.text == "Error: Postal Code is required"


def test_cancel_checkout(driver, cart_page, checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.click_cancel_button()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))

