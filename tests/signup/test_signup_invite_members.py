import pytest
import time
from playwright.sync_api import Page
from pages.signup.signup_page import SignUpPage
from utilities.config_reader import ConfigReader
from utilities.mail_reader import MailReader

@pytest.mark.ui
class TestSignUpInviteMembers:
    """
    Test suite - Name : Invite Members
    Details : Basic Test Cases for SetUp members page
    """
    def test_tc_32_invite_members_verify_ui_elements(self, page: Page):
        """
        Test Case - TC# : 32
        Name : Verify UI elements
        Summary : Check that all UI elements are present on the SetUp Members page
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
        sp.verify_invite_members_ui_elements()
        time.sleep(2)

    def test_tc_33_invite_members_check_placeholder_text(self, page: Page):
        """
        Test Case - TC# : 33
        Name : Check Placeholder text
        Summary : Check that the placeholder text in the "Tasks" fields is correct
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
        sp.verify_placeholder_texts("Team member 1 - Enter email address", "Invite email input placeholder text not visible")
        time.sleep(2)

    def test_tc_34_invite_members_verify_add_a_team_member(self, page: Page):
        """
        Test Case - TC# : 34
        Name : Verify Add a Team Member
        Summary : Checks that the user is able to send team invitation email to team members 
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        mr = MailReader("testworklenz")
        EMAIL = config.get_secondary_email()
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
        project_name = sp.verify_create_project()
        time.sleep(2)
        sp.verify_text_visible("Add your first tasks", "setup project not successful")
        time.sleep(2)
        sp.verify_create_task(False)
        time.sleep(2)
        sp.verify_text_visible("Invite your team", "setup task not successful")
        time.sleep(2)
        sp.invite_a_team_member(EMAIL,project_name)
        time.sleep(2)
        invite_link = mr.get_invite_link_mailinator(page)
        time.sleep(2)
        sp.navigate(invite_link)
        time.sleep(3)
        sp.verify_invited_page_loaded()
        time.sleep(2)

    def test_tc_35_invite_members_verify_add_more_team_members(self, page: Page):
        """
        Test Case - TC# : 35
        Name : Verify Add more Team Members
        Summary : Checks that the user is able to send team invitation emails to members more than once
        """
        sp = SignUpPage(page)
        config = ConfigReader()
        mr1 = MailReader("testworklenz")
        mr2 = MailReader("testworklenz2")
        EMAIL1 = config.get_invite_email("inviteEmail1")
        EMAIL2 = config.get_invite_email("inviteEmail2")
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
        project_name = sp.verify_create_project()
        time.sleep(2)
        sp.verify_text_visible("Add your first tasks", "setup project not successful")
        time.sleep(2)
        sp.verify_create_task(False)
        time.sleep(2)
        sp.verify_text_visible("Invite your team", "setup task not successful")
        time.sleep(2)
        sp.invite_team_members(EMAIL1,EMAIL2,project_name)
        time.sleep(2)
        invite_link = mr1.get_invite_link_mailinator(page)
        time.sleep(2)
        sp.navigate(invite_link)
        time.sleep(3)
        sp.verify_invited_page_loaded()
        time.sleep(2)
        invite_link = mr2.get_invite_link_mailinator(page)
        time.sleep(2)
        sp.navigate(invite_link)
        time.sleep(3)
        sp.verify_invited_page_loaded()
        time.sleep(2)

    def test_tc_36_invite_members_verify_skip_for_now(self, page: Page):
        """
        Test Case - TC# : 36
        Name : Verify Skip for Now Option
        Summary : Checks that User able to go Home page without adding team Members
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
        project_name = sp.verify_create_project()
        time.sleep(2)
        sp.verify_text_visible("Add your first tasks", "setup project not successful")
        time.sleep(2)
        sp.verify_create_task(False)
        time.sleep(2)
        sp.verify_text_visible("Invite your team", "setup task not successful")
        time.sleep(2)
        sp.verify_skip_for_now(project_name)
        time.sleep(2)

    def test_tc_37_invite_members_verify_add_invalid_email(self, page: Page):
        """
        Test Case - TC# : 37
        Name : Verify Add an Invalid Email address
        Summary : Checks that the user is unable to send a team invitation for an invalid email format
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
        sp.invite_invalid_email("test.com")
        time.sleep(2)

    def test_tc_38_invite_members_verify_add_team_member_with_empty_field(self, page: Page):
        """
        Test Case - TC# : 38
        Name : Verify Add team member with Empty field
        Summary : Check that the user is unable send a team invitation when the email address field is empty
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
        sp.add_empty_email()
        time.sleep(2)