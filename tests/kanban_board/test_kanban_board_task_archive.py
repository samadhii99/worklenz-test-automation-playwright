import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage

@pytest.mark.ui
class TestKanbanBoardResponsiveness:
    """
    Test suite - Name :  Kanban Board Task Archive
    Details : Basic test cases for tasks archive
    """

    def test_tc_36_verify_archive_a_task(self, authenticated_page):
        """
        Test Case - TC# : 36
        Name : Verify Archive a task
        Summary : Check that user can archive a task through Kanban board
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.archive_task()
        time.sleep(2)

    def test_tc_37_verify_archived_tasks_displayed(self, authenticated_page):
        """
        Test Case - TC# : 37
        Name : Verify Archived tasks displayed
        Summary : Check that user can see the archived tasks
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.archive_task()
        time.sleep(2)
        kb.verify_archived()
        time.sleep(2)

    def test_tc_38_verify_unarchive_a_task(self, authenticated_page):
        """
        Test Case - TC# : 38
        Name : Verify Unarchive a task
        Summary : Check that user can Unarchive a task
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.archive_task()
        time.sleep(2)
        kb.verify_archived()
        time.sleep(2)
        kb.unarchive_task()
        time.sleep(2)

    def test_tc_39_verify_unarchived_task_displayed(self, authenticated_page):
        """
        Test Case - TC# : 39
        Name : Verify Unarchive task displayed
        Summary : Check that user can see the unarchived task in active task list
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.archive_task()
        time.sleep(2)
        kb.verify_archived()
        time.sleep(2)
        kb.unarchive_task()
        time.sleep(2)
        kb.verify_unarchived()
        time.sleep(2)