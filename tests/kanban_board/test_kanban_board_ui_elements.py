import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage

@pytest.mark.ui
class TestKanbanBoardUIElements:
    """
    Test suite - Name : Kanban Board_UI elements
    Details : Basic test cases for Kanban BoardUI Element
    """

    def test_tc_01_verify_ui_elements(self, authenticated_page):
        """
        Test Case - TC# : 01
        Name : Verify UI elements
        Summary : Check that All UI elements are present on the Board
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.verify_ui_elements()
