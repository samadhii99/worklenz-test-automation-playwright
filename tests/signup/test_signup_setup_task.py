import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader

@pytest.mark.ui
class TestSignUpSetupTask:
    """
    Test suite - Name : Set Up Task
    Details : Basic Test Cases for the input Field in the Set Up Task page
    """
    def test_tc_26_setup_task_verify_ui_elements(self, page: Page):
        """
        Test Case - TC# : 26
        Name : Verify UI elements
        Summary : Check that all UI elements are present on the SetUp Tasks page
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
        sp.verify_create_task_ui_elements()
        time.sleep(2)

    def test_tc_27_setup_task_check_placeholder_text(self, page: Page):
        """
        Test Case - TC# : 27
        Name : Check Placeholder text
        Summary : Check that all UI elements are present on the SetUp Tasks page
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
        sp.verify_placeholder_texts("Task 1 - e.g., What needs to be done?", "Task name input placeholder text not visible")
        time.sleep(2)

    def test_tc_28_setup_task_verify_create_task(self, page: Page):
        """
        Test Case - TC# : 28
        Name : Verify Create a task for Project
        Summary : Check whether the user can create a   task for project
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
        sp.verify_create_task(False)
        time.sleep(2)
        sp.verify_text_visible("Invite your team", "setup task not successful")
        time.sleep(2)

    def test_tc_29_setup_task_verify_create_more_tasks(self, page: Page):
        """
        Test Case - TC# : 29
        Name : Verify Create more tasks for project
        Summary : Check whether the user can create more tasks for project
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
        sp.verify_create_task(True)
        time.sleep(2)
        sp.verify_text_visible("Invite your team", "setup task not successful")
        time.sleep(2)

    def test_tc_30_setup_task_verify_delete_task(self, page: Page):
        """
        Test Case - TC# : 30
        Name : Verify Delete the task
        Summary : Checks whether user can delete task two by clicking delete icon
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
        sp.verify_delete_created_task()
        time.sleep(2)

    def test_tc_31_setup_task_verify_task_set_up_with_empty_field(self, page: Page):
        """
        Test Case - TC# : 31
        Name : Verify Task Set Up with Empty field
        Summary : Checks whether the user is unable to set up the task by leaving the task field empty
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
        sp.verify_create_task_with_empty_name_field()
        time.sleep(2)