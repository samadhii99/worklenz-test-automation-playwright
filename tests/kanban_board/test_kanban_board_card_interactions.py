import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage

@pytest.mark.ui
class TestKanbanBoardCardInteractions:
    """
    Test suite - Name : Kanban Board Card Interactions
    Details : Basic test cases for  Kanban Board Card Interactions
    """

    def test_tc_18_add_task_at_the_top_of_the_status_column(self, authenticated_page):
        """
        Test Case - TC# : 18
        Name : Add Task at the Top of the Status Column
        Summary : Check whether user able to add a task at the top of the Status Column
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_phase_column()
        time.sleep(2)

    def test_tc_19_add_task_at_the_bottom_of_the_status_column(self, authenticated_page):
        """
        Test Case - TC# : 19
        Name : Add Task at the Bottom of the Status Column
        Summary : Check whether user able to add a task at the Bottom of the Status Column
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)

################################################################################################################
    # def test_tc_20_drag_and_drop_status_column(self, authenticated_page):
    #     """
    #     Test Case - TC# : 20
    #     Name : Drag and Drop Status Column
    #     Summary : Verify the ability to drag and drop a entire column between different columns.
    #     """
    #     page = authenticated_page
    #     kb = KanbanBoardPage(page)
    #     kb.open_kanban_board()
    #     time.sleep(3)
    #     kb.add_a_task_by_kanban_card(False)
    #     time.sleep(2)
    #     kb.drag_and_drop()
    #     time.sleep(2)
################################################################################################################

    def test_tc_21_rename_status_name(self, authenticated_page):
        """
        Test Case - TC# : 21
        Name : Rename Status column name
        Summary : Check whether user able to rename status name
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.rename_status_column()
        time.sleep(2)

    def test_tc_22_change_category(self, authenticated_page):
        """
        Test Case - TC# : 22
        Name : Change Category of Column
        Summary : Check whether user able to change category of the column
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.change_main_category("Doing")
        time.sleep(2)
        kb.change_new_category("Done")
        time.sleep(2)

    def test_tc_23_delete_status_with_no_task(self, authenticated_page):
        """
        Test Case - TC# : 23
        Name : Delete Status with No Task
        Summary : Verify that the user is able to delete a status that does not contain any tasks.
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.create_new_category()
        time.sleep(2)
        kb.delete_category(False)
        time.sleep(2)

    def test_tc_24_delete_status_with_task(self, authenticated_page):
        """
        Test Case - TC# : 24
        Name : Delete Status with Task
        Summary : Verify that user is able to delete a status that contain tasks after moving tasks to another status
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.create_new_category()
        time.sleep(2)
        kb.add_a_task_by_kanban_card(True)
        time.sleep(2)
        kb.add_a_task_by_kanban_card(True)
        time.sleep(2)
        kb.delete_category(True)
        time.sleep(2)

    def test_tc_25_add_new_status(self, authenticated_page):
        """
        Test Case - TC# : 25
        Name : Add new status(Column)
        Summary : Check whether user able to add new status to the board
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.group_by("Status")
        time.sleep(2)
        kb.click_manage_button("Manage Statuses")
        time.sleep(2)
        kb.create_new_status("Test Status")
        time.sleep(2)

    def test_tc_26_add_due_date(self, authenticated_page):
        """
        Test Case - TC# : 26
        Name : Add Due date to the task
        Summary : Check whether user able to Add due date to the task
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.add_due_date()
        time.sleep(2)

    def test_tc_27_change_due_date(self, authenticated_page):
        """
        Test Case - TC# : 27
        Name : Change Due date of the task
        Summary : Check whether user able to change due date of the task
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.add_due_date()
        time.sleep(2)
        kb.change_due_date()
        time.sleep(2)

    def test_tc_28_add_assignees(self, authenticated_page):
        """
        Test Case - TC# : 28
        Name : Add Assignees to the task
        Summary : Check whether user able to Add Assignees to the task
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.assign_members_for_task()
        time.sleep(2)

    def test_tc_29_invite_a_new_member_by_email(self, authenticated_page):
        """
        Test Case - TC# : 29
        Name : Invite a New member By Email
        Summary : Check whether user able to invite a new member to the project
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.invite_members_for_task()
        time.sleep(2)

################################################################################################################
    # def test_tc_30_drag_and_drop_task_card(self, authenticated_page):
    #     """
    #     Test Case - TC# : 30
    #     Name : Drag and Drop Task Card
    #     Summary : Verify the ability to drag and drop a task card between different columns.
    #     """
    #     page = authenticated_page
    #     kb = KanbanBoardPage(page)
    #     kb.open_kanban_board()
    #     time.sleep(2)
    #     kb.add_a_task_by_kanban_card(False)
    #     time.sleep(2)
    #     kb.drag_and_drop_task_to_different_phase("Doing")
    #     time.sleep(2)
################################################################################################################

    def test_tc_31_drag_and_drop_task_card(self, authenticated_page):
        """
        Test Case - TC# : 31
        Name : Open Task drawer
        Summary : Verify user able to open task drawer of the task
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.open_task_drawer()
        time.sleep(2)

    def test_tc_32_deletion_of_single_status_in_a_category(self, authenticated_page):
        """
        Test Case - TC# : 32
        Name : Deletion of Single Status in a Category
        Summary : Verify that the system restricts users from deleting a status if it is the only one remaining in a category
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(2)
        kb.click_manage_button("Manage Statuses")
        time.sleep(2)
        kb.get_single_status_category()
        time.sleep(2)
        kb.delete_category_in_single_status()
        time.sleep(2)