import pytest
import time
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestLoginUIElements:
    """
    Test suite - Name : Log-In Form UI Element
    Details : Basic test cases for Log-In Form UI Element
    """
    def test_tc_01_verify_ui_elements(self, page: Page):
        """
        Test Case - TC# : 01
        Name : Verify UI elements
        Summary : Check that All UI elements are present on the LogIn page
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.verify_ui_elements()
        time.sleep(2)

    def test_tc_02_check_placeholder_text(self, page: Page):
        """
        Test Case - TC# : 02
        Name : Check Placeholder text
        Summary : Check that placeholder text in the Email and password fields is correct
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.check_placeholder_visibility()
        time.sleep(2)