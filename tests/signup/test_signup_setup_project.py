import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignUpSetupProject:
    """
    Test suite - Name : Set Up Project
    Details : Basic Test Cases for Set Up Project page
    """
    def test_tc_21_setup_project_verify_ui_elements(self, page: Page):
        """
        Test Case - TC# : 21
        Name : Verify UI elements
        Summary : Check that All UI elements are present on the SetUp Project page
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
        sp.verify_create_project_ui_elements()
        time.sleep(2)

    def test_tc_22_setup_project_check_placeholder_text(self, page: Page):
        """
        Test Case - TC# : 22
        Name : Check Placeholder text
        Summary : Check that placeholder text in the "Project" field is correct
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
        sp.verify_placeholder_texts("New Project", "Project name input placeholder text not visible")
        time.sleep(2)

    def test_tc_23_setup_project_verify_create_first_project_with_valid_name(self, page: Page):
        """
        Test Case - TC# : 23
        Name : Verify Create first project with valid name
        Summary : Check whether the user can create a project with a valid name.
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
        sp.verify_create_project()
        time.sleep(2)
        sp.verify_text_visible("Add your first tasks", "setup project not successful")
        time.sleep(2)

    def test_tc_24_setup_project_verify_create_project_with_imported_template(self, page: Page):
        """
        Test Case - TC# : 24
        Name : Verify Create project with imported template
        Summary : Check whether the user can create a project using the Imported Template
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
        sp.verify_import_project()
        time.sleep(2)

    def test_tc_25_setup_project_verify_create_project_with_imported_template(self, page: Page):
        """
        Test Case - TC# : 25
        Name : Verify Project Setup with Empty field
        Summary : Checks whether the user is unable to set up a project by leaving the Name field empty
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
        sp.verify_create_project_with_empty_name_field()
        time.sleep(2)