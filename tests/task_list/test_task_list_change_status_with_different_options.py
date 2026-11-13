import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListChangeStatusWithDifferentOptions:
    """
    Test suite - Name : Change task's status with different change options
    Details : Basic test cases for task dependency with task's status with different change options
    """

    def test_tc_138_change_task_status_with_incomplete_task_dependency_from_bulk_action(self, authenticated_page):
        """
        Test Case - TC# : 138
        Name : Change task's status with task dependency (Incomplete) from bulk action menu
        Summary : Check whether user able to change task's status with task dependency(incomplete tasks) from bulb action menu
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_status_when_dependency_is_not_done_via_bulk_action("Done")
        time.sleep(2)

    def test_tc_139_change_task_status_with_incomplete_task_dependency_using_drag_and_drop(self, authenticated_page):
        """
        Test Case - TC# : 139
        Name : Change task's status with task dependency(Incomplete) using drag and drop
        Summary : Check whether user able to change task's status with task dependency(incomplete tasks) using drag and drop
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.drag_and_drop_the_dependency_is_not_done_task("Done")
        time.sleep(2)

    def test_tc_140_change_task_status_with_incomplete_task_dependency_from_task_outside_dropdown(self, authenticated_page):
        """
        Test Case - TC# : 140
        Name : Change task's status with task dependency(Incomplete) from task's outside dropdown
        Summary : Check whether user able to change task's status with task dependency(incomplete tasks) from task's outside dropdown
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.change_status_when_dependency_is_not_done_task("Done")    
        time.sleep(2)

    def test_tc_141_change_task_status_with_incomplete_task_dependency_from_task_inside_dropdown(self, authenticated_page):
        """
        Test Case - TC# : 141
        Name : Change task's status with task dependency(Incomplete) from task's inside dropdown
        Summary : Check whether user able to change task's status with task dependency(incomplete tasks) from task's inside dropdown
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_when_dependency_is_not_done_task_via_task_drawer("Done")
        time.sleep(2)

    def test_tc_142_change_task_status_with_incomplete_task_dependency_from_kanban_board(self, authenticated_page):
        """
        Test Case - TC# : 142
        Name : Change task's status with task dependency(Incomplete) from kanban board using drag and drop
        Summary : Check whether user able to change task's status with task dependency(incomplete tasks) from kanban board using drag and drop
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.change_status_when_dependency_is_not_done_task_via_kanban_board("Done")
        time.sleep(2)

        