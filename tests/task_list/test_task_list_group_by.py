import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListGroupBy:
    """
    Test suite - Name : Task-list_Group By
    Details : Basic test cases for Task-list Group By
    """

    def test_tc_17_group_by_status(self, authenticated_page):
        """
        Test Case - TC# : 17
        Name : Group by status
        Summary : Check whether user is able to group task list by status
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Status")
        time.sleep(2)
    
    def test_tc_18_create_status_window(self, authenticated_page):
        """
        Test Case - TC# : 18
        Name : Create status window
        Summary : Check whether user is able to see create status window by clicking settongs icon
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Status")
        time.sleep(2)
        tl.click_manage_button("Manage Statuses")
        time.sleep(2)

    def test_tc_19_create_new_status(self, authenticated_page):
        """
        Test Case - TC# : 19
        Name : Create new status
        Summary : Check whether user is able to create new status
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Status")
        time.sleep(2)
        tl.click_manage_button("Manage Statuses")
        time.sleep(2)
        tl.create_new_status("Test Status")
        time.sleep(2)

    def test_tc_20_group_by_priority(self, authenticated_page):
        """
        Test Case - TC# : 20
        Name : Group by priority
        Summary : Check whether user is able to group task list by priority
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Priority")
        time.sleep(2)

    def test_tc_21_group_by_phase(self, authenticated_page):
        """
        Test Case - TC# : 21
        Name : Group by phase
        Summary : Check whether user is able to group task list by phase
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Phase")
        time.sleep(2)

    def test_tc_22_configure_phases_windows(self, authenticated_page):
        """
        Test Case - TC# : 22
        Name : Configure phases windows
        Summary : Check whether user is able to view configure phase window by clicking settings icon
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Phase")
        time.sleep(2)
        tl.click_manage_button("Manage Phase")
        time.sleep(2)

    def test_tc_23_create_new_phase(self, authenticated_page):
        """
        Test Case - TC# : 23
        Name : Create new phase
        Summary : Check whether user is able to create new phase
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Phase")
        time.sleep(2)
        tl.click_manage_button("Manage Phase")
        time.sleep(2)
        tl.create_new_phase("Test Phase")
        time.sleep(2)

    def test_tc_24_change_phase_color(self, authenticated_page):
        """
        Test Case - TC# : 24
        Name : Change phase color
        Summary : Check whether user is able to change phase color
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Phase")
        time.sleep(2)
        tl.click_manage_button("Manage Phase")
        time.sleep(2)
        tl.select_phase("Test Phase")
        time.sleep(2)

    def test_tc_25_delete_phase(self, authenticated_page):
        """
        Test Case - TC# : 25
        Name : Delete phase
        Summary : Check whether user is able to delete phase
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Phase")
        time.sleep(2)
        tl.click_manage_button("Manage Phase")
        time.sleep(2)
        tl.delete_phase("Test Phase")
        time.sleep(2)

    def test_tc_26_create_new_status_with_empty_name(self, authenticated_page):
        """
        Test Case - TC# : 26
        Name : Create new status with empty name
        Summary : Check whether user is unable to create new status with empty name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Status")
        time.sleep(2)
        tl.click_manage_button("Manage Status")
        time.sleep(2)
        tl.create_new_status("")
        time.sleep(2)

    def test_tc_27_create_new_phase_with_empty_name(self, authenticated_page):
        """
        Test Case - TC# : 27
        Name : Create new phase with empty name
        Summary : Check whether user is unable to create new phase with empty name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.group_by("Phase")
        time.sleep(2)
        tl.click_manage_button("Manage Phase")
        time.sleep(2)
        tl.create_new_phase("")
        time.sleep(2)