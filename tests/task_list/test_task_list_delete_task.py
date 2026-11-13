import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestDeleteTask:
    """
    Test suite - Name : Delete task
    Details : Basic test case for delete a task
    """

    def test_tc_161_verify_delete_a_task(self, authenticated_page):
        """
        Test Case - TC# : 161
        Name : Verify delete a task
        Summary : Check that user can delete task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.delete_task_in_task_drawer()
        time.sleep(2)
        tl.verify_deleted_task("Delete task in task drawer failed")
        time.sleep(2)