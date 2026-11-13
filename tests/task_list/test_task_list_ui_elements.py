import pytest
import time
from pages.task_list.task_list_page import TaskListPage
@pytest.mark.ui
class TestTaskListUIElements:
    """
    Test suite - Name : Task-list_UI elements
    Details : Basic test cases for Task-list UI Element
    """

    def test_tc_01_verify_ui_elements(self, authenticated_page):
        """
        Test Case - TC# : 01
        Name : Verify UI elements
        Summary : Check that all UI elements are present on the Task-list page
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.verify_ui_elements()

################################################################################################################
    # def test_tc_02_display_tooltips_in_columns(self, authenticated_page):
    #     """
    #     Test Case - TC# : 02
    #     Name : Display Tooltips in Columns
    #     Summary : Check whether user can see tooltips when hovering over columns
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.display_tooltips_in_columns()
