import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListTaskDrawerTimeLogs:
    """
    Test suite - Name : Task-list Task Drawer/Time Logs
    Details : Basic test cases for task drawer/time logs
    """

    def test_tc_108_time_log_tab(self, authenticated_page):
        """
        Test Case - TC# : 108
        Name : Time Log Tab
        Summary : Check whether user able to see time log details window with add time log function
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)

    def test_tc_109_add_time_log_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 109
        Name : Add Time Log to the task
        Summary : Check whether user able to see time log details window with add time log function
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)
        tl.add_time_logs_via_task_drawer()
        time.sleep(2)

    def test_tc_110_edit_time_log_details(self, authenticated_page):
        """
        Test Case - TC# : 110
        Name : Edit Time Log details
        Summary : Check whether user able to edit time log details
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)
        tl.add_time_logs_via_task_drawer()
        time.sleep(2)
        tl.edit_time_log_details_via_task_drawer()
        time.sleep(2)

    def test_tc_111_delete_time_log_details(self, authenticated_page):
        """
        Test Case - TC# : 111
        Name : Delete Time Log details
        Summary : Check whether user able to delete time log details
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)
        tl.add_time_logs_via_task_drawer()
        time.sleep(2)
        tl.delete_time_log_details_via_task_drawer()
        time.sleep(2)

    def test_tc_112_cancel_deletion_of_time_log_details(self, authenticated_page):
        """
        Test Case - TC# : 112
        Name : Cancel delete of Time Log details
        Summary : Check whether user is able to cancel the deletion of time log details
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)
        tl.add_time_logs_via_task_drawer()
        time.sleep(2)
        tl.cancel_deletion_of_time_log_details_via_task_drawer()
        time.sleep(2)

    def test_tc_113_login_to_the_task_via_timer(self, authenticated_page):
        """
        Test Case - TC# : 113
        Name : Log in to the task via Timer
        Summary : Check whether user is able to cancel the deletion of time log details
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)
        tl.start_timer_via_task_drawer()
        time.sleep(2)

    def test_tc_114_export_time_log_details_to_excel(self, authenticated_page):
        """
        Test Case - TC# : 114
        Name : Export Time log details to Excel
        Summary : Check whether user able to export TimeLog details to Excel
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_time_logs_tab_via_task_drawer()
        time.sleep(2)
        tl.add_time_logs_via_task_drawer()
        time.sleep(2)
        tl.export_to_excel_via_task_drawer()
        time.sleep(2)