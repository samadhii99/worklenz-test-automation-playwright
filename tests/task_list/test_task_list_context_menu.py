import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListContextMenu:
    """
    Test suite - Name : Task-list ContextMenu
    Details : Basic test cases for context menu
    """

    def test_tc_51_view_context_menu(self, authenticated_page):
        """
        Test Case - TC# : 51
        Name : view context menu
        Summary : Check whether user is able to see context menu for the selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.view_context_menu()
        time.sleep(2)

    def test_tc_52_assign_task_to_me(self, authenticated_page):
        """
        Test Case - TC# : 52
        Name : view context menu
        Summary : Check whether user is able to assign task to themselves
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.right_click_on_task()
        time.sleep(2)
        tl.click_on_context_menu("Assign to Me")
        time.sleep(2)
        tl.verify_assign()
        time.sleep(2)

    def test_tc_53_move_to_task(self, authenticated_page):
        """
        Test Case - TC# : 53
        Name : move to task
        Summary : Check whether user is able to change status for selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.right_click_on_task()
        time.sleep(2)
        tl.click_on_context_menu("Move to")
        time.sleep(2)
        tl.verify_move_to_from_context_menu()
        time.sleep(2)

    def test_tc_54_archive_a_task(self, authenticated_page):
        """
        Test Case - TC# : 54
        Name : archive a task
        Summary : Check whether user is able to archive a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.right_click_on_task()
        time.sleep(2)
        tl.click_on_context_menu("Archive")
        time.sleep(2)
        tl.verify_archived()
        time.sleep(2)

    def test_tc_55_convert_task_to_subtask(self, authenticated_page):
        """
        Test Case - TC# : 55
        Name : convert task to subtask
        Summary : Check whether user is able to convert a task into subtask
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.right_click_on_task()
        time.sleep(2)
        tl.click_on_context_menu("Convert to Sub task")
        time.sleep(2)
        tl.covert_to_subtask_from_context_menu()
        time.sleep(2)
        tl.verify_coverted_to_subtask_from_context_menu()
        time.sleep(2)

    def test_tc_56_delete_a_task(self, authenticated_page):
        """
        Test Case - TC# : 56
        Name : delete a task
        Summary : Check whether user is able to delete a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.right_click_on_task()
        time.sleep(2)
        tl.click_on_context_menu("Delete")
        time.sleep(2)
        tl.verify_deleted_task("Delete task from context menu failed")
        time.sleep(2)