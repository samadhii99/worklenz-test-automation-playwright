import email
import time
import sys
import os
import random
from faker import Faker
from playwright.sync_api import Page, expect
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pages.base_page import BasePage


class SignUpPage(BasePage):
    """Login page object using Playwright"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.faker = Faker()
        # Using selectors from existing converted login page
        self.email_input = "input#login_email"
        self.password_input = "input#login_password"
        self.signup_link = "//a[@href='/auth/signup']"
        self.signup_name = "input#signup_name"
        self.signup_email_input = "input#signup_email"
        self.password_input = "//input[@type='password']"
        self.remember_me_checkbox = "//*[@id='login_remember']"
        self.forgot_password_link = "//a[@href='/auth/forgot-password']"
        self.signup_button = "//button[@type='submit']"
        self.cookie_accept_button = "//button[@aria-label='Accept analytics cookies']"
        self.cookie_banner = "h3#cookie-consent-title"
        self.privacy_policy_link = "//a[@href='https://worklenz.com/privacy/']"
        self.terms_of_use_link = "//a[@href='https://worklenz.com/terms/']"
        self.google_signup_button = "//button[@type='button' and contains(., 'Google')]"
        self.apple_signup_button = "//button[@type='button' and contains(., 'Apple')]"
        self.login_link = "//a[@href='/auth/login']"
        self.organization_name_input = "//input[@type='text']"
        self.project_name_input = "//input[@type='text']"
        self.task_name_input = "//input[@type='text']"
        self.invite_email_input = "//input[@type='text']"

    def navigate(self, url: str = None):
        """Navigate to login page"""
        if url is None:
            url = "https://react.worklenz.com/auth/login"
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def accept_cookies_if_present(self):
        """Accept cookies if cookie banner is present"""
        if self.page.locator(self.cookie_banner).is_visible(timeout=6000):
            self.page.locator(self.cookie_accept_button).click()

    def click_signup_link(self):
        """Click on the Sign Up link"""
        self.page.locator(self.signup_link).click()
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/auth/signup"), "Not redirected to Sign Up page after clicking Sign up link"

    def response_message_visible(self, message: str, error: str) -> bool:
        """Check if error message is visible"""
        assert self.page.get_by_text(message).is_visible(timeout=5000),error
        
    def verify_ui_elements(self):
        assert self.page.locator(self.signup_name).is_visible(), "Name input not visible"
        assert self.page.locator(self.signup_email_input).is_visible(), "Email input not visible"
        assert self.page.locator(self.password_input).is_visible(), "Password input not visible"
        assert self.page.get_by_text("Password must be at least 8").is_visible(), "Password criteria text not visible"
        assert self.page.locator(self.signup_button).is_visible(), "Sign Up button not visible"
        assert self.page.locator(self.google_signup_button).is_visible(), "Signup with Google button not visible"
        assert self.page.locator(self.apple_signup_button).is_visible(), "Signup with Apple button not visible"
        assert self.page.locator(self.login_link).is_visible(), "Login link not visible"

        self.page.locator(self.signup_button).click()
        self.wait_for_timeout(2000)
        assert self.page.get_by_text("Please enter your full name!").is_visible(), "Name required message not visible"
        assert self.page.get_by_text("Please enter your Email!").is_visible(), "Email required message not visible"
        assert self.page.get_by_text("Please enter your Password!").is_visible(), "Password required message not visible"

    def check_placeholder_visibility(self):
        assert self.page.get_by_placeholder("Enter your full name").is_visible(), "Name input placeholder not visible"
        assert self.page.get_by_placeholder("Enter your email").is_visible(), "Email input placeholder not visible"
        assert self.page.get_by_placeholder("Enter a stronger password").is_visible(), "Password input placeholder not visible"

    def enter_signup_credentials(self, email: str, password: str):
        """Enter signup credentials"""
        name = self.faker.name()
        if email is None:
            email = self.faker.email()
        if password is None:
            password = self.faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        self.page.fill(self.signup_name, name)
        self.page.fill(self.signup_email_input, email)
        self.page.fill(self.password_input, password)
        self.page.wait_for_timeout(3000)
        self.page.locator(self.signup_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def verify_signup(self):
        """Verify successful signup"""
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/worklenz/setup"), "Not redirected to dashboard after signup"

    def click_signup_with_empty_fields(self):
        """Click signup with empty fields"""
        self.page.locator(self.signup_button).click()
        self.page.wait_for_timeout(2000)
        assert self.page.get_by_text("Please enter your full name!").is_visible(), "Name required message not visible"
        assert self.page.get_by_text("Please enter your Email!").is_visible(), "Email required message not visible"
        assert self.page.get_by_text("Please enter your Password!").is_visible(), "Password required message not visible"

    def enter_signup_with_empty_credentials(self):
        """Enter signup credentials"""
        name = self.faker.name()
        self.page.fill(self.signup_name, name)
        self.page.wait_for_timeout(3000)
        self.page.locator(self.signup_button).click()
        self.page.wait_for_timeout(3000)

        assert self.page.get_by_text("Please enter your Email!").is_visible(), "Email required message not visible"
        assert self.page.get_by_text("Please enter your Password!").is_visible(), "Password required message not visible"

    def verify_placeholder_texts(self, placeholder: str, error: str) -> bool:
        """Verify placeholder texts"""
        assert self.page.get_by_placeholder(placeholder).is_visible(timeout=5000),error

    def enter_spaced_username(self, email: str, password: str):
        """Enter signup credentials with spaces in username"""
        name = " "
        self.page.fill(self.signup_name, name)
        self.page.fill(self.signup_email_input, email)
        self.page.fill(self.password_input, password)
        self.page.wait_for_timeout(3000)
        self.page.locator(self.signup_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def google_signup(self, email: str, password: str):
        """Perform Google sign-up"""
        self.page.locator("input[type='email']").fill(email)
        self.page.locator("button:has-text('Next')").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("input[type='password']").fill(password)
        self.page.locator("button:has-text('Next')").click()
        self.page.wait_for_timeout(2000)
        continue_button = self.page.get_by_role("button", name="Continue")
        if continue_button.is_visible(timeout=5000): continue_button.click()
        self.page.wait_for_timeout(5000)
        pass

    def click_google_signup(self):
        """Click Google sign-up button"""
        self.accept_cookies_if_present()
        self.page.locator(self.google_signup_button).click()

    def verify_homepage_loaded(self):
        """Verify if homepage is loaded by checking for a known element"""
        dashboard_element = self.page.locator("div.ant-flex-vertical.ant-flex-align-center")
        assert dashboard_element.is_visible(timeout=10000), "Homepage not loaded properly"

    def check_password_masking(self, password: str):
        self.page.fill(self.password_input, password)
        input_type = self.page.locator(self.password_input).get_attribute("type")
        assert input_type == "password", "Password is not masked in the password input field"
        pass

    def toggle_password_visibility(self, password: str):
        self.page.fill(self.password_input, password)
        invisible_eye_icon = self.page.get_by_label("eye-invisible").locator("svg")
        visible_eye_icon = self.page.get_by_label("eye").locator("path")

        if invisible_eye_icon.is_visible():
            invisible_eye_icon.click()
        elif visible_eye_icon.is_visible():
            pass

        toggeled_password = self.page.get_by_placeholder("Enter a stronger password").input_value()
        assert toggeled_password == password, "Password visibility toggle failed"
        pass

    def verify_setup_organization_ui_elements(self):
        assert self.page.locator(self.organization_name_input).is_visible(), "Organization Name input not visible"
        assert self.page.get_by_role("button", name="Continue").is_visible(), "Continue button not visible"

    def verify_setup_organization(self):
        org_name = self.faker.company()
        self.page.fill(self.organization_name_input, org_name)
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(3000)
        pass

    def verify_text_visible(self, text: str, error: str) -> bool:
        """Verify text visible"""
        assert self.page.get_by_text(text).is_visible(timeout=5000),error

    def verify_setup_organization_with_empty_name_field(self):
        org_name = ""
        self.page.fill(self.organization_name_input, org_name)
        continue_button = self.page.get_by_role("button", name="Continue")
        assert continue_button.is_disabled(), "Continue organization name with empty name field failed"

    def verify_create_project_ui_elements(self):
        assert self.page.locator(self.project_name_input).is_visible(), "Project Name input not visible"
        assert self.page.locator("button.px-3").first.is_visible(), "Quick suggestions not visible"
        assert self.page.locator(".ant-card-hoverable div.ant-card-body").first.is_visible(), "Project templates cards not visible"
        assert self.page.get_by_role("button", name="🎨 Browse All Templates").is_visible(), "Browse all templates button not visible"
        assert self.page.get_by_role("button", name="Go Back").is_visible(), "Go Back button not visible"
        assert self.page.get_by_role("button", name="Continue").is_visible(), "Continue button not visible"

    def verify_create_project(self):
        project_name = self.faker.company()
        self.page.fill(self.project_name_input, project_name)
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(2000)
        return project_name

    def verify_import_project(self):
        template_project = random.choice(self.page.locator(".ant-card-hoverable div.ant-card-body").all())
        project_name = template_project.locator(".block strong").inner_text().strip()
        template_project.click()
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(5000)
        created_project_name = self.page.get_by_role("heading", name=project_name).inner_text().strip()
        assert project_name == created_project_name, "create project using template failed"

    def verify_create_project_with_empty_name_field(self):
        project_name = ""
        self.page.fill(self.project_name_input, project_name)
        continue_button = self.page.get_by_role("button", name="Continue")
        assert continue_button.is_disabled(), "Continue project name with empty name field failed"

    def verify_create_task_ui_elements(self):
        assert self.page.locator(self.task_name_input).is_visible(), "Task Name input not visible"
        assert self.page.get_by_role("button", name="plus Add another task (1/5)").is_visible(), "Add another task button not visible"
        assert self.page.get_by_role("button", name="Go Back").is_visible(), "Go Back button not visible"
        assert self.page.get_by_role("button", name="Continue").is_visible(), "Continue button not visible"

    def verify_create_task(self, multiple_tasks: bool):
        task_name = self.faker.word()
        task1_input = self.page.get_by_role("textbox", name="Task 1 - e.g., What needs to")
        task2_input = self.page.get_by_role("textbox", name="Task 2 - e.g., What needs to")
        task1_input.fill(task_name)
        if multiple_tasks:
            self.page.get_by_role("button", name="plus Add another task (1/5)").click()
            task2_name = self.faker.word()
            task2_input.fill(task2_name)
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(3000)
        pass

    def verify_delete_created_task(self):
        task_name = self.faker.word()
        task_input = self.page.get_by_role("textbox", name="Task 1 - e.g., What needs to")
        task_input.fill(task_name)
        self.page.get_by_role("button", name="plus Add another task (1/5)").click()
        self.page.get_by_role("button", name="close-circle").first.click()
        assert not self.page.get_by_text(task_name).is_visible(), "Delete task failed"

    def verify_create_task_with_empty_name_field(self):
        task_name = ""
        task_input = self.page.get_by_role("textbox", name="Task 1 - e.g., What needs to")
        task_input.fill(task_name)
        self.page.get_by_role("button", name="Continue")
        task_value = task_input.input_value()
        assert task_value == "", "Continue task name with empty name field failed"

    def verify_invite_members_ui_elements(self):
        invite_email = self.faker.email()
        assert self.page.locator(self.invite_email_input).is_visible(), "Invite Email input not visible"
        assert self.page.get_by_role("button", name="plus Add another team member").is_visible(), "Add another team member button not visible"
        assert self.page.get_by_role("button", name="Skip for now").is_visible(), "Skip for now button not visible"
        assert self.page.get_by_role("button", name="Go Back").is_visible(), "Go Back button not visible"
        assert self.page.get_by_role("button", name="Continue").is_visible(), "Continue button not visible"

        self.page.locator(self.invite_email_input).fill(invite_email)
        self.page.get_by_role("button", name="plus Add another team member").click()
        assert self.page.get_by_role("button", name="close-circle").first.is_visible(), "Delete invite email button not visible"

    def invite_a_team_member(self, email: str, project_name: str):
        invite_email = email
        self.page.locator(self.invite_email_input).fill(invite_email)
        self.page.get_by_role("button", name="Continue").click()
        assert self.page.get_by_text("Valid email address").is_visible(), "Valid email address message not visible"
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(3000)
        created_project_name = self.page.get_by_role("heading", name=project_name).inner_text().strip()
        assert project_name == created_project_name, "Invite a team member failed"

    def invite_team_members(self, email1: str, email2: str, project_name: str):
        invite_email1 = email1
        invite_email2 = email2
        self.page.get_by_placeholder("Team member 1 - Enter email address").fill(invite_email1)
        self.page.get_by_role("button", name="plus Add another team member").click()
        assert self.page.get_by_text("Valid email address").is_visible(), "Valid email address message not visible"
        self.page.get_by_placeholder("Team member 2 - Enter email address").fill(invite_email2)
        self.page.get_by_role("button", name="Continue").click()
        assert self.page.get_by_text("Valid email address").nth(1).is_visible(), "Valid email address message not visible"
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_timeout(3000)
        created_project_name = self.page.get_by_role("heading", name=project_name).inner_text().strip()
        assert project_name == created_project_name, "Invite a team member failed"

    def verify_invited_page_loaded(self):
        """Check if invited page is loaded by invited page url"""
        self.page.wait_for_timeout(3000)
        assert self.page.url.endswith("/worklenz/home"), "Invited page not loaded properly"

    def verify_skip_for_now(self, project_name: str):
        self.page.get_by_role("button", name="Skip for now").click()
        self.page.wait_for_timeout(3000)
        created_project_name = self.page.get_by_role("heading", name=project_name).inner_text().strip()
        assert project_name == created_project_name, "Invite a team member failed"

    def invite_invalid_email(self, email: str):
        invite_email = email
        self.page.locator(self.invite_email_input).fill(invite_email)
        self.page.get_by_role("button", name="plus Add another team member").click()
        assert self.page.get_by_text("Please enter a valid email address").is_visible(), "Invalid email address message not visible"
        assert self.page.get_by_role("button", name="Continue").is_disabled(), "Continue button not disabled"

    def add_empty_email(self):
        invite_email = ""
        self.page.locator(self.invite_email_input).fill(invite_email)
        self.page.get_by_role("button", name="plus Add another team member").click()
        assert self.page.get_by_role("button", name="Continue").is_disabled(), "Continue button not disabled"
