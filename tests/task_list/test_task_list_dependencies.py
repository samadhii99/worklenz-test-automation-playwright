import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListTaskDependencies:
    """
    Test suite - Name : Task-list Dependencies
    Details : Basic test cases for dependencies
    """

    def test_tc_120_add_dependency_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 120
        Name : Add dependency to the task
        Summary : Check whether user able to add existing task as dependency to the tasks in ToDo
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

    def test_tc_121_delete_dependency_from_task(self, authenticated_page):
        """
        Test Case - TC# : 121
        Name : Delete Dependency from Task
        Summary : Check whether user able to delete a dependency from a tasks
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
        tl.delete_dependency_via_task_drawer()
        time.sleep(2)

    def test_tc_122_change_status_after_deleting_dependency(self, authenticated_page):
        """
        Test Case - TC# : 122
        Name : Change Status After Deleting Dependency
        Summary : Check whether user able to change the task’s status to "Done" without restriction, After deleting a dependency
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
        tl.delete_dependency_via_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Doing")
        time.sleep(2)

    def test_tc_123_change_task_to_done_when_dependency_is_done(self, authenticated_page):
        """
        Test Case - TC# : 123
        Name : Change Task to Done when Dependency is Done
        Summary : Check whether user able to Change a task's status to "Done" when its dependency is marked as "Done."
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Done")
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.get_random_task_by_phase("Done")
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
        tl.change_status_via_task_drawer("Doing")
        time.sleep(2)

    def test_tc_124_add_more_dependencies_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 124
        Name : Add more dependencies to the task
        Summary : Check whether user able to add more than one dependency to a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_multiple_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_multiple_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)

    def test_tc_125_add_more_dependencies_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 125
        Name : Change task to Done when all dependencies are Done
        Summary : Check whether user able to change the task's status to "Done" when all dependencies are either "Done."
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_multiple_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_multiple_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.view_bulk_action_menu_by_checking_multiple()
        time.sleep(2)
        tl.change_status_in_multiple_via_bulk_action("Done")
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Done")
        time.sleep(2)

    def test_tc_126_add_dependency_to_the_subtask(self, authenticated_page):
        """
        Test Case - TC# : 126
        Name : Add dependency to the subtask 
        Summary : Check whether user able to add existing task as dependency to the subtask in ToDo
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_subtask()
        time.sleep(2)
        tl.open_sub_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_sub_task_dependency_in_task_drawer("To Do")
        time.sleep(2)

    def test_tc_127_change_the_task_with_subtask_to_done_when_all_dependencies_are_done(self, authenticated_page):
        """
        Test Case - TC# : 127
        Name : Change the Task with Subtask to Done when All Dependencies are  Done
        Summary : Check whether user able to change the status of both the task and subtask to "Done" when all their dependencies are marked as "Done."
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Done")
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.get_random_task_by_phase("Done")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_subtask()
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.open_sub_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_sub_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Done")
        time.sleep(2)

    def test_tc_128_add_same_dependency_to_task(self, authenticated_page):
        """
        Test Case - TC# : 128
        Name : Add same Dependency to task
        Summary : Check whether user unable to add an already existing dependency
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
        tl.add_same_dependency_via_task_drawer()
        time.sleep(2)

################################################################################################################
    # def test_tc_129_adding_non_existent_task_as_dependencies(self, authenticated_page):
    #     """
    #     Test Case - TC# : 129
    #     Name : Adding Non-existent task as dependencies
    #     Summary : Check whether user unable to add a dependency that does not exist in the project 
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.get_all_task_names()
    #     time.sleep(2)
    #     tl.add_a_task(True)
    #     time.sleep(2)
    #     tl.open_task_drawer()
    #     time.sleep(2)
    #     tl.add_non_existing_dependency_via_task_drawer()
    #     time.sleep(2)

    # def test_tc_130_adding_dependency_with_empty_field(self, authenticated_page):
    #     """
    #     Test Case - TC# : 130
    #     Name : Adding Dependency with empty field
    #     Summary : Check whether user unable to add a dependency with empty field
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.get_all_task_names()
    #     time.sleep(2)
    #     tl.add_a_task(True)
    #     time.sleep(2)
    #     tl.open_task_drawer()
    #     time.sleep(2)
    #     tl.add_empty_dependency_via_task_drawer()
    #     time.sleep(2)
