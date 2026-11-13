import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListFilters:
    """
    Test suite - Name : Task-List_Filters
    Details : Basic test cases for Task-list filters
    """

    def test_tc_03_task_search_by_name(self, authenticated_page):
        """
        Test Case - TC# : 03
        Name : Task search By Name
        Summary : Check whether user is able to search tasks by task name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_project_tasks_with_details()
        time.sleep(2)
        tl.task_search_by_name()

    def test_tc_04_reset_task_list(self, authenticated_page):
        """
        Test Case - TC# : 04
        Name : Reset Task-list
        Summary : Check whether user can reset task-list after searching task name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_project_tasks_with_details()
        time.sleep(2)
        tl.task_search_by_name()
        time.sleep(2)
        tl.reset_task_list()

    def test_tc_05_sort_filter_by_task(self, authenticated_page):
        """
        Test Case - TC# : 05
        Name : Sort Filter by task
        Summary : Check whether user is able to sort tasks according to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Task",False) #sort and filter by task ascending
        time.sleep(2)
        tl.sort_filter_by("Task",True) #sort and filter by task descending

    def test_tc_06_sort_filter_by_status(self, authenticated_page):
        """
        Test Case - TC# : 06
        Name : Sort Filter by status
        Summary : Check whether user is able to sort tasks according to the status
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Status",False) #sort and filter by status ascending
        time.sleep(2)
        tl.sort_filter_by("Status",True) #sort and filter by status descending

    def test_tc_07_sort_filter_by_priority(self, authenticated_page):
        """
        Test Case - TC# : 07
        Name : Sort Filter by priority
        Summary : Check whether user is able to sort tasks according to the priority
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Priority",False) #sort and filter by priority ascending
        time.sleep(2)
        tl.sort_filter_by("Priority",True) #sort and filter by priority descending

    def test_tc_08_sort_filter_by_end_date(self, authenticated_page):
        """
        Test Case - TC# : 08
        Name : Sort Filter by end date
        Summary : Check whether user is able to sort tasks according to the end date
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("End Date",False) #sort and filter by end date ascending
        time.sleep(2)
        tl.sort_filter_by("End Date",True) #sort and filter by end date descending

    def test_tc_09_sort_filter_by_start_date(self, authenticated_page):
        """
        Test Case - TC# : 09
        Name : Sort Filter by start date
        Summary : Check whether user is able to sort tasks according to the start date
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Start Date",False) #sort and filter by start date ascending
        time.sleep(2)
        tl.sort_filter_by("Start Date",True) #sort and filter by start date descending

    def test_tc_10_sort_filter_by_completed_date(self, authenticated_page):
        """
        Test Case - TC# : 10
        Name : Sort Filter by completed date
        Summary : Check whether user is able to sort tasks according to the completed date
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Completed Date",False) #sort and filter by completed date ascending
        time.sleep(2)
        tl.sort_filter_by("Completed Date",True) #sort and filter by completed date descending

    def test_tc_11_sort_filter_by_created_date(self, authenticated_page):
        """
        Test Case - TC# : 11
        Name : Sort Filter by created date
        Summary : Check whether user is able to sort tasks according to the created date
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Created Date",False) #sort and filter by created date ascending
        time.sleep(2)
        tl.sort_filter_by("Created Date",True) #sort and filter by created date descending

    def test_tc_12_sort_filter_by_last_updated(self, authenticated_page):
        """
        Test Case - TC# : 12
        Name : Sort Filter by last updated
        Summary : Check whether user is able to sort tasks according to the last updated
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.sort_filter_by("Last Updated",False) #sort and filter by last updated ascending
        time.sleep(2)
        tl.sort_filter_by("Last Updated",True) #sort and filter by last updated descending

    def test_tc_13_priority_filter(self, authenticated_page):
        """
        Test Case - TC# : 13
        Name : Priority Filter
        Summary : Check whether user is able to filter tasks by priority
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.priority_filter(False) #filter by single priority
        time.sleep(2)
        tl.priority_filter(True) #filter by multiple priorities
        time.sleep(2)

    def test_tc_14_labels_filter(self, authenticated_page):
        """
        Test Case - TC# : 14
        Name : Labels Filter
        Summary : Check whether user is able to filter tasks by labels
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.labels_filter(False) #filter by one label
        time.sleep(2)
        tl.labels_filter(True) #filter by multiple labels
        time.sleep(2)

    def test_tc_15_member_filter(self, authenticated_page):
        """
        Test Case - TC# : 15
        Name : Member Filter
        Summary : Check whether user is able to filter tasks by members
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.member_filter(False) #filter by single member
        time.sleep(2)
        tl.member_filter(True) #filter by multiple members
        time.sleep(2)

    def test_tc_16_non_existant_task_search_by_name(self, authenticated_page):
        """
        Test Case - TC# : 16
        Name : "Non-existant task search by name"
        Summary : Check whether user unable to search Non-existant tasks by name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.task_search_by_non_existant_name()
        time.sleep(2)