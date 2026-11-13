import pytest
import time
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestLoginSecurityAndAccessibility:
    """
    Test suite - Name : LogIn_Security and Accessebility
    Details : Basic test cases for the Security and Accessibility functionality of LogIn
    """
    def test_tc_20_verify_password_masking(self, page: Page):
        """
        Test Case - TC# : 20
        Name : Password Masking
        Summary : Verify that the Password is masked when typed
        """
        lp = LoginPage(page)
        config = ConfigReader()
        PASSWORD = config.get_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.check_password_masking(PASSWORD)
        time.sleep(2)

    def test_tc_21_toggle_password_visibility(self, page: Page):
        """
        Test Case - TC# : 21
        Name : Toggle Password Visibility
        Summary : Verify that "eye" icon toggles password visibility
        """
        lp = LoginPage(page)
        config = ConfigReader()
        PASSWORD = config.get_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.toggle_password_visibility(PASSWORD)
        time.sleep(2)