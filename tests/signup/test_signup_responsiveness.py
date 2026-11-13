import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader
from utilities.responsive_utils import set_viewport

@pytest.mark.ui
class TestLoginResponsiveness:
    """
    Test suite - Name : Sign up page_Responsiveness
    Details : Basic Test Cases for Sign up page_Responsiveness
    """
    def test_tc_39_responsiveness_for_laptop_screen(self, page: Page):
        """
        Test Case - TC# : 39
        Name : Responsiveness for Laptop Screen
        Summary : Verify if the LogIn page displays correctly and is responsive for the Laptop screen size 
        """
        set_viewport(page, "laptop")
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

    def test_tc_40_responsiveness_for_pc_screen(self, page: Page):
        """
        Test Case - TC# : 40
        Name : Responsiveness for PC Screen
        Summary : Verify if the LogIn page displays correctly and is responsive for the PC screen size 
        """
        set_viewport(page, "pc")
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

    def test_tc_41_responsiveness_for_ipad_screen(self, page: Page):
        """
        Test Case - TC# : 41
        Name : Responsiveness for IPad Screen
        Summary :  Verify if the Login page displays correctly and is responsive for the iPad screen size using Google DevTools
        """
        set_viewport(page, "ipad")
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