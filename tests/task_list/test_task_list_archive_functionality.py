import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListArchiveFunctionality:
    """
    Test suite - Name : Task-list_Archive Functionality
    Details : Basic test cases for Archive Functionality
    """

    def test_tc_28_show_archived_tasks(self, authenticated_page):
        """
        Test Case - TC# : 28
        Name : Show archived tasks
        Summary : Check whether user is able see only archived tasks by selecting Show Archived
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.mark_show_archived(True)
        time.sleep(2)

    def test_tc_29_unarchive_a_tasks(self, authenticated_page):
        """
        Test Case - TC# : 28
        Name : Unarchive a tasks
        Summary : Check whether user is able to unarchive a archived task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.mark_show_archived(False)
        time.sleep(2)