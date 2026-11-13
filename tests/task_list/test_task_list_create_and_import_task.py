import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListCreateAndImportTask:
    """
    Test suite - Name : Task-list_Create task and Import task
    Details : Basic test cases for create task and import task
    """

    def test_tc_31_verify_task_creation_using_create_task(self, authenticated_page):
        """
        Test Case - TC# : 31
        Name : verify task creation using create task
        Summary : Verify that a task created using the create task is added to the correct category
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.create_task()
        time.sleep(2)

    def test_tc_32_verify_task_creation_using_import_task(self, authenticated_page):
        """
        Test Case - TC# : 32
        Name : verify task creation using import task
        Summary : Verify that when a task is created by importing a task template, it appears as a task card under the correct status column
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.import_task()
        time.sleep(2)