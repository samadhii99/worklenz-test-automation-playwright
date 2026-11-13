import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListShowFields:
    """
    Test suite - Name : Task-list_Show Fields
    Details : Basic test cases for Show Fields
    """

    def test_tc_30_show_fields(self, authenticated_page):
        """
        Test Case - TC# : 30
        Name : Show fields
        Summary : Check if the user is able to select the fields to display in the task list
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.select_fields()
        time.sleep(2)