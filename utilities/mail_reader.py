import re
from playwright.sync_api import Page
import time

class MailReader:
    """Sync MailReader for Mailinator public inbox"""

    BASE_URL = "https://www.mailinator.com"

    def __init__(self, inbox: str = "testworklenz"):
        # Inbox name ONLY, no @mailinator.com
        self.inbox = inbox

    def get_reset_link_mailinator(self, page: Page, retries: int = 10, wait_seconds: int = 3) -> str:
        """
        Poll Mailinator inbox until the latest reset email is received
        and return the reset link
        """
        for attempt in range(retries):
            try:
                # Open inbox page
                page.goto(f"{self.BASE_URL}/v4/public/inboxes.jsp?to={self.inbox}")
                page.wait_for_selector("//*[@ng-repeat='email in emails']", timeout=5000)

                # Click the latest email
                page.locator("//*[@ng-repeat='email in emails']").first.click()
                page.wait_for_selector("iframe#html_msg_body", timeout=5000)
                frame = page.frame_locator("iframe#html_msg_body")
                reset_link = frame.locator("a", has_text="Reset my password").get_attribute("href")
                assert reset_link is not None, "Reset link not found in email"
                return reset_link
            except Exception:
                time.sleep(wait_seconds)

        raise TimeoutError("Reset email not received within expected time")
    
    def get_invite_link_mailinator(self, page: Page, retries: int = 10, wait_seconds: int = 3) -> str:
        """
        Poll Mailinator inbox until the latest invite email is received
        and return the invited link
        """
        for attempt in range(retries):
            try:
                # Open inbox page
                page.goto(f"{self.BASE_URL}/v4/public/inboxes.jsp?to={self.inbox}")
                page.wait_for_selector("//*[@ng-repeat='email in emails']", timeout=5000)

                # Click the latest email
                page.locator("//*[@ng-repeat='email in emails']").first.click()
                page.wait_for_selector("iframe#html_msg_body", timeout=5000)
                frame = page.frame_locator("iframe#html_msg_body")
                reset_link = frame.locator("a", has_text="Go to Worklenz").get_attribute("href")
                assert reset_link is not None, "Invite link not found in email"
                return reset_link
            except Exception:
                time.sleep(wait_seconds)

        raise TimeoutError("Invite email not received within expected time")
