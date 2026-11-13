import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListBulkActionMenu:
    """
    Test suite - Name : Task-list Bulk Action Menu
    Details : Basic test cases for context menu
    """

    def test_tc_57_view_bulk_action_menu_by_selecting_task(self, authenticated_page):
        """
        Test Case - TC# : 57
        Name : view bulk action menu by selecting task
        Summary : Check whether user is able to see horizontal option menu for the selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)

    def test_tc_58_change_status_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 58
        Name : change status via bulk action menu
        Summary : Check whether user is able to change status of the task
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

    def test_tc_59_change_priority_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 59
        Name : change proiority via bulk action menu
        Summary : Check whether user is able to change priority of the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_priority_via_bulk_action("Low")
        time.sleep(2)

    def test_tc_60_change_phase_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 60
        Name : change phase via bulk action menu
        Summary : Check whether user is able to change phase of the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_phase_via_bulk_action("Resolved")
        time.sleep(2)

    def test_tc_61_change_label_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 61
        Name : change label via bulk action menu
        Summary : Check whether user is able to add label or change label for the selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.change_label_in_bulk_action()
        time.sleep(2)
        tl.create_label_in_bulk_action()
        time.sleep(2)

    def test_tc_62_assign_task_to_me_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 62
        Name : assign task to me via bulk action menu
        Summary : Check whether user is able to assign task to themselves
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.assign_task_to_me_in_bulk_action()
        time.sleep(2)
        tl.verify_assign()
        time.sleep(2)

    def test_tc_63_assign_task_to_members_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 63
        Name : assign task to members via bulk action menu
        Summary : Check whether user is able to assign task to members
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.assign_task_to_members_in_bulk_action()
        time.sleep(2)
        tl.verify_assign()
        time.sleep(2)

    def test_tc_64_archive_a_task_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 64
        Name : archive a task via bulk action menu
        Summary : Check whether user is able to archive a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.archive_task_in_bulk_action()
        time.sleep(2)
        tl.verify_archived()
        time.sleep(2)

    def test_tc_65_delete_a_task_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 65
        Name : delete a task via bulk action menu
        Summary : Check whether user is able to delete a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.delete_task_in_bulk_action()
        time.sleep(2)
        tl.verify_deleted_task("Delete task via bulk action menu failed")
        time.sleep(2)

    def test_tc_66_create_task_templates_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 66
        Name : create task templates via bulk action menu
        Summary : Check whether user is able to create task templates for the selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.create_task_templates_in_bulk_action()
        time.sleep(2)
        tl.verify_import_task()
        time.sleep(2)

    def test_tc_67_cancel_task_templates_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 67
        Name : cancel task templates via bulk action menu
        Summary : Check whether user is able to cancel task templates for the selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.cancel_task_templates_in_bulk_action()
        time.sleep(2)

    def test_tc_68_deselect_all_via_bulk_action_menu(self, authenticated_page):
        """
        Test Case - TC# : 68
        Name : deselect all via bulk action menu
        Summary : Check whether user is able to deselect the selected task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.view_bulk_action_menu()
        time.sleep(2)
        tl.deselect_task()
        time.sleep(2)