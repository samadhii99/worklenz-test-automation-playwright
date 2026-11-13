import pytest
import time
from pages.home.home_page import HomePage

@pytest.mark.ui
class TestHomeUIElements:
    """
    Test suite - Name : Home_UI elements
    Details : Basic test cases for Home page UI Elements
    """

    def test_tc_01_verify_ui_elements(self, authenticated_page):
        """
        Test Case - TC# : 01
        Name : Verify UI elements
        Summary : Check that All UI elements are present on the Home page
        """
        page = authenticated_page
        kb = HomePage(page)
        kb.open_home_page()
        time.sleep(2)
        kb.verify_ui_elements()
        time.sleep(2)

    def test_tc_02_verify_tooltips(self, authenticated_page):
        """
        Test Case - TC# : 01
        Name : Verify Tooltip in Home Page
        Summary : Check whether All tooltips are presented on Home Page
        """
        page = authenticated_page
        kb = HomePage(page)
        kb.open_home_page()
        time.sleep(2)
        kb.verify_tooltips()
        time.sleep(2)
