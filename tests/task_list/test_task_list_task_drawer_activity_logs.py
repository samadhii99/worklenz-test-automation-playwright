import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListTaskDrawerActivityLogs:
    """
    Test suite - Name : Task-list Task Drawer/Activity Logs
    Details : Basic test cases for task drawer/activity logs
    """

    def test_tc_115_view_activity_log_tab(self, authenticated_page):
        """
        Test Case - TC# : 115
        Name : View Activity Log Tab
        Summary : Check whether user able to see relevant Activity details for the specific task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_activity_log_tab_via_task_drawer()
        time.sleep(2)

    def test_tc_116_display_multiple_changes_in_activity_log(self, authenticated_page):
        """
        Test Case - TC# : 116
        Name : Display Multiple Changes in Activity Log (via Task Drawer)
        Summary : Verify that when a task's status, phase, priority, members, due date are changed using the Task Drawer, the changes are recorded in the Activity Log
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Doing")
        time.sleep(2)
        tl.add_phase_to_the_task_via_task_drawer()
        time.sleep(2)
        tl.change_priority_via_task_drawer()
        time.sleep(2)
        tl.assign_task_to_members_in_drawer()
        time.sleep(2)
        tl.add_due_date_in_drawer()
        time.sleep(2)
        tl.click_activity_log_tab_via_task_drawer()
        time.sleep(2)
        tl.verify_activities_in_activity_logs_via_task_drawer()
        time.sleep(2)

    def test_tc_117_display_multiple_changes_in_activity_log_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 117
        Name : Display Multiple Changes in Activity Log (via Bulb Action Menu)
        Summary : Verify that changes to a task's attributes via the Bulb Action Menu are displayed in the Activity Log.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_status_via_bulk_action("Doing")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_priority_via_bulk_action("Low")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_phase_via_bulk_action("Resolved")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_status_via_bulk_action("Done")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_priority_via_bulk_action("High")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_phase_via_bulk_action("Test Phase")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_status_via_bulk_action("To Do")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_priority_via_bulk_action("Medium")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_phase_via_bulk_action("Backlog")
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.assign_task_to_members_in_bulk_action()
        time.sleep(2)
        tl.verify_assign()
        time.sleep(2)        
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_activity_log_tab_via_task_drawer()
        time.sleep(2)
        tl.verify_activities_in_activity_logs_via_bulk_action()
        time.sleep(2)

    def test_tc_118_display_multiple_changes_in_activity_log_via_context_menu(self, authenticated_page):
        """
        Test Case - TC# : 118
        Name : Display Multiple Changes in Activity Log (via Context Menu)
        Summary : Verify that changes to a task's attributes via the Context Menu are displayed in the Activity Log.
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
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_activity_log_tab_via_task_drawer()
        time.sleep(2)
        tl.verify_activities_in_activity_logs_via_context_menu()
        time.sleep(2)

    def test_tc_119_display_multiple_changes_in_activity_log_via_task_table(self, authenticated_page):
        """
        Test Case - TC# : 119
        Name : Display Multiple Changes in Activity Log (via task table)
        Summary : Verify that changes to a task's attributes via the task table are displayed in the Activity Log.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.change_status("Doing")
        time.sleep(2)
        tl.change_priority()
        time.sleep(2)
        tl.set_due_date()
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.click_activity_log_tab_via_task_drawer()
        time.sleep(2)
        tl.verify_activities_in_activity_logs_via_task_table()
        time.sleep(2)