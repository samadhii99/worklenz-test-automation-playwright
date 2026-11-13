import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage

@pytest.mark.ui
class TestKanbanBoardCreateAndImportTask:
    """
    Test suite - Name : Kanban Board_Create task and Import task
    Details : Basic Test cases for Create task and Import task
    """

    def test_tc_16_verify_task_creation_using_create_task(self, authenticated_page):
        """
        Test Case - TC# : 16
        Name : Verify task creation using "Create Task" 
        Summary : Verify that a task created using the "Create Task" is added to the correct status column as a  task card
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.create_task()
        time.sleep(2)

    def test_tc_17_verify_task_creation_using_import_task(self, authenticated_page):
        """
        Test Case - TC# : 17
        Name : Verify task creation using "Import Task" 
        Summary : Verify that when a task is created by importing a task template, it appears as a task card under the correct status column.
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.import_task()
        time.sleep(2)