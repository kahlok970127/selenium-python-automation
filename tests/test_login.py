
from page.login import Auth_action


def test_login_success(driver):
    auth = Auth_action(driver)
    auth.login("standard_user", "secret_sauce")
    auth.verify_login_success()


def test_login_success_with_enter(driver):
    auth = Auth_action(driver)
    auth.login_with_enter("standard_user", "secret_sauce")
    auth.verify_login_success()


def test_both_empty(driver):
    auth = Auth_action(driver)
    auth.login("", "")
    auth.verify_login_failed()


def test_empty_username(driver):
    auth = Auth_action(driver)
    auth.login("", "secret_sauce")
    auth.verify_login_failed()


def test_empty_password(driver):
    auth = Auth_action(driver)
    auth.login("standard_user", "")
    auth.verify_login_failed()


def test_invalid_username(driver):
    auth = Auth_action(driver)
    auth.login("invaliduser", "secret_sauce")
    auth.verify_login_failed()


def test_invalid_password(driver):
    auth = Auth_action(driver)
    auth.login("standard_user", "inavalid_sauce")
    auth.verify_login_failed()


def test_both_invalid(driver):
    auth = Auth_action(driver)
    auth.login("invalid_user", "invalid_password")
    auth.verify_login_failed()


def test_lockout_user(driver):
    auth = Auth_action(driver)
    auth.login("locked_out_user", "secret_sauce")
    auth.verify_login_failed()


def test_username_case_sensitive(driver):
    auth = Auth_action(driver)
    auth.login("Standard_User", "secret_sauce")
    auth.verify_login_failed()


def test_password_case_sensitive(driver):
    auth = Auth_action(driver)
    auth.login("standard_user", "Secret_Sauce")
    auth.verify_login_failed()


def test_username_spaces(driver):
    auth = Auth_action(driver)
    auth.login(" standard_user ", "secret_sauce")
    auth.verify_login_failed()
