import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskList:
    """
    Test suite - Name : Task-list
    Details : Basic test cases for task list
    """

    def test_tc_33_change_category_name(self, authenticated_page):
        """
        Test Case - TC# : 33
        Name : change category name (Status Name)
        Summary : Check whether user is able to rename category name(Status Name)
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.change_category_name()
        time.sleep(2)

################################################################################################################
    # def test_tc_34_change_category(self, authenticated_page):
    #     """
    #     Test Case - TC# : 34
    #     Name : change category
    #     Summary : Check whether user is able to category
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.change_category()
    #     time.sleep(2)
################################################################################################################

    def test_tc_35_add_a_task(self, authenticated_page):
        """
        Test Case - TC# : 35
        Name : add a task
        Summary : Check whether user is able to add tasks for To Do table
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)

    def test_tc_36_add_subtask_for_the_task(self, authenticated_page):
        """
        Test Case - TC# : 36
        Name : add subtask for the task
        Summary : Check whether user is able to add subtasks for the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_subtask()
        time.sleep(2)

    def test_tc_37_edit_task_name(self, authenticated_page):
        """
        Test Case - TC# : 37
        Name : edit task name
        Summary : Check whether user is able to edit and change task name
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.edit_task_name()
        time.sleep(2)

    def test_tc_38_assign_members_for_task(self, authenticated_page):
        """
        Test Case - TC# : 38
        Name : assign members for task
        Summary : Check whether user is able to assign members for a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.assign_members_for_task()
        time.sleep(2)

    def test_tc_39_invite_a_new_member_by_email(self, authenticated_page):
        """
        Test Case - TC# : 39
        Name : invite a new member by email
        Summary : Check whether user is able to invite a new member to the project by email
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.invite_a_new_member_by_email()
        time.sleep(2)

    def test_tc_40_add_label_for_the_task(self, authenticated_page):
        """
        Test Case - TC# : 40
        Name : add label for the task
        Summary : Check whether user is able to add label for a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_label_for_the_task()
        time.sleep(2)

################################################################################################################

    # def test_tc_41_add_label_by_creating_new_label(self, authenticated_page):
    #     """
    #     Test Case - TC# : 41
    #     Name : add label by creating new label
    #     Summary : Check whether user is able to add new label for a task by creating a new label
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.add_a_task(True)
    #     time.sleep(2)
    #     tl.create_new_label()
    #     time.sleep(2)
################################################################################################################

    def test_tc_42_add_phase_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 42
        Name : add phase to the task
        Summary : Check whether user is able to add phase to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.select_fields()
        time.sleep(2)
        tl.add_phase_to_task()
        time.sleep(2)

    def test_tc_43_change_status_of_the_task(self, authenticated_page):
        """
        Test Case - TC# : 43
        Name : change status of the task
        Summary : Check whether user is able to change status for a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.change_status("Doing")
        time.sleep(2)

    def test_tc_44_change_priority(self, authenticated_page):
        """
        Test Case - TC# : 43
        Name : change priority
        Summary : Check whether user is able to change the priority level of task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.change_priority()
        time.sleep(2)

    def test_tc_45_add_time_tracking_for_a_task(self, authenticated_page):
        """
        Test Case - TC# : 45
        Name : add time tracking for a task
        Summary : Check whether user is able to add time tracking for the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_time_track()
        time.sleep(2)

    def test_tc_46_set_start_date_for_a_task(self, authenticated_page):
        """
        Test Case - TC# : 46
        Name : set start date for a task
        Summary : Check whether user is able to set start date for a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.set_start_date()
        time.sleep(2)

    def test_tc_47_set_due_date_for_a_task(self, authenticated_page):
        """
        Test Case - TC# : 47
        Name : set due date for a task
        Summary : Check whether user is able to set due date for a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.set_due_date()
        time.sleep(2)

    def test_tc_48_display_time_tracking_details(self, authenticated_page):
        """
        Test Case - TC# : 48
        Name : display time tracking details
        Summary : Check whether user is able to see the relevant time tracking details of the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_time_track()
        time.sleep(2)
        tl.show_time_track_logs()
        time.sleep(2)

    def test_tc_49_add_a_task_with_empty_field(self, authenticated_page):
        """
        Test Case - TC# : 49
        Name : add a task with empty field
        Summary : Check user is unable to add task with empty field
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(False)
        time.sleep(2)

    def test_tc_50_invite_new_member_by_invalid_email_format(self, authenticated_page):
        """
        Test Case - TC# : 50
        Name : invite a new member by invalid email format
        Summary : Check whether user is unable to invite a new member to the project with invalid email format
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.invite_a_new_member_by_invalid_email()
        time.sleep(2)