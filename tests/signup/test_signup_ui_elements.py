import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignUpUIElements:
    """
    Test suite - Name : Sign-Up Form UI Element
    Details : Basic test cases for Sign-up Form UI Element
    """
    def test_tc_01_verify_ui_elements(self, page: Page):
        """
        Test Case - TC# : 01
        Name : Verify UI elements
        Summary : Check that All UI elements are present on the Sign up page
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.verify_ui_elements()
        time.sleep(2)

    def test_tc_02_check_placeholder_text(self, page: Page):
        """
        Test Case - TC# : 02
        Name : Check Placeholder text
        Summary : Check that placeholder text in the Full Name,Email and password fields is correct
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.check_placeholder_visibility()
        time.sleep(2)