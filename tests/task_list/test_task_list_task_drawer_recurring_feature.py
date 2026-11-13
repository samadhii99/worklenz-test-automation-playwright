import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListRecurringFeature:
    """
    Test suite - Name : Task-list_Task drawer/ Recurring feature
    Details : Basic test cases for ensure the functionality of Recurring feature
    """

    def test_tc_147_verify_the_enable_of_the_recurring(self, authenticated_page):
        """
        Test Case - TC# : 147
        Name : Verify the enable of the recurring
        Summary : Verify the recurring function enables after click on it
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)

    def test_tc_148_recurring_task_configuration(self, authenticated_page):
        """
        Test Case - TC# : 148
        Name : Recurring task configuration
        Summary : Verify the user can change the recurring task settings
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_weekly()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)

    def test_tc_149_disable_of_a_recurring_feature(self, authenticated_page):
        """
        Test Case - TC# : 149
        Name : Disable of a recurring feature
        Summary : Ensure that once recurring is disable from a one task, all recurred tasks' recurring should be disable
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(False)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(False)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(False)
        time.sleep(2)

    def test_tc_150_enable_daily_recurring(self, authenticated_page):
        """
        Test Case - TC# : 150
        Name : Enable daily Recurring
        Summary : Verify enable recurring daily and its functionality
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_daily()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)

    def test_tc_151_enable_monthly_recurring_on_specific_date(self, authenticated_page):
        """
        Test Case - TC# : 151
        Name : Enable Monthly recurring
        Summary : Verify enable of Monthly recurring and its functionality
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_monthly_on_specific_date()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)

    def test_tc_152_enable_x_days_recurring(self, authenticated_page):
        """
        Test Case - TC# : 152
        Name : Enable Every X days recurring
        Summary : Verify enable of Every X days recurring and its functionality
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_x_days()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
    
    def test_tc_153_enable_x_weeks_recurring(self, authenticated_page):
        """
        Test Case - TC# : 153
        Name : Enable Every X weeks recurring
        Summary : Verify enable of Every X weeks recurring and its functionality
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_x_weeks()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)

    def test_tc_154_enable_x_months_recurring(self, authenticated_page):
        """
        Test Case - TC# : 154
        Name : Enable Every X Months recurring
        Summary : Verify enable of X Months recurring and its functionality
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_x_months()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)

    def test_tc_155_enable_monthly_recurring_on_specific_day(self, authenticated_page):
        """
        Test Case - TC# : 155
        Name : Enable Monthly recurring
        Summary : Verify enable of Monthly recurring and its functionality
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.recurring_toggle_via_task_drawer(True)
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)
        tl.configure_recurring_repeats_to_monthly_on_specific_day()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_recurring_task_in_task_list(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_recurring_toggle_enabled(True)
        time.sleep(2)
        tl.verify_enabled_recurring_type_show_via_task_drawer()
        time.sleep(2)