import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignupAccountCreation:
    """
    Test suite - Name : Log-in Functionality
    Details : Basic Test Cases for Log-in Functionality
    """
    def test_tc_03_verify_sign_up_with_valid_credentials(self, page: Page):
        """
        Test Case - TC# : 03
        Name : Verify Sign up with valid credentials
        Summary : Check Whether User able to Signup with valid Credentials
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_credentials(None,None)
        time.sleep(1)
        sp.response_message_visible("Successfully signed up!", "signup not successful")
        time.sleep(2)
        sp.verify_signup()
        time.sleep(2)

    def test_tc_04_verify_sign_up_with_already_registered_email(self, page: Page):
        """
        Test Case - TC# : 04
        Name : Verify Sign-Up with Already registered Email 
        Summary : Check that user unable to sign-up with an email address that is already registered
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        PASSWORD = config.get_password()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_credentials(EMAIL,PASSWORD)
        time.sleep(1)
        sp.response_message_visible("Worklenz account already exists for email " + EMAIL + ".", "signup with existing email failed to show error message")
        sp.response_message_visible("Failed to sign up", "signup with existing email failed to show error message")
        time.sleep(2)

    def test_tc_05_verify_sign_up_with_already_registered_email(self, page: Page):
        """
        Test Case - TC# : 05
        Name : Verify Sign-Up with all the Fields empty
        Summary : Check that the system displays an error when required fields are empty
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.click_signup_with_empty_fields()
        time.sleep(2)

    def test_tc_06_verify_sign_up_with_empty_fields(self, page: Page):
        """
        Test Case - TC# : 06
        Name : Verify Sign-Up with empty fields
        Summary : Check that the system displays an error when required fields are empty
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_with_empty_credentials()
        time.sleep(2)

    def test_tc_07_verify_sign_up_with_invalid_email(self, page: Page):
        """
        Test Case - TC# : 07
        Name : Verify Sign-Up with Invalid Email Format
        Summary : Verify that user unable to Signup with Invalid Email Format
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
        sp.enter_signup_credentials("test.com",PASSWORD)
        time.sleep(1)
        sp.verify_placeholder_texts("Please enter your Email!", "Email validation message not visible for invalid email format")
        time.sleep(2)

    def test_tc_08_verify_sign_up_with_weak_password_without_symbol(self, page: Page):
        """
        Test Case - TC# : 08
        Name : Verify Sign-Up with weak password without symbol
        Summary : Verify that user unable sign-up with a weak password with 8 Characters without symbol.
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_credentials(EMAIL,"2211Test")
        time.sleep(1)
        sp.verify_placeholder_texts("Password does not meet the requirements!", "Password criteria message not visible for weak password without symbol")
        time.sleep(2)

    def test_tc_09_verify_sign_up_with_weak_password_without_uppercase(self, page: Page):
        """
        Test Case - TC# : 09
        Name : Verify Sign-Up with weak password without Uppercase letter
        Summary : Verify that user unable sign-up with a weak password with 8 Characters without Uppercase letter
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_credentials(EMAIL,"221@test")
        time.sleep(1)
        sp.verify_placeholder_texts("Password does not meet the requirements!", "Password criteria message not visible for weak password without uppercase letter")
        time.sleep(2)

    def test_tc_10_verify_sign_up_with_weak_password_without_8_characters(self, page: Page):
        """
        Test Case - TC# : 10
        Name : Verify Sign-Up with weak password without 8 Characters
        Summary : Verify that user unable sign-up with a weak password without 8 Characters 
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_credentials(EMAIL,"221@Tes")
        time.sleep(1)
        sp.verify_placeholder_texts("Password must be at least 8 characters!", "Password criteria message not visible for weak password without 8 characters")
        time.sleep(2)

    def test_tc_11_verify_sign_up_only_spaces_in_username(self, page: Page):
        """
        Test Case - TC# : 11
        Name : only spaces as input for Username field
        Summary : Verify that system displays an error message when the username field contains only spaces and prevents sign-up.
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        PASSWORD = config.get_password()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_spaced_username(EMAIL, PASSWORD)
        time.sleep(1)
        sp.verify_placeholder_texts("Please enter your full name!", "Name validation message not visible for username with only spaces")
        sp.verify_placeholder_texts("Full name must be at least 4 characters!", "Name validation message not visible for username with only spaces")
        time.sleep(2)

    def test_tc_12_verify_sign_up_only_spaces_in_password(self, page: Page):
        """
        Test Case - TC# : 12
        Name : Only Spaces as input for Password field
        Summary : Verify that system displays an error message when the password field contains only spaces and prevents sign-up.
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        EMAIL = config.get_email()
        sp.navigate(config.get_application_url())
        time.sleep(3)
        sp.accept_cookies_if_present()
        time.sleep(2)
        sp.click_signup_link()
        time.sleep(2)
        sp.enter_signup_credentials(EMAIL, " ")
        time.sleep(1)
        sp.verify_placeholder_texts("Password must be at least 8 characters!", "Password validation message not visible for password with only spaces")
        sp.verify_placeholder_texts("Password does not meet the requirements!", "Password validation message not visible for password with only spaces")
        time.sleep(2)