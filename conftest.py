
import pytest
from selenium import webdriver
from page.login import Auth_action
from page.inventory import inventory_action
from page.shopping_cart import Cart_action
from page.checkout import Checkout_action
from page.checkout2 import Checkout_action2


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Run Chrome in headless mode (no visible browser window)
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_page(driver):
    auth = Auth_action(driver)
    auth.login("standard_user", "secret_sauce")
    auth.verify_login_success()
    return driver


@pytest.fixture
def inventory_page(logged_in_page):
    return inventory_action(logged_in_page)


@pytest.fixture
def cart_page(logged_in_page):
    return Cart_action(logged_in_page)


@pytest.fixture
def checkout_page(logged_in_page):
    return Checkout_action(logged_in_page)


@pytest.fixture
def checkout_page2(logged_in_page):
    return Checkout_action2(logged_in_page)
