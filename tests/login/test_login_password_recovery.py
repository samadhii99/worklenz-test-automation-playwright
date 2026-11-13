import pytest
import time
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.mail_reader import MailReader

@pytest.mark.ui
class TestLoginPasswordRecovery:
    """
    Test suite - Name : Log-in Functionality
    Details : Basic Test Cases for Log-in Functionality
    """
    def test_tc_09_verify_forget_password_link(self, page: Page):
        """
        Test Case - TC# : 09
        Name : Verify "Forget Password" link-text
        Summary : Verify the "Forgot Password" link Functionality
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)

    def test_tc_10_return_to_login(self, page: Page):
        """
        Test Case - TC# : 10
        Name : Verify "Return to LogIn" button
        Summary : Check whether user able to return LogIn Page after clicking "Return to LogIn" button
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.click_return_to_login_button()
        time.sleep(2)

    def test_tc_11_verify_password_reset_and_login(self, page: Page):
        """
        Test Case - TC# : 11
        Name : Verify Reset Password and Log In
        Summary : Check whether user is able to reset their password using the "Forgot Password" link and then log in with the new password.
        """
        lp = LoginPage(page)
        config = ConfigReader()
        mr = MailReader("testworklenz")
        EMAIL = config.get_secondary_email()
        PASSWORD = config.get_new_password()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.reset_password(EMAIL)
        time.sleep(1)
        lp.response_message_visible("If an account with that email exists, a password reset link has been sent to your email.", "Password reset failed")
        lp.response_message_visible("Reset instruction sent!", "Password reset failed")
        time.sleep(2)
        reset_link = mr.get_reset_link_mailinator(page)
        time.sleep(2)
        lp.add_new_password(PASSWORD, reset_link)
        time.sleep(1)
        lp.check_login_page_loaded()
        time.sleep(2)
        lp.enter_credentials(EMAIL, PASSWORD)
        time.sleep(1)
        lp.response_message_visible("You have successfully logged in!", "Login with new password failed")
        time.sleep(2)

    def test_tc_12_verify_reset_password_with_invalid_email(self, page: Page):
        """
        Test Case - TC# : 12
        Name : Verify Reset Password with Invalid Email
        Summary : Check whether user unable to continue reset password process with Invalid Email password
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.reset_password("invalid-email.com")
        time.sleep(1)
        lp.response_message_visible("Please enter your Email!", "Password reset with invalid email failed")
        time.sleep(2)

################################################################################################################
    # def test_tc_13_verify_reset_password_with_unregistered_email(self, page: Page):
    #     """
    #     Test Case - TC# : 13
    #     Name : Verify Reset Password with Unregistered Email Address
    #     Summary : Check that an error message is displayed when a user attempts to reset the password with an email address that is not associated with any account.
    #     """
    #     lp = LoginPage(page)
    #     config = ConfigReader()
    #     lp.navigate(config.get_application_url())
    #     time.sleep(3)
    #     lp.accept_cookies_if_present()
    #     time.sleep(2)
    #     lp.click_forgot_password_link()
    #     time.sleep(2)
    #     lp.reset_password("test@email.com")
    #     time.sleep(1)
    #     lp.response_message_visible("Account does not exists!.", "Password reset with unregistered email failed")
    #     time.sleep(2)
################################################################################################################

    def test_tc_14_verify_error_message_for_empty_input_field(self, page: Page):
        """
        Test Case - TC# : 14
        Name : Verify Error Message for Empty Input Field
        Summary : Check that an error message appears when required fields are left empty during password reset.
        """
        lp = LoginPage(page)
        config = ConfigReader()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.reset_password("")
        time.sleep(1)
        lp.response_message_visible("Please enter your Email!", "Password reset with empty email failed")
        time.sleep(2)

    def test_tc_15_verify_reset_password_with_weak_password_without_symbol(self, page: Page):
        """
        Test Case - TC# : 15
        Name : Verify Reset Password with weak password without symbol
        Summary : Check that user unable  Reset Password with a weak password with 8 Characters without symbol.
        """
        lp = LoginPage(page)
        config = ConfigReader()
        mr = MailReader("testworklenz")
        EMAIL = config.get_secondary_email()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.reset_password(EMAIL)
        time.sleep(1)
        lp.response_message_visible("If an account with that email exists, a password reset link has been sent to your email.", "Password reset failed")
        lp.response_message_visible("Reset instruction sent!", "Password reset failed")
        time.sleep(2)
        reset_link = mr.get_reset_link_mailinator(page)
        time.sleep(2)
        lp.add_new_password("Test1234", reset_link)
        time.sleep(1)
        lp.response_message_visible("Minimum of 8 characters, with upper and lowercase and a number and a symbol.", "Reset password without symbol failed")
        time.sleep(2)

    def test_tc_16_verify_reset_password_with_weak_password_without_uppercase(self, page: Page):
        """
        Test Case - TC# : 16
        Name : Verify  Reset Password with weak password without Uppercase letter
        Summary : Check that user is unable Reset the Password with a weak password with 8 Characters without Uppercase letter
        """
        lp = LoginPage(page)
        config = ConfigReader()
        mr = MailReader("testworklenz")
        EMAIL = config.get_secondary_email()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.reset_password(EMAIL)
        time.sleep(1)
        lp.response_message_visible("If an account with that email exists, a password reset link has been sent to your email.", "Password reset failed")
        lp.response_message_visible("Reset instruction sent!", "Password reset failed")
        time.sleep(2)
        reset_link = mr.get_reset_link_mailinator(page)
        time.sleep(2)
        lp.add_new_password("test123@", reset_link)
        time.sleep(1)
        lp.response_message_visible("Minimum of 8 characters, with upper and lowercase and a number and a symbol.", "Reset password without uppercase failed")
        time.sleep(2)

    def test_tc_17_verify_reset_password_with_weak_password_without_8_characters(self, page: Page):
        """
        Test Case - TC# : 17
        Name : Verify  Reset Password with weak password without 8 Characters
        Summary : Check that user unable  Reset Password with a weak password without 8 Characters 
        """
        lp = LoginPage(page)
        config = ConfigReader()
        mr = MailReader("testworklenz")
        EMAIL = config.get_secondary_email()
        lp.navigate(config.get_application_url())
        time.sleep(3)
        lp.accept_cookies_if_present()
        time.sleep(2)
        lp.click_forgot_password_link()
        time.sleep(2)
        lp.reset_password(EMAIL)
        time.sleep(1)
        lp.response_message_visible("If an account with that email exists, a password reset link has been sent to your email.", "Password reset failed")
        lp.response_message_visible("Reset instruction sent!", "Password reset failed")
        time.sleep(2)
        reset_link = mr.get_reset_link_mailinator(page)
        time.sleep(2)
        lp.add_new_password("Test12@", reset_link)
        time.sleep(1)
        lp.response_message_visible("Minimum of 8 characters, with upper and lowercase and a number and a symbol.", "Reset password without uppercase failed")
        time.sleep(2)