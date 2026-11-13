import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage

@pytest.mark.ui
class TestKanbanBoardTaskAssignToMe:
    """
    Test suite - Name :  Kanban board task "Assign to me" option
    Details : Basic test case for 'Assign to me' option
    """

    def test_tc_40_verify_assign_to_me(self, authenticated_page):
        """
        Test Case - TC# : 40
        Name : Verify 'Assign to me' option 
        Summary : Check that user can assign a task to themselves through Assign to me option
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.add_a_task_by_kanban_card(False)
        time.sleep(2)
        kb.assign_to_me()
        time.sleep(2)
        kb.verify_assigned_to_me()
        time.sleep(2)