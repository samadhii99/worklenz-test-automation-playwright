import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListTaskDrawer:
    """
    Test suite - Name : Task-list Task Drawer
    Details : Basic test cases for task drawer
    """

    def test_tc_69_open_task_drawer(self, authenticated_page):
        """
        Test Case - TC# : 69
        Name : open task drawer
        Summary : Check whether user is able to open task drawer
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)

    def test_tc_70_verify_ui_elements(self, authenticated_page):
        """
        Test Case - TC# : 70
        Name : verify ui elements
        Summary : Check that all UI elements are present on the task drawer
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.verify_task_drawer_ui_elements()
        time.sleep(2)

    def test_tc_70_change_task_name_via_task_drawer(self, authenticated_page):
        """
        Test Case - TC# : 70
        Name : change task name via task drawer
        Summary : Check whether user is able to change task name in the task drawer
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_task_name_via_task_drawer(True)
        time.sleep(2)

    def test_tc_71_change_task_status(self, authenticated_page):
        """
        Test Case - TC# : 71
        Name : change task status
        Summary : Check whether user able to change status of the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_task_status_via_task_drawer()
        time.sleep(2)

    def test_tc_72_delete_task_status(self, authenticated_page):
        """
        Test Case - TC# : 72
        Name : delete the task
        Summary : Check whether user able to delete the task from task list
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.delete_task_via_task_drawer()
        time.sleep(2)
        tl.verify_deleted_task("Delete task from task drawer failed")
        time.sleep(2)

    def test_tc_73_change_task_name_with_empty_name(self, authenticated_page):
        """
        Test Case - TC# : 73
        Name : change task name with empty name
        Summary : Check whether user able to change task name with empty name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_task_name_via_task_drawer(False)
        time.sleep(2)