################################################################################################################

    def test_tc_131_change_task_as_done_when_dependency_is_in_to_do(self, authenticated_page):
        """
        Test Case - TC# : 131
        Name : Change Task as Done when Dependency is in "To Do"
        Summary : Check whether user unable to Change Task as Done when Dependency is not done
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
        tl.change_status_to_done_when_dependency_is_not_done("Done")
        time.sleep(2)

    def test_tc_132_change_task_as_done_when_dependency_is_in_doing(self, authenticated_page):
        """
        Test Case - TC# : 132
        Name : Change Task as Done when Dependency is in "Doing"
        Summary : Check whether user unable to Change Task as Done when Dependency is in "Doing"
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
        tl.close_task_drawer()
        time.sleep(2)
        tl.get_random_task_by_phase("Doing")
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
        tl.change_status_when_dependency_is_not_done("Done")
        time.sleep(2)

    def test_tc_133_change_task_as_doing_when_dependency_is_in_todo(self, authenticated_page):
        """
        Test Case - TC# : 133
        Name : Change Task as Doing when Dependency is in "To Do"
        Summary : Check whether user unable to Change Task as Done when Dependency is in "To Doing"
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
        tl.change_status_via_task_drawer("Doing")
        time.sleep(2)

    def test_tc_134_change_task_to_done_when_all_multiple_dependencies_are_not_done(self, authenticated_page):
        """
        Test Case - TC# : 134
        Name : Change Task to Done when all Multiple Dependencies are not Done
        Summary : Check whether user unable to change task as done when all Multiple Dependencies are not Done
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
        tl.close_task_drawer()
        time.sleep(2)
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
        tl.get_random_task_by_phase("Doing")
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
        tl.change_status_when_dependency_is_not_done("Done")
        time.sleep(2)

    def test_tc_135_change_task_to_done_when_one_of_dependency_is_not_done(self, authenticated_page):
        """
        Test Case - TC# : 135
        Name : Change Task to Done when One of Dependency is Not Done
        Summary : Check whether user unable to change a task's status to "Done" when one of the dependencies is not marked as "Done"
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Done")
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
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
        tl.get_random_task_by_phase("Done")
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
        tl.change_status_when_dependency_is_not_done("Done")
        time.sleep(2)

    def test_tc_136_change_subtask_to_done_when_dependency_is_not_done(self, authenticated_page):
        """
        Test Case - TC# : 136
        Name : Change Subtask to Done when Dependency is Not Done
        Summary : Check whether user unable to change a subtask’s status to "Done" when dependency is still in "To Do" or "Doing"
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_subtask()
        time.sleep(2)
        tl.open_sub_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_sub_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.open_sub_task_drawer()
        time.sleep(2)
        tl.change_status_when_dependency_is_not_done("Done")
        time.sleep(2)

    def test_tc_137_change_subtask_to_done_when_dependency_is_not_done(self, authenticated_page):
        """
        Test Case - TC# : 137
        Name : Change Task to Done (Subtask Dependency is not Done)
        Summary : Check whether user unable to change a task’s status to "Done" when the task dependencies are "Done" but the subtask dependencies are in "To Do" or "Doing"
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_via_task_drawer("Done")
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.get_random_task_by_phase("Done")
        time.sleep(2)
        tl.add_a_task(True)
        time.sleep(2)
        tl.add_subtask()
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_main_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.get_random_task_by_phase("To Do")
        time.sleep(2)
        tl.open_sub_task_drawer()
        time.sleep(2)
        tl.add_dependency_via_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.close_task_drawer()
        time.sleep(2)
        tl.verify_sub_task_dependency_in_task_drawer("To Do")
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_status_when_dependency_is_not_done("Done")
        time.sleep(2)