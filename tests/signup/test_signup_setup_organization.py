import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignUpSetupOrganization:
    """
    Test suite - Name : Set Up Organization
    Details : Basic Test Cases for Set Up Organization Page
    """
    def test_tc_17_setup_organization_verify_ui_elements(self, page: Page):
        """
        Test Case - TC# : 17
        Name : Verify UI elements
        Summary : Check that All UI elements are present on the SetUp Organization page
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
        sp.verify_setup_organization_ui_elements()
        time.sleep(2)

    def test_tc_18_setup_organization_check_placeholder_text(self, page: Page):
        """
        Test Case - TC# : 18
        Name : Check Placeholder text
        Summary : Check that placeholder text in the "Organization" fields is correct
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
        sp.verify_placeholder_texts("e.g. Example Team", "Organization name input placeholder text not visible")
        time.sleep(2)

    def test_tc_19_setup_organization_verify_account_setup_with_valid_organization_name(self, page: Page):
        """
        Test Case - TC# : 19
        Name : Verify Account setup with valid organization name
        Summary : Check whether user set up account by adding a valid organization name.
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
        sp.verify_setup_organization()
        time.sleep(2)
        sp.verify_text_visible("Let's create your first project", "setup organization not successful")
        time.sleep(2)

    def test_tc_20_setup_organization_verify_account_setup_with_empty_organization_name(self, page: Page):
        """
        Test Case - TC# : 20
        Name : Verify Account Setup with Empty field
        Summary : Checks whether User unable to set up account by leaving Name field empty
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
        sp.verify_setup_organization_with_empty_name_field()
        time.sleep(2)