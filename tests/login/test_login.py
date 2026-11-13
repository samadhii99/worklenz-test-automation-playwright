# import pytest
# from playwright.sync_api import sync_playwright, expect, Page
# import sys, os
# import datetime

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# from pages.login.login_page import LoginPage
# from utilities.config_reader import ConfigReader

# # Use config reader for credentials
# config = ConfigReader()
# EMAIL = config.get_email()
# PASSWORD = config.get_password()

# # ---------- Soft Assertion Mechanism ----------
# soft_assert_failures = []

# def soft_assert(condition, message):
#     if not condition:
#         soft_assert_failures.append(message)
#         print(f"⚠️ Soft Assertion Failed: {message}")

# # Note: page fixture is now defined in tests/conftest.py

# # ---------- Login Tests ----------
# def test_valid_login(page: Page):
#     soft_assert_failures.clear()

#     login_page = LoginPage(page)
#     config = ConfigReader()
#     login_page.navigate(config.get_application_url())
#     login_page.enter_credentials(EMAIL, PASSWORD, use_alt_selectors=True)

#     greeting = page.locator("body > div.ant-message.ant-message-top.css-os2fvf > div > div > div > div > span:nth-child(2)")
#     try:
#         expect(greeting).to_be_visible(timeout=5000)
#     except:
#         soft_assert(False, "Dashboard greeting not visible")

#     text = greeting.inner_text() if greeting.is_visible() else ""
#     soft_assert("You have successfully logged in!" in text, f"Greeting mismatch: {text}")

#     if soft_assert_failures:
#         raise AssertionError("Soft assertion failures:\n" + "\n".join(soft_assert_failures))


# def test_invalid_email(page: Page):
#     soft_assert_failures.clear()

#     login_page = LoginPage(page)
#     config = ConfigReader()
#     login_page.navigate(config.get_application_url())
#     login_page.enter_credentials("invalid-email.com", PASSWORD, use_alt_selectors=True)

#     error_xpath = "//*[@id='login_email_help']/div[normalize-space()='Please enter a valid email address']"
#     soft_assert(login_page.error_message_visible(error_xpath), "Invalid email error not displayed")

#     if soft_assert_failures:
#         raise AssertionError("Soft assertion failures:\n" + "\n".join(soft_assert_failures))


# def test_invalid_password(page: Page):
#     soft_assert_failures.clear()

#     login_page = LoginPage(page)
#     config = ConfigReader()
#     login_page.navigate(config.get_application_url())
#     login_page.enter_credentials(EMAIL, "", use_alt_selectors=True)

#     error_xpath = "//*[@id='login_password_help']/div[normalize-space()='Please enter your Password!']"
#     soft_assert(login_page.error_message_visible(error_xpath), "Password required error not displayed")

#     if soft_assert_failures:
#         raise AssertionError("Soft assertion failures:\n" + "\n".join(soft_assert_failures))


# def test_wrong_credentials(page: Page):
#     soft_assert_failures.clear()

#     login_page = LoginPage(page)
#     config = ConfigReader()
#     login_page.navigate(config.get_application_url())
#     login_page.enter_credentials("ceyare4516@mliok.com", "wrongPassword", use_alt_selectors=True)

#     greeting = page.locator("body > div.ant-notification.ant-notification-topRight.css-os2fvf.ant-notification-stack.ant-notification-stack-expanded > div:nth-child(2) > div > div > div > div.ant-notification-notice-message")
#     try:
#         expect(greeting).to_be_visible(timeout=5000)
#     except:
#         soft_assert(False, "Login form not visible for wrong credentials")

#     text = greeting.inner_text() if greeting.is_visible() else ""
#     soft_assert("Login failed" in text, f"Greeting mismatch: {text}")

#     if soft_assert_failures:
#         raise AssertionError("Soft assertion failures:\n" + "\n".join(soft_assert_failures))


# # def test_google_sign_in(page):
# #     """
# #     Test Google Sign-In button on login page.
# #     This will open Google's login popup and check if the page navigates correctly.
# #     """
# #     soft_assert_failures.clear()

# #     login_page = LoginPage(page)
# #     login_page.navigate()

# #     # Click the Google Sign-In button
# #     google_button = page.locator("//button[@type='button' and contains(., 'Google')]")
# #     try:
# #         expect(google_button).to_be_visible(timeout=5000)
# #         google_button.click()
# #     except:
# #         soft_assert(False, "Google Sign-In button not visible or clickable")

# #     # Wait for new page (Google login popup)
# #     try:
# #         with page.context.expect_page() as new_page_info:
# #             google_button.click()
# #         google_popup = new_page_info.value
# #         expect(google_popup).not_to_be_none()
# #         print("Google Sign-In popup opened successfully")
# #     except Exception as e:
# #         soft_assert(False, f"Google Sign-In popup did not open: {e}")

# #     if soft_assert_failures:
# #         raise AssertionError("Soft assertion failures:\n" + "\n".join(soft_assert_failures))
