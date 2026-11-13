import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage
from utilities.responsive_utils import set_viewport

@pytest.mark.ui
class TestKanbanBoardResponsiveness:
    """
    Test suite - Name :  Kanban Board_Responsiveness
    Details : Basic Test Cases for check Responsiveness of Kanban Board
    """

    def test_tc_33_responsiveness_for_laptop_screen(self, authenticated_page):
        """
        Test Case - TC# : 33
        Name : Responsiveness for Laptop Screen
        Summary : Verify if the LogIn page displays correctly and is responsive for the Laptop screen size 
        """
        page = authenticated_page
        set_viewport(page, "laptop")
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)

    def test_tc_34_responsiveness_for_pc_screen(self, authenticated_page):
        """
        Test Case - TC# : 34
        Name : Responsiveness for PC Screen
        Summary : Verify if the LogIn page displays correctly and is responsive for the PC screen size 
        """
        page = authenticated_page
        set_viewport(page, "pc")
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
    
    def test_tc_35_responsiveness_for_ipad_screen(self, authenticated_page):
        """
        Test Case - TC# : 35
        Name : Responsiveness for IPad Screen
        Summary :  Verify if the Login page displays correctly and is responsive for the iPad screen size using Google DevTools
        """
        page = authenticated_page
        set_viewport(page, "ipad")
        kb = KanbanBoardPage(page)
        kb.open_kanban_board_in_ipad()
        time.sleep(3)