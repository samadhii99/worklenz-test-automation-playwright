import pytest
import time
from pages.kanban_board.kanban_board_page import KanbanBoardPage

@pytest.mark.ui
class TestKanbanBoardFilters:
    """
    Test suite - Name : Kanban Board_Filters
    Details : Basic Test cases for Kanban Board filters
    """

    def test_tc_02_task_search_by_name(self, authenticated_page):
        """
        Test Case - TC# : 02
        Name : Task search By Name
        Summary : Check Whether user able to search tasks by task name
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.get_random_task_name()
        time.sleep(2)
        kb.task_search_by_name()
        time.sleep(2)

    def test_tc_03_reset_kanban_board(self, authenticated_page):
        """
        Test Case - TC# : 03
        Name : Reset Kanban Board
        Summary : Check whether user able to reset Board after searching task name
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.get_random_task_name()
        time.sleep(2)
        kb.task_search_by_name()
        time.sleep(2)
        kb.reset_task_list()
        time.sleep(2)

    def test_tc_12_priority_filter(self, authenticated_page):
        """
        Test Case - TC# : 12
        Name : Priority Filter
        Summary : Check whether user able to filter tasks by Priority
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.priority_filter(False) #filter by single priority
        time.sleep(2)
        kb.priority_filter(True) #filter by multiple priorities
        time.sleep(2)

    def test_tc_13_labels_filter(self, authenticated_page):
        """
        Test Case - TC# : 13
        Name : Labels Filter
        Summary : Check whether user able to filter tasks by Label
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.labels_filter(False) #filter by one label
        time.sleep(2)
        kb.labels_filter(True) #filter by multiple labels
        time.sleep(2)

    def test_tc_14_member_filter(self, authenticated_page):
        """
        Test Case - TC# : 14
        Name : Member Filter
        Summary : Check whether user is able to filter tasks by members
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.member_filter(False) #filter by single member
        time.sleep(2)
        kb.member_filter(True) #filter by multiple members
        time.sleep(2)

    def test_tc_15_non_existant_task_search_by_name(self, authenticated_page):
        """
        Test Case - TC# : 15
        Name : Search Non-existant Task
        Summary : Check Whether user unable to search Non-existant tasks by task name
        """
        page = authenticated_page
        kb = KanbanBoardPage(page)
        kb.open_kanban_board()
        time.sleep(3)
        kb.task_search_by_non_existant_name()
        time.sleep(2)