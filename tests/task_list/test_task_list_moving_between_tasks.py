import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListMovingBetweenTasks:
    """
    Test suite - Name : Task list - Moving between tasks
    Details : Basic test case for moving between main tasks
    """

    def test_tc_156_verify_move_to_the_next_task(self, authenticated_page):
        """
        Test Case - TC# : 156
        Name : Verify move to the next task
        Summary : Check that user can move to the next task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.open_first_task_via_task_drawer()
        time.sleep(2)
        tl.move_to_next_task_via_task_drawer()
        time.sleep(2)

    def test_tc_157_verify_move_to_the_previous_task(self, authenticated_page):
        """
        Test Case - TC# : 157
        Name : Verify move to the previous task
        Summary : Check that user can move to the previous task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task_via_create_task_button()
        time.sleep(2)
        tl.move_to_previous_task_via_task_drawer()
        time.sleep(2)

    def test_tc_158_verify_move_to_the_next_task(self, authenticated_page):
        """
        Test Case - TC# : 158
        Name : Verify task count display in the task drawer
        Summary : Check that task count is display correctly
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.open_first_task_via_task_drawer()
        time.sleep(2)
        tl.task_counts_in_task_drawer()
        time.sleep(2)