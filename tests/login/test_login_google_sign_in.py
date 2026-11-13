import pytest
import time
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.mail_reader import MailReader

@pytest.mark.ui
class TestLoginGoogleSignIn:
    """
    Test suite - Name : Sign-in with Google
    Details : Basic test cases for sign-in with Google Functionality
    """
    def test_tc_18_verify_sign_in_with_google(self, page: Page):
        """
        Test Case - TC# : 18
        Name : Verify SignIn with Google for Existing Worklenz Account
        Summary : Check whether user able to login using signIn with Google option
        """
        lp = LoginPage(page)
        config = ConfigReader()
        EMAIL = config.get_google_email()
        PASSWORD = config.get_google_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_google_signin()
        time.sleep(2)
        lp.google_signin(EMAIL, PASSWORD)
        time.sleep(2)
        lp.verify_homepage_loaded()
        time.sleep(2)

################################################################################################################
    # def test_tc_19_verify_sign_in_with_google_for_new_worklenz_account(self, page: Page):
    #     """
    #     Test Case - TC# : 19
    #     Name : Verify SignIn with Google for new Worklenz Account
    #     Summary : Check whether user able to login using signIn with Google with new Google account
    #     """
    #     lp = LoginPage(page)
    #     config = ConfigReader()
    #     EMAIL = config.get_google_email()
    #     PASSWORD = config.get_google_password()
    #     lp.navigate(config.get_application_url())
    #     time.sleep(3)
    #     lp.accept_cookies_if_present()
    #     time.sleep(2)
    #     lp.click_google_signin()
    #     time.sleep(2)
    #     lp.google_signin(EMAIL, PASSWORD)
    #     time.sleep(2)
    #     lp.verify_homepage_loaded()
    #     time.sleep(2)
################################################################################################################