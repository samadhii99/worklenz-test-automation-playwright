import email
from playwright.sync_api import Page, expect
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object using Playwright"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        # Using selectors from existing converted login page
        self.email_input = "input#login_email"
        self.password_input = "input#login_password"
        self.remember_me_checkbox = "//*[@id='login_remember']"
        self.forgot_password_link = "//a[@href='/auth/forgot-password']"
        self.login_button = "//button[@type='submit']"
        self.cookie_accept_button = "//button[@aria-label='Accept analytics cookies']"
        self.cookie_banner = "h3#cookie-consent-title"
        self.google_signin_button = "//button[@type='button' and contains(., 'Google')]"
        self.apple_signin_button = "//button[@type='button' and contains(., 'Apple')]"
        self.signup_link = "//a[@href='/auth/signup']"
        self.return_to_login_button = "//button[@type='button' and contains(., 'Return to Login')]"
        self.reset_password_button = "//button[@type='submit' and contains(., 'Reset Password')]"
        self.reset_password_email_input = "//*[@id='forgot-password_email']"
        self.new_password_input = "#verify-reset-email_newPassword input"
        self.confirm_password_input = "input#verify-reset-email_confirmPassword"
        self.reset_password_submit_button = "//button[@type='submit' and contains(., 'Reset password')]"

    def navigate(self, url: str = None):
        """Navigate to login page"""
        if url is None:
            url = "https://react.worklenz.com/auth/login"
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
        self.wait_for_timeout(3000)

    def accept_cookies_if_present(self):
        """Accept cookies if cookie banner is present"""
        if self.page.locator(self.cookie_banner).is_visible(timeout=6000):
            self.page.locator(self.cookie_accept_button).click()

    def enter_credentials(self, email: str, password: str):
        """Enter login credentials"""
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.wait_for_timeout(3000)
        self.page.locator(self.login_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def click_google_signin(self):
        """Click Google sign-in button"""
        self.accept_cookies_if_present()
        self.page.locator(self.google_signin_button).click()

    def google_signin(self, email: str, password: str):
        """Perform Google sign-in"""
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

    def response_message_visible(self, message: str, error: str) -> bool:
        """Check if error message is visible"""
        assert self.page.get_by_text(message).is_visible(timeout=5000),error
        
    def verify_ui_elements(self):
        assert self.page.locator(self.email_input).is_visible(), "Email input not visible"
        assert self.page.locator(self.password_input).is_visible(), "Password input not visible"
        assert self.page.locator(self.remember_me_checkbox).is_visible(), "Remember Me checkbox not visible"
        assert self.page.locator(self.forgot_password_link).is_visible(), "Forgot Password link not visible"
        assert self.page.locator(self.login_button).is_visible(), "Login button not visible"
        assert self.page.locator(self.google_signin_button).is_visible(), "Sign in with Google button not visible"
        assert self.page.locator(self.apple_signin_button).is_visible(), "Sign in with Apple button not visible"
        assert self.page.locator(self.signup_link).is_visible(), "Sign Up link not visible"

    def check_placeholder_visibility(self):
        assert self.page.get_by_placeholder("Enter your email").is_visible(), "Email input placeholder not visible"
        assert self.page.get_by_placeholder("Enter your password").is_visible(), "Password input placeholder not visible"

    def remember_me_check(self, check: bool):
        check_box = self.page.locator(self.remember_me_checkbox)
        if check_box.is_checked():
            checked = True
        else:
            checked = False

        if check:
            if checked == False:
                check_box.check()
            return
        else:
            if checked == True:
                check_box.uncheck()
            return
    
    def logout(self):
        """Log out the user"""
        profile_menu = self.page.get_by_role("button", name="user", exact=True)
        profile_menu.click()
        self.page.wait_for_timeout(1000)
        logout_button = self.page.get_by_role("link", name="Log Out", exact=True)
        logout_button.click()
        self.page.wait_for_timeout(3000)
        assert self.page.url.endswith("/auth/login"), "Logout failed, not redirected to login page"

    def check_remembered_credentials(self, expected_email: str):
        """Check if the email field is pre-filled with remembered email"""
        email_value = self.page.locator(self.email_input).input_value()
        assert email_value == expected_email, f"Remembered email mismatch: expected {expected_email}, got {email_value}"

    def click_signup_link(self):
        """Click on the Sign Up link"""
        self.page.locator(self.signup_link).click()
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/auth/signup"), "Not redirected to Sign Up page after clicking Sign up link"

    def login_invalid_email(self, email: str, password: str):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.wait_for_timeout(2000)
        self.page.locator(self.login_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def login_invalid_credentials(self, email: str, password: str):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.wait_for_timeout(2000)
        self.page.locator(self.login_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def login_empty_credentials(self, email: str):
        self.page.fill(self.email_input, email)
        self.page.locator(self.login_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def click_forgot_password_link(self):
        """Click on the Forgot Password link"""
        self.page.locator(self.forgot_password_link).click()
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/auth/forgot-password"), "Not redirected to Forgot Password page after clicking Forgot Password link"

    def click_return_to_login_button(self):
        """Click on the Return to LogIn button on Forgot Password page"""
        return_to_login_button = self.page.locator(self.return_to_login_button)
        return_to_login_button.click()
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/auth/login"), "Not redirected to Login page after clicking Return to LogIn button"

    def reset_password(self, email: str):
        self.page.fill(self.reset_password_email_input, email)
        self.page.locator(self.reset_password_button).click()
        self.page.wait_for_timeout(2000)
        pass

    def add_new_password(self, password: str, reset_link: str):
        self.page.goto(reset_link)
        self.page.wait_for_timeout(2000)
        assert "auth/verify-reset-email/" in self.page.url, "Not redirected to Reset Password page"
        self.accept_cookies_if_present()
        self.page.fill(self.new_password_input, password)
        self.page.fill(self.confirm_password_input, password)
        self.page.wait_for_timeout(2000)
        self.page.locator(self.reset_password_submit_button).click()
        self.page.wait_for_timeout(3000)
        pass

    def check_login_page_loaded(self):
        """Check if login page is loaded by verifying the presence of email input"""
        assert self.page.url.endswith("/auth/login"), "Login page not loaded properly"

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

        toggeled_password = self.page.locator(self.password_input).input_value()
        assert toggeled_password == password, "Password visibility toggle failed"
        pass
