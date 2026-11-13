import pytest
import time
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.responsive_utils import set_viewport

@pytest.mark.ui
class TestLoginResponsiveness:
    """
    Test suite - Name : LogIn page_Responsiveness
    Details : Basic Test Cases for LogIn page_Responsiveness
    """
    def test_tc_22_responsiveness_for_laptop_screen(self, page: Page):
        """
        Test Case - TC# : 22
        Name : Responsiveness for Laptop Screen
        Summary : Verify if the LogIn page displays correctly and is responsive for the Laptop screen size 
        """
        set_viewport(page, "laptop")
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.check_login_page_loaded()
        time.sleep(2)

    def test_tc_23_responsiveness_for_pc_screen(self, page: Page):
        """
        Test Case - TC# : 23
        Name : Responsiveness for PC Screen
        Summary : Verify if the LogIn page displays correctly and is responsive for the PC screen size 
        """
        set_viewport(page, "pc")
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.check_login_page_loaded()
        time.sleep(2)

    def test_tc_24_responsiveness_for_ipad_screen(self, page: Page):
        """
        Test Case - TC# : 24
        Name : Responsiveness for IPad Screen
        Summary :  Verify if the Login page displays correctly and is responsive for the iPad screen size using Google DevTools
        """
        set_viewport(page, "ipad")
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.check_login_page_loaded()
        time.sleep(2)