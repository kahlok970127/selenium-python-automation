from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_out_complete(driver, cart_page, checkout_page, checkout_page2):
    cart_page.open_cart()
    cart_page.checkout_cart()

    checkout_page.enter_first_name("firstname")
    checkout_page.enter_last_name("lastname")
    checkout_page.enter_postal_code("postal_code")
    checkout_page.click_continue_button()
    checkout_page2.click_finish_button()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-complete.html"))


def test_generate_pdf(driver, cart_page, checkout_page, checkout_page2):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.enter_first_name("firstname")
    checkout_page.enter_last_name("lastname")
    checkout_page.enter_postal_code("postal_code")
    checkout_page.click_continue_button()
    checkout_page2.click_finish_button()
    download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(checkout_page2.generate_report))
    download_button.click()



def test_check_out_complete_backhome(driver, cart_page, checkout_page, checkout_page2):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.enter_first_name("firstname")
    checkout_page.enter_last_name("lastname")
    checkout_page.enter_postal_code("postal_code")
    checkout_page.click_continue_button()
    checkout_page2.click_finish_button()
    checkout_page2.back_home()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))