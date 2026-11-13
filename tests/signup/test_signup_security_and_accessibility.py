import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignUpSecurityAndAccessibility:
    """
    Test suite - Name : Signup Security and Accessibility
    Details : Basic test cases for the Security and Accessibility functionality of LogIn
    """
    def test_tc_15_verify_password_masking(self, page: Page):
        """
        Test Case - TC# : 15
        Name : Password Masking
        Summary : Verify that the Password is masked when typed
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        PASSWORD = config.get_password()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.check_password_masking(PASSWORD)
        time.sleep(2)

    def test_tc_16_toggle_password_visibility(self, page: Page):
        """
        Test Case - TC# : 16
        Name : Toggle Password Visibility
        Summary : Verify that "eye" icon toggles password visibility
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        PASSWORD = config.get_password()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.toggle_password_visibility(PASSWORD)
        time.sleep(2)