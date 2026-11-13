import pytest
import time
from pages.home.home_page import HomePage

@pytest.mark.ui
class TestHomeCreateProjectDrawer:
    """
    Test suite - Name : Home_Create Project Drawer
    Details : Basic test cases for create new project Functionality with Create Project Drawer
    """

    def test_tc_03_verify_create_project(self, authenticated_page):
        """
        Test Case - TC# : 03
        Name : Verify Open Create project drawer
        Summary : Check whether user able to view the Create project drawer by clicking Create a project button
        """
        page = authenticated_page
        hp = HomePage(page)
        hp.open_home_page()
        time.sleep(2)
        hp.open_create_project_drawer()
        time.sleep(2)

    def test_tc_04_verify_ui_elements_in_create_project_drawer(self, authenticated_page):
        """
        Test Case - TC# : 04
        Name : Verify UI elements in Create project drawer
        Summary : Check that all UI elements are present on the Create project drawer
        """
        page = authenticated_page
        hp = HomePage(page)
        hp.open_home_page()
        time.sleep(2)
        hp.open_create_project_drawer()
        time.sleep(2)
        hp.verify_ui_elements_in_create_project_drawer()
        time.sleep(2)

    def test_tc_05_verify_creating_a_new_project(self, authenticated_page):
        """
        Test Case - TC# : 05
        Name : Verify Creating a new project
        Summary : Check whether user able to create new project
        """
        page = authenticated_page
        hp = HomePage(page)
        hp.open_home_page()
        time.sleep(2)
        hp.open_create_project_drawer()
        time.sleep(2)
        hp.insert_project_details()
        time.sleep(2)
        hp.click_create_project()
        time.sleep(2)

    def test_tc_06_verify_valid_input_range_for_hours_per_day(self, authenticated_page):
        """
        Test Case - TC# : 06
        Name : Verify Valid Input Range for Hours per Day
        Summary : Check that the "Hours per Day" field accepts values between 0 and 24 and disables the increment icon at 24.
        """
        page = authenticated_page
        hp = HomePage(page)
        hp.open_home_page()
        time.sleep(2)
        hp.open_create_project_drawer()
        time.sleep(2)
        hp.insert_project_details()
        time.sleep(2)
        hp.verify_hours_per_day()
        time.sleep(2)

    def test_tc_07_verify_required_fields_when_creating_new_project(self, authenticated_page):
        """
        Test Case - TC# : 07
        Name : Verify Required Fields When creating new project
        Summary : Verify that "Name" field cannot be left empty, displaying "Please enter a name" error messages
        """
        page = authenticated_page
        hp = HomePage(page)
        hp.open_home_page()
        time.sleep(2)
        hp.open_create_project_drawer()
        time.sleep(2)
        hp.verify_project_name_validation()
        time.sleep(2)
