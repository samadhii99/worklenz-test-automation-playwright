import pytest
import time
from pages.task_list.task_list_page import TaskListPage

@pytest.mark.filters
class TestTaskListTaskDrawerInfo:
    """
    Test suite - Name : Task-list Task Drawer/Info
    Details : Basic test cases for task drawer/info
    """

    def test_tc_74_add_phase_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 74
        Name : add phase to the task
        Summary : Check whether user able to add a phase for the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_phase_to_the_task_via_task_drawer()
        time.sleep(2)

    def test_tc_75_add_assignees_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 75
        Name : add assignees to the task
        Summary : Check whether user able to add assignees to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.assign_task_to_members_in_drawer()
        time.sleep(2)
        tl.verify_assigned_members_in_task_drawer()
        time.sleep(2)

    def test_tc_76_search_members_when_assigning(self, authenticated_page):
        """
        Test Case - TC# : 76
        Name : search members when assigning
        Summary : Check whether user can search members when adding assignees to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.search_members_in_assign_members_section_in_drawer()
        time.sleep(2)
        tl.verify_assigned_members_in_task_drawer()
        time.sleep(2)

    def test_tc_77_add_due_date(self, authenticated_page):
        """
        Test Case - TC# : 77
        Name : add due date
        Summary : Check whether user able to add due date to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_due_date_in_drawer()
        time.sleep(2)

    def test_tc_78_add_start_date(self, authenticated_page):
        """
        Test Case - TC# : 78
        Name : add start date
        Summary : Check whether user able to add start date to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_start_date_in_drawer()
        time.sleep(2)

    def test_tc_79_add_time_estimation(self, authenticated_page):
        """
        Test Case - TC# : 79
        Name : add time estimation
        Summary : Check whether user able to add estimated time to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_estimated_time_in_drawer()
        time.sleep(2)

    def test_tc_80_estimation_time_minutes_field(self, authenticated_page):
        """
        Test Case - TC# : 80
        Name : estimation time minutes field
        Summary : Verify that the "Minutes" field accepts a maximum input of 60 and disables the increment icon after reaching the limit and does not accept any value above 60.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.check_estimated_time_minutes_max_in_drawer()
        time.sleep(2)

    def test_tc_81_change_priority(self, authenticated_page):
        """
        Test Case - TC# : 81
        Name : change priority
        Summary : Check Whether user able to Change priority of the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_priority_via_task_drawer()
        time.sleep(2)

    def test_tc_82_add_label(self, authenticated_page):
        """
        Test Case - TC# : 82
        Name : add label
        Summary : Check Whether user able to add labels for a task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_label_via_task_drawer()
        time.sleep(2)

    def test_tc_83_add_label_by_creating_new_label(self, authenticated_page):
        """
        Test Case - TC# : 83
        Name : add label by creating new label
        Summary : Check Whether user able to add new label for a task by creating new label
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.create_label_via_task_drawer()
        time.sleep(2)

    def test_tc_84_enable_billable_task(self, authenticated_page):
        """
        Test Case - TC# : 84
        Name : enable billable task
        Summary : Verify that a task can be marked as billable by enabling the Billable toggle
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.billable_toggle_via_task_drawer(True)
        time.sleep(2)

    def test_tc_85_disable_billable_task(self, authenticated_page):
        """
        Test Case - TC# : 84
        Name : disable billable task
        Summary : Verify that a task can be marked as non-billable by enabling the Billable toggle
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.billable_toggle_via_task_drawer(False)
        time.sleep(2)

    def test_tc_86_when_done_notify_field(self, authenticated_page):
        """
        Test Case - TC# : 86
        Name : when done notify field
        Summary : Verify that the user can add a member to a task after task is completed to notify them of its completion
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.notify_members_via_task_drawer()
        time.sleep(2)

    def test_tc_87_add_description_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 87
        Name : add description to the task
        Summary : Check whether user able to add description to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_description_via_task_drawer()
        time.sleep(2)

    def test_tc_88_add_bold_and_italic_text_in_the_description_field(self, authenticated_page):
        """
        Test Case - TC# : 88
        Name : add bold and italic text in the description field
        Summary : Verify that the user can format text as both bold and italic in the task description field
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_bold_and_italic_text_to_description_via_task_drawer()
        time.sleep(2)

    def test_tc_89_add_bullet_points_in_the_description_field(self, authenticated_page):
        """
        Test Case - TC# : 89
        Name : add bullet points in the description field
        Summary : Verify that the user can add bullet points in the task description field
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_bullet_points_to_description_via_task_drawer()
        time.sleep(2)

    def test_tc_90_add_numbered_list_in_the_description_field(self, authenticated_page):
        """
        Test Case - TC# : 90
        Name : add numbered list in the description field
        Summary : Verify that the user can add numbered list in the task description field
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_numbered_list_to_description_via_task_drawer()
        time.sleep(2)

################################################################################################################
    # def test_tc_91_change_text_alignment_in_the_description_field(self, authenticated_page):
    #     """
    #     Test Case - TC# : 91
    #     Name : Change Text Alignment in the Description Field
    #     Summary : Verify that the user can change the text alignment (left, center, right, or justified) in the description field.
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.add_a_task(True)
    #     time.sleep(2)
    #     tl.open_task_drawer()
    #     time.sleep(2)
    #     tl.change_text_alignment_to_description_via_task_drawer()
    #     time.sleep(2)
