import pytest
import time
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestLoginLoginFunctionality:
    """
    Test suite - Name : Log-in Functionality
    Details : Basic Test Cases for Log-in Functionality
    """
    def test_tc_03_verify_successful_login(self, page: Page):
        """
        Test Case - TC# : 03
        Name : Verify Successful LogIn
        Summary : Check whether the user can logIn using a valid registered email and the right password
        """
        lp = LoginPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        PASSWORD = config.get_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.enter_credentials(EMAIL, PASSWORD)
        time.sleep(1)
        lp.response_message_visible("You have successfully logged in!", "Login failed")
        time.sleep(2)

################################################################################################################
    # def test_tc_04_verify_successful_login(self, page: Page):
    #     """
    #     Test Case - TC# : 04
    #     Name : Verify "Remember me" Checkbox
    #     Summary : Verify that the Remember me functionality works correctly
    #     """
    #     lp = LoginPage(page)
    #     config = ConfigReader()
    #     EMAIL = config.get_email()
    #     PASSWORD = config.get_password()
    #     lp.navigate(config.get_application_url())
    #     time.sleep(3)
    #     lp.accept_cookies_if_present()
    #     time.sleep(2)
    #     lp.remember_me_check(True)
    #     time.sleep(2)
    #     lp.enter_credentials(EMAIL, PASSWORD)
    #     time.sleep(1)
    #     lp.response_message_visible("You have successfully logged in!", "Login failed")
    #     time.sleep(2)
    #     lp.logout()
    #     time.sleep(2)
    #     lp.accept_cookies_if_present()
    #     time.sleep(2)
    #     lp.check_remembered_credentials(EMAIL)
################################################################################################################

    def test_tc_05_verify_sign_up_link(self, page: Page):
        """
        Test Case - TC# : 05
        Name : Verify "SignUp" link-text 
        Summary : Check whether the user is able to redirect to the Sign Up Page after clicking Sign up.
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_signup_link()
        time.sleep(2)

    def test_tc_06_verify_login_with_invalid_email(self, page: Page):
        """
        Test Case - TC# : 06
        Name : Verify LogIn with Invalid email format
        Summary : Checks whether user unable to logIn when entering invalid email format
        """
        lp = LoginPage(page)
        config = ConfigReader()
        PASSWORD = config.get_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.login_invalid_email("test@.com", PASSWORD)
        time.sleep(1)
        lp.response_message_visible("Please enter a valid email", "Invalid email error message not visible")
        time.sleep(2)

    def test_tc_07_verify_login_with_invalid_credentials(self, page: Page):
        """
        Test Case - TC# : 07
        Name : Verify LogIn with Invalid Credentials
        Summary : Checks whether the user is unable to logIn using invalid credentials
        """
        lp = LoginPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        PASSWORD = config.get_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.login_invalid_credentials(EMAIL, "wrongPassword")
        time.sleep(1)
        lp.response_message_visible("Please check your email and password and try again", "Invalid email error message not visible")
        lp.response_message_visible("Incorrect email or password", "Invalid credentials error message not visible")
        time.sleep(2)
        lp.login_invalid_credentials("test@email.com", PASSWORD)
        time.sleep(1)
        lp.response_message_visible("Please check your email and password and try again", "Invalid email error message not visible")
        lp.response_message_visible("No account found with this email", "Invalid email error message not visible")
        time.sleep(2)

    def test_tc_08_verify_login_with_empty_fields(self, page: Page):
        """
        Test Case - TC# : 08
        Name : Verify LogIn with Empty field
        Summary : Checks whether user unable to logIn with empty fields
        """
        lp = LoginPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.login_empty_credentials(EMAIL)
        time.sleep(1)
        lp.response_message_visible("Please enter your Password!", "Password required error message not visible")
        time.sleep(2)