from selenium.webdriver.support import expected_conditions as EC


def test_product_show_in_cart(inventory_page, cart_page):
    inventory_page.add_multiple_product(2)
    cart_page.open_cart()

    items = cart_page.wait.until(EC.visibility_of_all_elements_located(cart_page.cart_items))
    assert len(items) == 2


def test_cart_innertext_count(inventory_page, cart_page):
    inventory_page.add_multiple_product(3)
    badge = cart_page.wait.until(EC.visibility_of_element_located(cart_page.shopping_cart_badge))
    assert badge.text == "3"


def test_certain_product_name_match_in_cart(inventory_page, cart_page):
    inventory_page.add_certain_item("Sauce Labs Bike Light")
    cart_page.open_cart()

    name = cart_page.wait.until(EC.visibility_of_element_located(cart_page.inventory_item_name))
    assert name.text == "Sauce Labs Bike Light"


def test_added_item_price_match_in_cart(inventory_page, cart_page):
    inventory_price = inventory_page.get_product_price("Sauce Labs Bike Light")
    inventory_page.add_certain_item("Sauce Labs Bike Light")
    cart_page.open_cart()

    price = cart_page.wait.until(EC.visibility_of_element_located(cart_page.inventory_item_price))
    assert price.text == inventory_price


def test_added_multiple_item_match_in_cart(inventory_page, cart_page):
    product_group = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    inventory_page.add_multiple_items_with_name(product_group)
    cart_page.open_cart()
    cart_page.wait.until(EC.visibility_of_all_elements_located(cart_page.cart_items))

    cart_items = [
        item.text for item in cart_page.driver.find_elements(*cart_page.inventory_item_name)
    ]
    assert set(cart_items) == set(product_group)


def test_remove_product(inventory_page, cart_page):
    inventory_page.add_certain_item("Sauce Labs Bike Light")
    cart_page.open_cart()
    cart_page.wait.until(EC.visibility_of_all_elements_located(cart_page.cart_items))
    cart_page.remove_certain_product("Sauce Labs Bike Light")
    assert cart_page.wait.until(EC.invisibility_of_element_located(cart_page.shopping_cart_badge))


def test_remove_multiple_item_with_name(inventory_page, cart_page):
    product_group = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    remove_product_group = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt"
    ]

    inventory_page.add_multiple_items_with_name(product_group)
    cart_page.open_cart()
    cart_page.remove_certain_product(remove_product_group)
    badge = cart_page.wait.until(EC.visibility_of_element_located(cart_page.shopping_cart_badge))
    assert badge.text == "1"


def test_empty_cart(cart_page):
    cart_page.open_cart()
    items = cart_page.driver.find_elements(*cart_page.cart_items)
    assert len(items) == 0


def test_checkout_button(cart_page):
    cart_page.open_cart()
    cart_page.checkout_cart()

    cart_page.wait.until(
        EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))


def test_continue_shopping(cart_page):
    cart_page.open_cart()
    cart_page.continue_shopping()
    cart_page.wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))