import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListTaskLinkCopy:
    """
    Test suite - Name : Task link Copy feature
    Details : Basic test case for copy task link
    """

    def test_tc_159_verify_copy_the_task_link(self, authenticated_page):
        """
        Test Case - TC# : 159
        Name : Verify Copy the task link
        Summary : Check that user can copy the task link
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.open_first_task_via_task_drawer()
        time.sleep(2)
        tl.copy_task_link_in_task_drawer()
        time.sleep(2)

    def test_tc_160_verify_open_a_task_through_copied_link(self, authenticated_page):
        """
        Test Case - TC# : 160
        Name : Verify open a task through copied link
        Summary : Check that user can open a task using copied task link
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.copy_task_link_in_task_drawer()
        time.sleep(2)
        tl.past_task_link()
        time.sleep(2)