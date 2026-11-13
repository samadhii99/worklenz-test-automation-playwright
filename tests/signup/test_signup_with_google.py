import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignupWithGoogle:
    """
    Test suite - Name : Sign Up With Google
    Details : Basic test cases for sign up with Google Functionality
    """
    def test_tc_13_verify_sign_up_with_google(self, page: Page):
        """
        Test Case - TC# : 13
        Name : Verify Sign up with new Google Account
        Summary : Check Whether User able to Signup with Google account
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_google_email()
        PASSWORD = config.get_google_password()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.click_google_signup()
        time.sleep(2)
        sp.google_signup(EMAIL, PASSWORD)
        time.sleep(2)
        sp.verify_signup()
        time.sleep(2)

    def test_tc_14_verify_sign_up_with_an_already_registered_google_account(self, page: Page):
        """
        Test Case - TC# : 14
        Name : Verify Sign-Up with an Already Registered Google Account
        Summary : Verify that the user is unable to sign up with a Google account that is already registered to a Worklenz account.
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_google_email()
        PASSWORD = config.get_google_password()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.click_google_signup()
        time.sleep(2)
        sp.google_signup(EMAIL, PASSWORD)
        time.sleep(2)
        sp.verify_homepage_loaded()
        time.sleep(2)