################################################################################################################

    def test_tc_92_add_a_hyperlink_in_the_description_field(self, authenticated_page):
        """
        Test Case - TC# : 92
        Name : Add a hyperlink in the Description Field
        Summary : Verify that the user can add a hyperlink to the task description field.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_hyperlink_to_description_via_task_drawer()
        time.sleep(2)

    def test_tc_93_change_text_type_in_the_description_field(self, authenticated_page):
        """
        Test Case - TC# : 93
        Name : Change Text Type (Heading, Paragraph.)
        Summary : Verify that text in the task description field can be changed to different text types, such as Paragraph or Heading.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.change_text_type_to_description_via_task_drawer()
        time.sleep(2)

    def test_tc_94_add_sub_task(self, authenticated_page):
        """
        Test Case - TC# : 94
        Name : Add sub task
        Summary : Check whether user able to add subtask
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_sub_task_via_task_drawer(True)
        time.sleep(2)

    def test_tc_95_add_dependency(self, authenticated_page):
        """
        Test Case - TC# : 95
        Name : Add dependency
        Summary : Check whether able to add dependency to the tasks
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

    def test_tc_96_add_attachment_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 96
        Name : Add Attachment to the task
        Summary : Check whether user able to add Attachments to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_attachment_via_task_drawer(False)
        time.sleep(2)

    def test_tc_97_add_multiple_attachment_to_the_task(self, authenticated_page):
        """
        Test Case - TC# : 97
        Name : Add Multiple Attachments to a Task
        Summary : Verify that the user can add multiple attachments to a task.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_attachment_via_task_drawer(True)
        time.sleep(2)

    def test_tc_99_add_multiple_attachment_types_to_a_task(self, authenticated_page):
        """
        Test Case - TC# : 99
        Name : Add Multiple Attachment Types to a Task
        Summary : Verify that the user can upload multiple types of attachments (e.g., images, documents, PDFs.) to a task.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_multiple_attachment_types_via_task_drawer()
        time.sleep(2)

################################################################################################################
    # def test_tc_100_tooltips_for_attachments(self, authenticated_page):
    #     """
    #     Test Case - TC# : 100
    #     Name : Tooltip for Attachments
    #     Summary : Verify that a tooltip is displayed for attachments, showing the attachment name
    #     """
    #     page = authenticated_page
    #     tl = TaskListPage(page)
    #     tl.open_task_list()
    #     time.sleep(3)
    #     tl.add_a_task(True)
    #     time.sleep(2)
    #     tl.open_task_drawer()
    #     time.sleep(2)
    #     tl.add_attachment_via_task_drawer(False)
    #     time.sleep(2)
    #     tl.add_multiple_attachment_types_via_task_drawer()
    #     time.sleep(2)
################################################################################################################

    def test_tc_101_preview_an_uploaded_attachment(self, authenticated_page):
        """
        Test Case - TC# : 101
        Name : Preview an Uploaded Attachment
        Summary : Verify that the user can preview uploaded attachments.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_attachment_via_task_drawer(False)
        time.sleep(2)
        tl.preview_attachment_via_task_drawer()
        time.sleep(2)

    def test_tc_102_download_an_uploaded_attachment(self, authenticated_page):
        """
        Test Case - TC# : 102
        Name : Download an Uploaded Attachment
        Summary : Verify that the user can download an uploaded attachments.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_attachment_via_task_drawer(False)
        time.sleep(2)
        tl.download_attachment_via_task_drawer()
        time.sleep(2)

    def test_tc_103_delete_an_attachment(self, authenticated_page):
        """
        Test Case - TC# : 103
        Name : Delete an Attachment
        Summary : Verify that the user can delete an uploaded attachment.
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_attachment_via_task_drawer(False)
        time.sleep(2)
        tl.delete_attachment_via_task_drawer()
        time.sleep(2)

    def test_tc_104_add_comment(self, authenticated_page):
        """
        Test Case - TC# : 104
        Name : Add comment
        Summary : Check whether user able to Add comment to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_comment_via_task_drawer(True)
        time.sleep(2)

    def test_tc_105_add_comment_with_attachmant(self, authenticated_page):
        """
        Test Case - TC# : 105
        Name : Add comment with attachment
        Summary : Check whether user able to Add comment with Attachment to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_comment_with_attachment_via_task_drawer()
        time.sleep(2)

    def test_tc_106_add_sub_task_with_empty_name(self, authenticated_page):
        """
        Test Case - TC# : 106
        Name : Add sub task with empty name
        Summary : Check whether user able to Add comment with Attachment to the task
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_sub_task_via_task_drawer(False)
        time.sleep(2)

    def test_tc_107_add_empty_comment(self, authenticated_page):
        """
        Test Case - TC# : 107
        Name : Add empty comment
        Summary : Check whether user unable to add empty comment
        """
        page = authenticated_page
        tl = TaskListPage(page)
        tl.open_task_list()
        time.sleep(3)
        tl.add_a_task(True)
        time.sleep(2)
        tl.open_task_drawer()
        time.sleep(2)
        tl.add_comment_via_task_drawer(False)
        time.sleep(2)