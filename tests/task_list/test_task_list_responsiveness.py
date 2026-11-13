import pytest
import time
from pages.task_list.task_list_page import TaskListPage
from utilities.responsive_utils import set_viewport

@pytest.mark.filters
class TestTaskListResponsiveness:
    """
    Test suite - Name : Task-list_Responsiveness
    Details : Basic Test Cases for check Responsiveness of Task-list
    """

    def test_tc_143_responsiveness_for_laptop_screen(self, authenticated_page):
        """
        Test Case - TC# : 143
        Name : Responsiveness for Laptop Screen
        Summary : Verify that theTask-list page displays correctly and is responsive for the Laptop screen size
        """
        page = authenticated_page
        set_viewport(page, "laptop")
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)

    def test_tc_145_responsiveness_for_pc_screen(self, authenticated_page):
        """
        Test Case - TC# : 145
        Name : Responsiveness for PC Screen
        Summary : Verify that theTask-list page displays correctly and is responsive for the PC screen size
        """
        page = authenticated_page
        set_viewport(page, "pc")
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
    
    def test_tc_146_responsiveness_for_ipad_screen(self, authenticated_page):
        """
        Test Case - TC# : 146
        Name : Responsiveness for IPad Screen
        Summary : Verify if the Task-list page displays correctly and is responsive for the iPad screen size using Google DevTools
        """
        page = authenticated_page
        set_viewport(page, "ipad")
        tl = TaskListPage(page)
        tl.open_task_list_in_ipad()
        time.sleep(3)