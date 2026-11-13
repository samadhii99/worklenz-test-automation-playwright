from cmath import phase
from pages.base_page import BasePage
from playwright.sync_api import Page
from datetime import datetime, timedelta
from faker import Faker
from pathlib import Path
import random
import re

from tests.conftest import page

class TaskListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.faker = Faker()
        self.tasks_details = []
        self.filter_button = "button.rounded-md.font-medium"
        self.filter_button_value = "button.flex.w-full"
        self.header = "div.text-sm"
        

        #manage phase/status card locators
        self.manage_button = "button.font-semibold.px-3"
        self.manage_status_phase_card = "div.ant-modal-content"
        self.status_cards = "div.transition-all.rounded-lg"
        self.phase_cards = "div.rounded.group"

        #task_list board locators
        self.task = "span.text-gray-700.text-sm"
        self.assignees = "div.px-2.gap-1"
        self.priority = "div:nth-of-type(8) button.inline-flex"
        self.status = "div.flex:nth-of-type(5) button"
        self.labels = "div.min-w-0.flex-wrap"
        self.phase = "div.flex:nth-of-type(8) button"
        self.end_date = "span.whitespace-nowrap"
        self.start_date = "div:nth-of-type(11) span.text-gray-400.text-sm"
        self.completed_date = ".min-w-max div.flex:nth-of-type(13)"
        self.created_date = ".min-w-max div.flex:nth-of-type(12)"
        self.phase_list = "xpath=//*[starts-with(@id, 'rc-tabs-') and contains(@id, '-panel-tasks-list')]/div/div[2]/div/div/div[2]/div"

        #create task locators
        self.create_task_button = "button.ant-btn-compact-first-item"
        self.create_task_card = "div.ant-drawer-content[role='dialog']"
        self.task_name = "p.task-name-display"

        #import task locators
        self.import_dropdown = "button.ant-btn-icon-only.ant-btn-primary"
        self.import_task_option = "li.ant-dropdown-menu-item"
        self.template_name_dropdown = "input.ant-select-selection-search-input"
        self.template_list = "div.rc-virtual-list-holder-inner div.ant-select-item-option"
        self.selected_tasks = ".ant-list-item span.ant-typography"
        
    def open_task_list(self):
        self.wait_for_selector("li[data-menu-id*='projects']")
        self.page.locator("li[data-menu-id*='projects']").click()
        self.page.wait_for_timeout(2000)
        self.wait_for_selector("span.ant-page-header-heading-title")
        tbody = self.page.locator("tbody")
        if tbody.count() > 0:
            tbody_text = tbody.inner_text().strip()
            if "No projects found" in tbody_text:
                raise AssertionError("No tasks found in the project")

        # Case 2: tbody does not exist or has no rows
        if tbody.count() == 0:
            raise AssertionError("Table body not present")

        # Optional: Check rows inside tbody
        rows = tbody.locator("tr")
        if rows.count() == 0:
            raise AssertionError("Table body present but no task rows found")
            
        t_body = self.page.locator("tbody")
        rows = t_body.locator("tr").all()
        for row in rows:
            if row.locator(".ant-table-cell-row-hover .cursor-pointer span").first:
                project_name = row.locator(".cursor-pointer span").inner_text().strip()
                row.click()
                break
        self.wait_for_timeout(3000)
        project_tab_name = self.page.locator(".site-page-header").inner_text().strip()
        assert project_name in project_tab_name, "Open task list failed"

    def open_task_list_in_ipad(self):
        self.page.get_by_role("button").locator("span[aria-label='menu']").click()
        self.page.locator("//div[text()='Projects']").click()
        self.page.wait_for_timeout(2000)
        self.wait_for_selector("span.ant-page-header-heading-title")
        tbody = self.page.locator("tbody")
        if tbody.count() > 0:
            tbody_text = tbody.inner_text().strip()
            if "No projects found" in tbody_text:
                raise AssertionError("No tasks found in the project")

        # Case 2: tbody does not exist or has no rows
        if tbody.count() == 0:
            raise AssertionError("Table body not present")

        # Optional: Check rows inside tbody
        rows = tbody.locator("tr")
        if rows.count() == 0:
            raise AssertionError("Table body present but no task rows found")
            
        t_body = self.page.locator("tbody")
        rows = t_body.locator("tr").all()
        for row in rows:
            if row.locator(".ant-table-cell-row-hover .cursor-pointer span").first:
                project_name = row.locator(".cursor-pointer span").inner_text().strip()
                row.click()
                break
        self.wait_for_timeout(3000)
        project_tab_name = self.page.locator(".site-page-header").inner_text().strip()
        assert project_name in project_tab_name, "Open task list in ipad failed"
    
    def verify_ui_elements(self):
        assert self.page.locator(self.filter_button, has_text="Search").is_visible(), "Search input not visible"
        assert self.page.locator(self.filter_button, has_text="Sort").is_visible(), "Sort button not visible"
        assert self.page.locator(self.filter_button, has_text="Priority").is_visible(), "Priority button not visible"
        assert self.page.locator(self.filter_button, has_text="Members").is_visible(), "Members button not visible"
        assert self.page.locator(self.filter_button, has_text="Labels").is_visible(), "Labels button not visible"
        assert self.page.locator(self.filter_button, has_text="Group by").is_visible(), "Group by button not visible"
        assert self.page.locator("button.font-semibold", has_text="Manage Statuses").is_visible(), "Manage Status button not visible"
        assert self.page.locator("input.text-gray-600").is_visible(), "Show archived checkbox not visible"
        assert self.page.locator(".ml-auto button").is_visible(), "Fields button not visible"
        assert self.page.locator(".anticon-holder svg").first.is_visible(), "Task drag handler not visible"

        # # Verify tooltips in button hover in task list tab
        # # Search
        # self.page.locator(self.filter_button, has_text="Search").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Search").is_visible(), "Search not visible on hover"
        # # Sort
        # self.page.locator(self.filter_button, has_text="Sort").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Sort").is_visible(), "Sort not visible on hover"
        # # Priority
        # self.page.locator(self.filter_button, has_text="Priority").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Priority").is_visible(), "Priority not visible on hover"
        # # # Members
        # self.page.locator(self.filter_button, has_text="Members").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Members").is_visible(), "Members not visible on hover"
        # # # Labels
        # self.page.locator(self.filter_button, has_text="Labels").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Labels").is_visible(), "Labels not visible on hover"
        # # Group by
        # self.page.locator(self.filter_button, has_text="Group by").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Group by").is_visible(), "Group by not visible on hover"
        # # Manage Statuses
        # self.page.locator("button.font-semibold", has_text="Manage Statuses").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Manage Statuses").is_visible(), "Manage Statuses not visible on hover"
        # # Show archived
        # self.page.locator("input.text-gray-600").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Show archived").is_visible(), "Show archived not visible on hover"
        # # Fields
        # self.page.locator(".ml-auto button").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Fields").is_visible(), "Fields not visible on hover"

        # verify UI elements by hovering

        # Hover over the open button and verify tooltip
        task_rows = self.page.locator("div.border-b.flex")
        first_task_row = task_rows.first
        task_column = first_task_row.locator("div.justify-between")
        task_column.hover()
        assert task_column.locator("button.duration-200.opacity-0").is_visible(), "Open button not visible when hovered"

        # Right click on the first task row to verify context menu
        task_column.click(button="right")
        self.page.locator("div.fixed").wait_for(state="visible")
        assert self.page.locator("div.fixed").is_visible(), "Context menu not visible on right click"

        # Click on the checkbox of the first task to verify bulk actions menu
        first_task_row.page.locator(".border-r input").first.click()
        self.page.locator("body > div:nth-of-type(2)").wait_for(state="visible")
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        assert bulk_actions_menu.is_visible(), "Bulk Actions menu not visible on checkbox click"

        # Hover the buttons in bulk actions menu to verify tooltip
        # Change Status
        bulk_actions_menu.page.locator(".anticon-retweet path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Change Status").is_visible(), "Change Status not visible on hover"
        # Change Priority
        bulk_actions_menu.page.locator(".ant-btn-icon .anticon-flag path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Change Priority").is_visible(), "Change Priority not visible on hover"
        # Change Phase
        bulk_actions_menu.page.locator(".anticon-bulb path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Change Phase").is_visible(), "Change Phase not visible on hover"
        # Add Labels
        bulk_actions_menu.page.locator(".anticon-tags path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Add Labels").is_visible(), "Add Labels not visible on hover"
        # Assign to me
        bulk_actions_menu.page.locator(".anticon-user-add path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Assign to Me").is_visible(), "Assign to Me not visible on hover"
        # Assign members
        bulk_actions_menu.page.locator(".ant-btn-text .anticon-usergroup-add path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Assign Members").is_visible(), "Assign Members not visible on hover"
        # Archive
        bulk_actions_menu.page.locator(".anticon-inbox path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Archive").is_visible(), "Archive not visible on hover"
        # Delete
        bulk_actions_menu.page.locator(".anticon-delete path").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Delete").is_visible(), "Delete not visible on hover"
        # More options
        bulk_actions_menu.page.locator(".anticon-more svg").hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="More options").is_visible(), "More options not visible on hover"
        # Clear Selection
        bulk_actions_menu.page.locator(".anticon-close svg").last.hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Clear Selection").is_visible(), "Clear Selection not visible on hover"
        
    def display_tooltips_in_columns(self):
        # Hover over the open button and verify tooltip
        task_rows = self.page.locator("div.border-b.flex")
        first_task_row = task_rows.first
        
        task_column = first_task_row.locator("span.text-gray-700")
        task_name = task_column.inner_text().strip()
        task_column.hover()
        self.page.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Assign to Me").is_visible(), "Assign to Me not visible on hover"

    def task_names(self):
        """Get project tasks names"""
        task_rows = self.page.locator("div.border-b.flex").all()
        self.all_tasks = len(task_rows)
        task_names = []
        
        for task_row in task_rows:            
            task_name_element = task_row.locator("span.text-gray-700.text-sm")
            if not task_name_element.is_visible():
                continue
            task_name = task_name_element.inner_text().strip()
            task_names.append(task_name)

        return task_names

    def get_project_tasks_with_details(self):
        """Get project tasks with details"""
        task_rows = self.page.locator("div.border-b.flex").all()
        self.all_tasks = len(task_rows)
        
        for task_row in task_rows:
            task_details = {
                "task_name": "",
                "task_members": [],
                "task_priority": "",
                "task_status": "",
                "task_label": [],
                "task_phase": ""
            }
            
            task_name_element = task_row.locator("span.text-gray-700.text-sm")
            if not task_name_element.is_visible():
                continue
            task_name = task_name_element.inner_text().strip()
            task_details["task_name"] = task_name
            
            member_cell = task_row.locator("div.px-2.gap-1")
            member_cell.locator(".rounded-full.w-5").first.click()
            member_dropdown = self.page.locator("div.fixed")
            members_list = member_dropdown.locator("div.p-2.flex").all()
            
            for member_list in members_list:
                checkbox_class = member_list.locator("div.w-4").get_attribute("class") or ""
                if "bg-blue-500 border-blue-500" in checkbox_class:
                    member = member_list.locator("div.font-medium.text-xs").inner_text().strip()
                    task_details["task_members"].append(member)
                else:
                    continue   
            member_cell.locator(".rounded-full.w-5").first.click()
            
            pritority_cell = task_row.locator("div:nth-of-type(8) button.inline-flex")
            priority_select_item = pritority_cell.locator("span.truncate").first
            priority = priority_select_item.inner_text().strip() or ""
            task_details["task_priority"] = priority
            
            status_cell = task_row.locator("div.flex:nth-of-type(5) button")
            status_select_item = status_cell.locator("span").first
            status = status_select_item.inner_text().strip() or ""
            task_details["task_status"] = status
            
            label_cell = task_row.locator("div.min-w-0.flex-wrap")
            label_cell.locator("button").first.click()
            label_dropdown = self.page.locator("div.fixed")
            labels_list = label_dropdown.locator("div.px-2.gap-2").all()
            
            for label in labels_list:
                checkbox_class = label.locator("div.w-4").get_attribute("class") or ""
                if "bg-blue-500 border-blue-500" in checkbox_class:
                    label_text = label.locator("div.font-medium").inner_text().strip()
                    task_details["task_label"].append(label_text)
                else:
                    continue
            
            label_cell.locator("button").first.click()
            
            task_list_header = self.page.locator("div.py-3")
            phase_header_exists = task_list_header.locator('div:has-text("Phase")').count() > 0

            if phase_header_exists:               
                try:
                    phase_cell = task_row.locator("div.flex:nth-of-type(8) button")
                    phase_select_item = phase_cell.locator("span").first
                    phase = phase_select_item.inner_text().strip() or ""
                    task_details["task_phase"] = phase
                except:
                    task_details["task_phase"] = ""
            if not phase_header_exists:
                self.page.locator(".ml-auto button").click()
                columns_dropdown = self.page.locator("div.top-full")
                phase_toggle = columns_dropdown.locator('button:has-text("Phase")')
                if phase_toggle.count() > 0:
                    phase_toggle.first.click()
                    self.page.locator(".ml-auto button").click()
                
                try:
                    phase_cell = task_row.locator("div.flex:nth-of-type(8) button")
                    phase_select_item = phase_cell.locator("span").first
                    phase = phase_select_item.inner_text().strip() or ""
                    task_details["task_phase"] = phase
                except:
                    task_details["task_phase"] = ""
            
            self.tasks_details.append(task_details)

    def task_search_by_name(self):

        if not self.tasks_details:
            return
        
        task_search_input = random.choice(self.tasks_details)["task_name"]
        searched_task_names = []

        self.page.locator(self.filter_button, has_text="Search").click()
        search_input = self.page.locator("input.w-full")
        search_input.fill(task_search_input)
        self.page.locator("button.transition-colors.rounded-md").click()
        self.page.wait_for_timeout(2000)
        
        task_rows = self.page.locator("div.border-b.flex").all()

        for task_row in task_rows:
            task_name_locator = task_row.locator("span.text-gray-700.text-sm")
            if task_name_locator.is_visible():
                task_name = task_name_locator.inner_text().strip()
                searched_task_names.append(task_name)
        
        # Fail if no results found
        assert searched_task_names, (f"No tasks found for search input: '{task_search_input}'")

        for searched_task_name in searched_task_names:
            assert task_search_input in searched_task_name, (f"Search failed: '{searched_task_name}' does not contain '{task_search_input}'")

    def reset_task_list(self):
        self.page.locator("button.duration-200.transition-colors.text-xs", has_text="Cancel").click()
        self.page.wait_for_timeout(2000)
        task_rows = self.page.locator("div.border-b.flex").all()
        reset_task_count = len(task_rows)
        assert reset_task_count == self.all_tasks, (f"Task list reset failed")

    def get_column_selector_by_text(self, column_name: str, start_index: int) -> str:
        headers = self.page.locator("div.text-sm")
        count = headers.count()

        for i in range(start_index, count):  # Playwright is 0-based
            header = self.page.locator(f"div.flex:nth-of-type({i+1})")
            header_text = header.first.inner_text().strip().lower()

            if column_name.lower() in header_text:
                return f"div.flex:nth-of-type({i + 1})"

        raise AssertionError(f"Column '{column_name}' not found starting from index {start_index}")

    def sort_filter_by(self,sort_type: str, status: bool = False):
        sort_button = self.page.locator(self.filter_button, has_text="Sort")
        sort_button.click()

        # Sort tasks by sort_type
        self.page.locator(self.filter_button_value, has_text=sort_type).click()
        self.page.wait_for_timeout(2000)

        # Verify sorting by task name
        task_names = []
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            task_rows = phase.locator("div.border-b.flex").all()
            sort_type = "Due Date" if sort_type == "End Date" else sort_type
            if sort_type == "Task":
                column_selector = self.task
            else:
                column_selector = self.get_column_selector_by_text(sort_type, start_index=1)
            for task_row in task_rows:
                task_name_locator = task_row.locator(column_selector)
                if task_name_locator.is_visible():
                    task_name = task_name_locator.inner_text().strip()
                    task_names.append(task_name)
            
            # Normalize for UI-style comparison
            def normalize(text: str):
                return text.casefold().replace(" ", "")
            if any(keyword.lower() in sort_type.lower() for keyword in ["date", "Last Updated"]):
                date_format = "%b %d, %Y"
                date_ui = []
                for date_str in task_names:
                    try:
                        date_ui.append(datetime.strptime(date_str, date_format))
                    except ValueError:
                        continue
                date_sorted = sorted(date_ui, reverse=status)
                assert date_ui == date_sorted, "Task sorting by Date failed"
            else:
                normalized_ui = [normalize(name) for name in task_names]
                normalized_sorted = sorted(normalized_ui, reverse=status)
                assert normalized_ui == normalized_sorted, "Task sorting Ascending by Task failed"
            task_names.clear()

    def priority_filter(self,multiple_priorities: bool):
        priority_button = self.page.locator(self.filter_button, has_text="Priority")
        priority_button.click()

        # Filter tasks by priority
        priorities = self.page.locator(self.filter_button_value).all()
        priority_filters = []
        multiple_limits = random.randint(2, len(priorities))
        for priority in random.sample(priorities, len(priorities)):
            priority_text = priority.inner_text().strip()
            priority.click()
            priority_filters.append(priority_text)
            
            if multiple_priorities:
                if len(priority_filters) < multiple_limits:
                    continue
                else:
                    break
            break       
            
        self.page.wait_for_timeout(2000)

        # Verify filter by priority
        priority_names = []
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            task_rows = phase.locator("div.border-b.flex").all()
            column_selector = self.get_column_selector_by_text("Priority", start_index=1)
            for task_row in task_rows:
                task_name_locator = task_row.locator(column_selector)
                if task_name_locator.is_visible():
                    priority_text = task_name_locator.inner_text().strip()
                    priority_names.append(priority_text)                 
            
                    # validate filtered values
                    assert all(name in priority_filters for name in priority_names), f"Task filter by {priority_filters} failed"
            priority_names.clear()

        # clear filter
        for priority_filter in priority_filters:
            self.page.locator(self.filter_button_value, has_text=priority_filter).click()
        self.page.wait_for_timeout(2000)
        priority_button.click()

    def labels_filter(self, multiple_labels: bool):
        labels_button = self.page.locator(self.filter_button, has_text="Labels")
        labels_button.click()

        # Filter tasks by labels
        labels = self.page.locator(self.filter_button_value).all()
        label_filters = []
        multiple_limits = random.randint(2, 5)
        for label in random.sample(labels, len(labels)):
            label_texts = label.inner_text().strip()
            label.click()
            label_filters.append(label_texts)
            
            if multiple_labels:
                if len(label_filters) < multiple_limits:
                    continue
                else:
                    break
            break       
            
        self.page.wait_for_timeout(2000)

        # Verify filter by labels
        label_names = []
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            task_rows = phase.locator("div.border-b.flex").all()
            column_selector = self.get_column_selector_by_text("Labels", start_index=1)
            for task_row in task_rows:
                task_name_locator = task_row.locator(column_selector)
                if task_name_locator.is_visible():
                    task_name_locator.locator("button").first.click()
                    label_dropdown = self.page.locator("div.fixed")
                    labels_list = label_dropdown.locator("div.px-2.gap-2").all() 
                    for label in labels_list:
                        checkbox_class = label.locator("div.w-4").get_attribute("class") or ""
                        if "bg-blue-500 border-blue-500" in checkbox_class:
                            label_text = label.locator("div.font-medium").inner_text().strip()
                            label_names.append(label_text)
                        else:
                            continue                   
            
                    # validate filtered values
                    assert any(name in label_filters for name in label_names), f"Task filter by {label_filters} failed"
            label_names.clear()

        # clear filter
        labels_button.click()
        for label_filter in label_filters:
            self.page.locator(self.filter_button_value, has_text=label_filter).click()
        self.page.wait_for_timeout(2000)
        labels_button.click()

    def member_filter(self, multiple_members: bool):
        members_button = self.page.locator(self.filter_button, has_text="Members")
        members_button.click()

        # Filter tasks by members
        members = self.page.locator(self.filter_button_value).all()
        member_filters = []
        multiple_limits = random.randint(1, len(members))
        for member in random.sample(members, len(members)):
            member_text = member.inner_text().strip().split("\n")[-1].strip()
            member.click()
            member_filters.append(member_text)
            
            if multiple_members:
                if len(member_filters) < multiple_limits:
                    continue
                else:
                    break
            break       
            
        self.page.wait_for_timeout(2000)

        # Verify filter by members
        members_names = []
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            task_rows = phase.locator("div.border-b.flex").all()
            column_selector = self.get_column_selector_by_text("Assignees", start_index=1)
            for task_row in task_rows:
                task_name_locator = task_row.locator(column_selector)
                if task_name_locator.is_visible():
                    task_name_locator.locator("button").first.click()
                    members_dropdown = self.page.locator("div.fixed")
                    members_list = members_dropdown.locator("div.p-2.flex").all() 
                    for member in members_list:
                        checkbox_class = member.locator("div.w-4").get_attribute("class") or ""
                        if "bg-blue-500 border-blue-500" in checkbox_class:
                            member_text = member.locator("div.font-medium").nth(1).inner_text().strip().split("\n")[-1]
                            members_names.append(member_text)
                        else:
                            continue                   
            
                    # validate filtered values
                    assert any(name in member_filters for name in members_names), f"Task filter by {member_filters} failed"
            members_names.clear()

        # clear filter
        members_button.click()
        for label_filter in member_filters:
            self.page.locator(self.filter_button_value, has_text=label_filter).click()
        self.page.wait_for_timeout(2000)
        members_button.click()

    def task_search_by_non_existant_name(self):
        task_search_input = "non_existent_task_name_12345"
        self.page.locator(self.filter_button, has_text="Search").click()
        search_input = self.page.locator("input.w-full")
        search_input.fill(task_search_input)
        self.page.locator("button.transition-colors.rounded-md").click()
        self.page.wait_for_timeout(2000)

        phase_list = self.page.locator(self.phase_list).all()
        for phase in phase_list:
            task_rows = phase.locator("div.border-b.flex").all()
            for task_row in task_rows:
                task_name_locator = task_row.locator("span.text-gray-700.text-sm")
                no_task_locator = task_row.locator("span.text-gray-500")
                if task_name_locator.is_visible():
                    assert False, "Non-existant task search by name failed"
                elif no_task_locator.is_visible():
                    assert no_task_locator.inner_text().strip() == "No tasks in this group", "Non-existant task search by name failed"

    def group_by(self, group_by: str):
        group_by_button = self.page.locator(self.filter_button, has_text="Group by")
        group_by_button.click()

        # Group by value
        group_list = self.page.locator(self.filter_button_value).all()
        for group in group_list:
            if group.inner_text().strip() == group_by:
                group.click()
                break   
            
        self.page.wait_for_timeout(2000)

        # Verify Group by value
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            task_phase_names = []
            phase_status = phase.locator("span.pr-2").inner_text().strip()
            if phase_status == "Unmapped":
                phase_status = "Select"
            task_rows = phase.locator("div.border-b.flex").all()
            column_selector = self.get_column_selector_by_text(group_by, start_index=1)
            for task_row in task_rows:
                task_locator = task_row.locator(column_selector)
                if task_locator.is_visible():
                    task_phase = task_locator.inner_text().strip()
                    task_phase_names.append(task_phase)
            
            # validate group by values
            assert all(name in phase_status for name in task_phase_names), f"Task group by {group_by} failed"
    
    def click_manage_button(self, config_name: str):
        manage_button = self.page.locator(self.manage_button, has_text=config_name)
        manage_button.click()

        self.page.wait_for_timeout(2000)
        manage_status_phase_card = self.page.locator(self.manage_status_phase_card)
        if manage_status_phase_card.is_visible():
            assert True, "Manage {config_name} Status button click failed"
    
    def create_new_status(self, status_name):
        test_status_name = status_name
        status_cards = self.page.locator(self.status_cards).all()

        for status in random.sample(status_cards, 1):
            status_name = status.locator("h5").inner_text().strip()
            status.locator("button", has_text="Add Status").first.click()
            inputbox = status.locator("input")
            create_btn = status.locator("button", has_text="Create")

            #fill input
            inputbox.fill(test_status_name)

            # VALIDATION: if input is empty, Create must be disabled
            if not test_status_name.strip():
                assert not create_btn.is_enabled(),("Create button should be disabled when status name is empty")
                return
            else:
                # If input is NOT empty, Create must be enabled
                assert create_btn.is_enabled(), ("Create button should be enabled when status name is provided")
                create_btn.click()
        
        self.page.wait_for_timeout(2000)

        #verify status created in manage status card
        status_cards = self.page.locator(self.status_cards).all()
        for status in status_cards:
            if status_name == status.locator("h5").inner_text().strip():
                sub_status_elements = status.locator("div.flex-1").all()
                sub_status_values = []
                for sub_status_ele in sub_status_elements:
                    sub_status = sub_status_ele.inner_text().strip()
                    sub_status_values.append(sub_status)
                
        assert test_status_name in sub_status_values, "Create new status failed"
        self.page.locator("button", has_text="Close").click()

        #verify status created in task list
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            if test_status_name ==  phase.locator("span.pr-2").inner_text().strip():
                assert True, "Create new status failed"
                break

    def create_new_phase(self, phase_name):
        test_phase_name = phase_name
        phase_cards = self.page.locator(self.phase_cards).all()

        self.page.locator("button", has_text="Add Option").first.click()
        self.page.locator("div.p-2").locator("input.flex-1").fill(test_phase_name)
        self.page.locator("div.p-2").locator("button", has_text="Create").click()

        inputbox = self.page.locator("div.p-2").locator("input.flex-1")
        create_btn = self.page.locator("div.p-2").locator("button", has_text="Create")

        #fill input
        inputbox.fill(test_phase_name)

        # VALIDATION: if input is empty, Create must be disabled
        if not test_phase_name.strip():
            assert not create_btn.is_enabled(), (
                "Create button should be disabled when phase name is empty"
            )
            return
        else:
            # If input is NOT empty, Create must be enabled
            assert create_btn.is_enabled(), (
                "Create button should be enabled when phase name is provided"
            )
            create_btn.click()
        
        self.page.wait_for_timeout(2000)

        #verify status created in manage status card
        phase_cards = self.page.locator(self.phase_cards).all()
        phase_values = []
        for phase_card in phase_cards:
            phase = phase_card.locator("div.flex-1").inner_text().strip()
            phase_values.append(phase)
                
        assert test_phase_name in phase_values, "Create new phase failed"
        self.page.locator("button", has_text="Close").click()

        #verify status created in task list
        phase_list = self.page.locator(self.phase_list).all()

        for phase in phase_list:
            if test_phase_name ==  phase.locator("span.pr-2").inner_text().strip():
                assert True, "Create new phase failed"
                break

    def select_phase(self, phase: str):
        phase_cards = self.page.locator(self.phase_cards).all()
        for phase_card in phase_cards:
            if phase == phase_card.locator("div.flex-1").inner_text().strip():
                current_color_style = phase_card.locator("div.ant-color-picker-color-block-inner").get_attribute("style") 
                phase_card.locator("div.ant-color-picker-color-block-inner").click()
                self.random_color_select()
                phase_card.locator("div.ant-color-picker-color-block-inner").click()
                self.page.wait_for_timeout(2000)
                new_color_style = phase_card.locator("div.ant-color-picker-color-block-inner").get_attribute("style")

                assert current_color_style != new_color_style, "Select phase color failed"
                break

    def delete_phase(self, phase: str):
        phase_cards = self.page.locator(self.phase_cards).all()
        for phase_card in phase_cards:
            if phase == phase_card.locator("div.flex-1").inner_text().strip():
                phase_card.hover()
                phase_card.locator(".anticon-delete path").click()
                self.page.locator(".ant-btn-dangerous span", has_text="Delete").click()
                self.page.wait_for_timeout(2000)
                break
        
        #verify deletion
        phase_cards = self.page.locator(self.phase_cards).all()
        phase_values = []
        for phase_card in phase_cards:
            phase_name = phase_card.locator("div.flex-1").inner_text().strip()
            phase_values.append(phase_name)
                
        assert phase not in phase_values, "Delete phase failed"

    def mark_show_archived(self, type: bool):
        show_archived_btn = self.page.locator("label:has-text('Show archived') input[type='checkbox']")
        all_tasks = self.task_names()
        show_archived_btn.click()
        self.page.wait_for_timeout(1000)
        assert show_archived_btn.is_checked(), "Mark show archived failed"
        if type == True:
            archived_tasks = self.task_names()
            assert archived_tasks != all_tasks, "Mark show archived failed"
            pass
        else:
            show_archived_btn.click()
            self.page.wait_for_timeout(1000)
            assert not show_archived_btn.is_checked(), "Mark show archived failed"
            unarchived_tasks = self.task_names()
            assert unarchived_tasks == all_tasks, "Mark show archived failed"
            pass

    def select_fields(self):
        fields_button = self.page.locator(self.filter_button, has_text="Fields")
        fields_button.click()

        fields_list = []

        fields = self.page.locator(self.filter_button_value).all()
        for field in fields:
            value =field.inner_text().strip()
            fields_list.append(value)
            checkbox_div = field.locator("div").first
            class_attr = checkbox_div.get_attribute("class") or ""

            is_checked = "bg-gray-600" in class_attr
            if not is_checked:
                field.click()
                    
        self.page.wait_for_timeout(2000)

        header_columns = self.page.locator(self.header).all()
        header_column_values = []
        for header_column in header_columns:
            header_column_values.append(header_column.inner_text().strip())

        fields_button.click()

        assert all(value in header_column_values for value in fields_list), "Select fields failed"

    def create_task(self):
        create_task_btn = self.page.locator(self.create_task_button)
        create_task_btn.click()
        self.page.wait_for_timeout(1000)

        create_task_card = self.page.locator(self.create_task_card)
        assert create_task_card.is_visible(), "Create task failed"

        task_name = self.faker.name()
        task_name_input = self.page.locator(self.task_name)
        task_name_input.click()
        self.page.locator("input[placeholder='Type your Task']").clear()
        self.page.locator("input[placeholder='Type your Task']").fill(task_name)
        self.page.wait_for_timeout(1000)
        assert task_name in self.task_names(), "Create task failed"

    def import_task(self):
        self.page.locator(self.import_dropdown).click()
        self.page.locator(self.import_task_option).click()
        self.page.wait_for_timeout(1000)

        import_task_card = self.page.locator(self.create_task_card)
        assert import_task_card.is_visible(), "Import task failed"

        self.page.locator(self.template_name_dropdown).click()
        self.page.locator(self.template_list).first.click()

        selected_tasks = []
        self.page.wait_for_timeout(3000)
        tasks = self.page.locator(self.selected_tasks).all()
        for task in tasks:
            task_name = task.inner_text().strip()
            selected_tasks.append(task_name)

        self.page.locator("button", has_text="Import").click()
        self.page.wait_for_timeout(2000)

        all_tasks = self.task_names()

        assert any(selected_task in all_tasks for selected_task in selected_tasks), "Import task failed"

    def change_category_name(self):
        status = self.faker.word()
        phase_task = self.page.locator(".flex > .ant-dropdown-trigger").first
        phase_task.click()
        self.page.get_by_text("Rename Status").click()
        self.page.get_by_role("textbox").fill(status)
        self.page.get_by_role("textbox").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify status name changed in task list
        phase = self.page.locator(self.phase_list).first
        phase_name = phase.locator("span.pr-2").inner_text().strip()

        assert status == phase_name, "Change category name failed"

        phase_task.click()
        self.page.get_by_text("Rename Status").click()
        self.page.get_by_role("textbox").fill("To Do")
        self.page.get_by_role("textbox").press("Enter")
        self.page.wait_for_timeout(2000)

    def change_category(self):
        self.page.locator(".flex > .ant-dropdown-trigger").first.click()
        self.page.get_by_text("Change Category").click()
        self.page.wait_for_timeout(2000)

        #verify status name changed in task list
        
    def add_a_task(self, task_name_type: bool):
        if task_name_type == True:
            task = self.faker.word()
        else:
            task = ""
        self.test_task_name = task
        task_row = self.page.locator(self.phase_list).first
        task_row.page.get_by_role("button", name="plus Add Task").first.click()
        self.page.get_by_placeholder("Type task name and press").fill(task)
        self.page.get_by_placeholder("Type task name and press").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify task added in task list
        if task_name_type == False:
            assert self.page.get_by_placeholder("Type task name and press") .is_visible(), "Add a task with empty name failed"
        else:
            assert any(task in name for name in self.task_names()), "Add a task with empty name failed"

        

    def add_subtask(self):
        self.subtask = self.faker.word()
        task_name = self.test_task_name
        status_phases = self.page.locator(self.phase_list).all()
        for status_phase in status_phases:
            task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                main_task = task_row.locator(".border-r > div > div > button").first
                main_task.click()
                self.page.get_by_role("button", name="plus Add Sub Task").click()
                self.page.get_by_placeholder("Type subtask name and press").fill(self.subtask)
                self.page.get_by_placeholder("Type subtask name and press").press("Enter")
                self.page.wait_for_timeout(2000)
                break

        #verify task added in task list
        subtasks = []
        subtask_list = main_task.page.locator(".bg-gray-50 span.text-gray-700.text-sm").all()
        for subtask_item in subtask_list:
            name = subtask_item.inner_text().strip()
            subtasks.append(name)

        assert any(self.subtask in name for name in subtasks), "Add subtask failed"

    def edit_task_name(self):
        new_task_name = self.faker.word()
        task_name = random.choice(self.task_names())
        self.page.locator(self.phase_list).first
        self.page.get_by_text(task_name).click()
        self.page.get_by_role("textbox").fill(new_task_name)
        self.page.get_by_role("textbox").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify task added in task list
        assert any(new_task_name in name for name in self.task_names()), "Edit task name failed"

    def assign_members_for_task(self):
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Assignees", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.locator("button").first.click()
            members_dropdown = self.page.locator("div.fixed")
            member = members_dropdown.locator("div.p-2.flex").first
            member.click()
            task_name_locator.locator("button").first.click()
            self.page.wait_for_timeout(2000)

            # Verify assigned members
            task_name_locator.locator("button").first.click()
            members_dropdown = self.page.locator("div.fixed")
            checkbox_class = member.locator("div.w-4").get_attribute("class") or ""
            assert "bg-blue-500 border-blue-500" in checkbox_class, "Assign members for task failed"
        else:
            assert False, "Assign members for task failed - Task not found"

    def invite_a_new_member_by_email(self):
        email = self.faker.email()
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Assignees", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.locator("button").first.click()
            self.page.get_by_role("button", name="user-add Invite member").click()
            self.page.wait_for_timeout(1000)
            self.page.locator(".ant-select-selection-overflow").click()
            self.page.get_by_label("Invite with email").fill(email)
            self.page.get_by_role("button", name="Invite", exact=True).click()

            #verify invitation sent
            self.page.wait_for_timeout(1000)
            message = self.page.locator("//*[@class='ant-message-custom-content ant-message-success']").inner_text().strip()
            assert "project member(s) invited successfully" in message, "Invite a new member by email failed"
            self.page.wait_for_timeout(2000)
        
        else:
            assert False, "Invite a new member by email failed - Task not found"

    def invite_a_new_member_by_invalid_email(self):
        email = "test@.com"
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Assignees", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.locator("button").first.click()
            self.page.get_by_role("button", name="user-add Invite member").click()
            self.page.wait_for_timeout(1000)
            self.page.locator(".ant-select-selection-overflow").click()
            self.page.get_by_label("Invite with email").fill(email)
            self.page.get_by_role("button", name="Invite", exact=True).click()

            #verify invitation sent
            self.page.wait_for_timeout(1000)
            assert self.page.get_by_text("Please enter valid email").is_visible(), "Invite a new member by invalid email failed"

        
        else:
            assert False, "Invite a new member by invalid email failed - Task not found"

    def add_label_for_the_task(self):
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Labels", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.locator("button").first.click()
            labels_dropdown = self.page.locator("div.fixed")
            label = labels_dropdown.locator("div.px-2.gap-2").first
            label_text = label.locator("div.font-medium").inner_text().strip()
            self.page.get_by_placeholder("Search labels...").click()
            self.page.get_by_placeholder("Search labels...").fill(label_text)
            label.click()
            task_name_locator.locator("button").first.click()
            self.page.wait_for_timeout(2000)

            # Verify assigned members
            task_name_locator.locator("button").first.click()
            labels_dropdown = self.page.locator("div.fixed")
            checkbox_class = label.locator("div.w-4").get_attribute("class") or ""
            assert "bg-blue-500 border-blue-500" in checkbox_class, "Add label for task failed"
        
        else:
            assert False, "Add label for task failed - Task not found"

    def create_new_label(self):
        task_name = self.test_task_name
        new_label = self.faker.word()
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Labels", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.locator("button").first.click()
            labels_dropdown = self.page.locator("div.fixed")
            label = labels_dropdown.locator("div.px-2.gap-2").first
            self.page.get_by_placeholder("Search labels...").click()
            self.page.get_by_placeholder("Search labels...").fill(new_label)
            self.page.get_by_role("button", name="Create \"reality\"").click()
            task_name_locator.locator("button").first.click()
            self.page.wait_for_timeout(2000)

            # Verify label
            task_name_locator.locator("button").first.click()
            labels_dropdown = self.page.locator("div.fixed")
            checkbox_class = label.locator("div.w-4").get_attribute("class") or ""
            assert "bg-blue-500 border-blue-500" in checkbox_class, "Add label for task failed"

        else:
            assert False, "Add label for task failed - Task not found"

    def add_phase_to_task(self):
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Phase", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.locator("button").first.click()
            phase_dropdown = self.page.locator("div.fixed")
            phase_select_item = phase_dropdown.locator("span").nth(2)
            phase = phase_select_item.inner_text().strip() or ""
            phase_select_item.click()
            self.page.wait_for_timeout(2000)

            # Verify phase added
            phase_button = task_name_locator.locator("button").first.inner_text().strip()
            assert phase == phase_button, "Add phase for task failed"
        
        else:
            assert False, "Add phase for task failed - Task not found"
        
    def change_status(self, status):
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list).all()
        for phase in phases:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                # column_selector = self.get_column_selector_by_text("Status", start_index=1)
                task_name_locator = task_row.locator("[data-column-id='status'] button")
                if task_name_locator.is_visible():
                    # task_name_locator.locator("button").first.click()
                    task_name_locator.click()
                    status_dropdown = self.page.locator("div.fixed")
                    status_select_item = status_dropdown.locator("span", has_text=status)
                    status_select_item.click()
                    self.page.wait_for_timeout(2000)

                    # Verify status changed
                    status_phase = self.page.locator(self.phase_list, has_text=status).first
                    new_task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
                    # column_selector = self.get_column_selector_by_text("Status", start_index=1)
                    new_task_name_locator = new_task_row.locator("[data-column-id='status'] button")
                    # status_button = new_task_name_locator.locator("button").first.inner_text().strip()
                    status_button = new_task_name_locator.inner_text().strip()
                    break
        assert status == status_button, "Change status for task failed"

    def change_priority(self):
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list).all()
        for phase in phases:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                # column_selector = self.get_column_selector_by_text("Priority", start_index=1)
                task_name_locator = task_row.locator("[data-column-id='priority'] button")
                if task_name_locator.is_visible():
                    # task_name_locator.locator("button").first.click()
                    task_name_locator.click()
                    priority_dropdown = self.page.locator("div.fixed")
                    priority_select_item = priority_dropdown.locator("span").nth(1)
                    priority = priority_select_item.inner_text().strip() or ""
                    priority_select_item.click()
                    self.page.wait_for_timeout(2000)

                    # Verify priority changed
                    # priority_button = task_name_locator.locator("button").first.inner_text().strip()
                    priority_button = task_name_locator.inner_text().strip()
                    assert priority == priority_button, "Change priority for task failed"

                else:
                    assert False, "Change priority for task failed - Task not found"
                break

    def add_time_track(self):
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Time Tracking", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            start_time = task_name_locator.inner_text().strip() or ""
            task_name_locator.locator("button").first.click()
            self.page.wait_for_timeout(2000)

            # Verify time track
            current_time = task_name_locator.inner_text().strip() or ""
            task_name_locator.locator("button").first.click()
            assert start_time != current_time, "Time track for task failed"

        else:
            assert False, "Time track for task failed - Task not found"

    def set_start_date(self):
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Start Date", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            start_date = task_name_locator.inner_text().strip() or ""
            task_name_locator.click()
            self.page.locator(".ant-picker-dropdown .ant-picker-now-btn").click()
            self.page.wait_for_timeout(2000)

            # Verify start date
            selected_start_date = task_name_locator.inner_text().strip() or ""
            assert start_date != selected_start_date, "Set start date for task failed"

        else:
            assert False, "Set start date for task failed - Task not found"

    def set_due_date(self):
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list).all()
        for phase in phases:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                # column_selector = self.get_column_selector_by_text("Due Date", start_index=1)
                task_name_locator = task_row.locator("[data-column-id='dueDate'] div.cursor-pointer")
                if task_name_locator.is_visible():
                    due_date = task_name_locator.inner_text().strip() or ""
                    task_name_locator.click()
                    self.page.locator(".ant-picker-dropdown .ant-picker-now-btn").click()
                    self.page.wait_for_timeout(2000)

                    # Verify due date
                    selected_due_date = task_name_locator.inner_text().strip() or ""
                    break
        assert due_date != selected_due_date, "Set due date for task failed"

    def show_time_track_logs(self):
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first

        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Time Tracking", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        if task_name_locator.is_visible():
            task_name_locator.first.click()
            self.page.wait_for_timeout(2000)

            # Verify time track logs
            logs_locator = self.page.locator("div.ant-flex-wrap-wrap").all()
            assert len(logs_locator) > 0, "display time tracking details for task failed"

        else:
            assert False, "display time tracking details for task failed - Task not found"

    def view_context_menu(self):
        task = self.page.locator(".border-r > div > div").first
        task.click(button="right")

        # Verify context menu
        context_menu = self.page.locator("div.fixed")
        assert context_menu.is_visible(), "View context menu for a task failed"

    def right_click_on_task(self):
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list).all()
        for phase in phases:
            task_row = phase.locator(".border-r > div > div", has_text=task_name).first
            if task_row.is_visible():
                task_row.click(button="right")

                # Verify context menu
                context_menu = self.page.locator("div.fixed")
                assert context_menu.is_visible(), "View context menu for a task failed"
                break
        assert context_menu.is_visible(), "View context menu for a task failed"

    def click_on_context_menu(self, menu_option: str):
        self.page.get_by_role("button", name = menu_option).click()

        if menu_option == "Move to":
            #if Move to, select Doing
            self.page.locator(".absolute > li:nth-child(2) > .flex.items-center.gap-2.px-4").click()

        self.page.wait_for_timeout(2000)

    def verify_assign(self):
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list).all()
        for phase in phases:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                # column_selector = self.get_column_selector_by_text("Assignees", start_index=1)
                task_name_locator = task_row.locator("button.rounded-full.w-5")
                if task_name_locator.is_visible():
                    # task_name_locator.locator("button").first.click()
                    task_name_locator.click()
                    members_dropdown = self.page.locator("div.fixed")
                    member = members_dropdown.locator("div.p-2.flex").first
                    checkbox_class = member.locator("div.w-4").get_attribute("class") or ""
                    assert "bg-blue-500 border-blue-500" in checkbox_class, "assign to me failed"
                    status = True
                else:
                    status = False
                    assert False, "assign to me failed - Task not found"
                break
        assert status, "assign to me failed"

    def verify_move_to_from_context_menu(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.phase_list, has_text="Doing").first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        assert task_row.is_visible(), "Move to from context menu failed"

    def verify_archived(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.phase_list).first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        assert not task_row.is_visible(), "Archive task from context menu failed"

        # check in archived tasks
        self.mark_show_archived(True)
        status_phase = self.page.locator(self.phase_list).first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        assert task_row.is_visible(), "Archive task from context menu failed"

    def covert_to_subtask_from_context_menu(self):
        assert self.page.locator("div.ant-drawer-header", has_text= "Convert to Sub task").is_visible(), "Convert to subtask from context menu failed"
        self.page.get_by_role("button",name = "right To Do").click()
        main_task = self.page.locator(".ant-drawer-body div:nth-of-type(2) td.ant-table-cell:nth-of-type(2)").first
        main_task.click()
        self.page.wait_for_timeout(1000)  

    def verify_coverted_to_subtask_from_context_menu(self):
        task_name = self.test_task_name
        main_task = self.page.locator(".border-r > div > div > button").first
        main_task.click()
        subtask_list = main_task.page.locator(".bg-gray-50 span.text-gray-700.text-sm", has_text=task_name)
        assert subtask_list.is_visible(), "Convert task to subtask from context menu failed"

    def verify_deleted_task(self, message):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.phase_list).first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        assert not task_row.is_visible(), message
        return True

    def view_bulk_action_menu(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.phase_list).all()
        for phase in status_phase:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                task_row.locator(".border-r input").first.click()
                bulk_actions_menu = self.page.locator("div").filter(has_text="task selected")
                bulk_actions_menu.wait_for(state="visible")
                break
        assert bulk_actions_menu.is_visible(), "Bulk Actions menu not visible on checkbox click"

    def view_bulk_action_menu_by_checking_multiple(self):
        task_names = self.random_task_names
        status_phase = self.page.locator(self.phase_list).all()
        for phase in status_phase:
            for task_name in task_names:
                task_row = phase.locator("div.border-b.flex", has_text=task_name)
                if task_row.is_visible():
                    task_row.locator(".border-r input").first.click()
            break

        bulk_actions_menu = self.page.locator("div").filter(has_text="task selected")
        bulk_actions_menu.wait_for(state="visible")
        assert bulk_actions_menu.is_visible(), "Bulk Actions menu not visible on checkbox click"
    
    def change_status_in_multiple_via_bulk_action(self, status: str):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-retweet path").click()
        self.page.locator("span.ant-badge-status-text", has_text=status).click()
        self.page.wait_for_timeout(2000)

        # Verify status changed
        task_names = self.random_task_names
        for task_name in task_names:
            phase = self.page.locator(self.phase_list, has_text=status).first
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            assert task_row.is_visible(), "Change status from bulk action menu failed"

    def change_status_via_bulk_action(self, status: str):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-retweet path").click()
        self.page.locator("span.ant-badge-status-text", has_text=status).click()
        self.page.wait_for_timeout(2000)

        # Verify status changed
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list, has_text=status).first
        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        assert task_row.is_visible(), "Change status from bulk action menu failed"
        
    def change_priority_via_bulk_action(self, priority: str): 
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".ant-btn-icon .anticon-flag path").click()
        self.page.locator("span.ant-badge-status-text", has_text=priority).click()
        self.page.wait_for_timeout(2000)

        # Verify priority changed
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list, has_text=priority).all()
        for phase in phases:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                assert task_row.is_visible(), "Change priority from bulk action menu failed"
                break
        assert task_row.is_visible(), "Change priority from bulk action menu failed"

    def change_phase_via_bulk_action(self, phase: str): 
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-bulb path").click()
        self.page.locator("span.ant-badge-status-text", has_text=phase).click()
        self.page.wait_for_timeout(2000)

        # Verify phase changed
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list, has_text=phase).all()
        for p in phases:
            task_row = p.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                assert task_row.is_visible(), "Change phase from bulk action menu failed"
                break

    def change_label_in_bulk_action(self):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-tags path").click()
        labels_dropdown = self.page.locator("div.ant-card-body")
        label = labels_dropdown.locator("li.ant-list-item").first
        label_texts = label.inner_text().strip()
        label.click()
        self.page.get_by_role("button", name="Apply").click()
        self.page.wait_for_timeout(2000)

        # Verify label changed
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first
        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Labels", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        task_name_locator.locator("button").first.click()
        labels_dropdown = self.page.locator("div.fixed")
        label = labels_dropdown.locator("div.px-2.gap-2").all()
        for l in label:
            label_text = l.locator("div.font-medium").inner_text().strip()
            if label_texts == label_text:
                assert True, "change label from bulk action menu failed"
                break
        else:
            assert False, "change label from bulk action menu failed"
    
    def create_label_in_bulk_action(self):
        new_label = self.faker.word()
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-tags path").click()
        labels_dropdown = self.page.locator("div.ant-card-body")
        label = labels_dropdown.locator("li.ant-list-item").first
        self.page.get_by_placeholder("Search or create label...").click()
        self.page.get_by_placeholder("Search or create label...").fill(new_label)
        self.page.get_by_role("button", name="Apply").click()
        self.page.wait_for_timeout(2000)

        # Verify label changed
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first
        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        column_selector = self.get_column_selector_by_text("Labels", start_index=1)
        task_name_locator = task_row.locator(column_selector)
        task_name_locator.locator("button").first.click()
        labels_dropdown = self.page.locator("div.fixed")
        label = labels_dropdown.locator("div.px-2.gap-2").all()
        for l in label:
            label_text = l.locator("div.font-medium").inner_text().strip()
            if new_label == label_text:
                assert True, "create label from bulk action menu failed"
                break
        else:
            assert False, "create label from bulk action menu failed"

    def assign_task_to_me_in_bulk_action(self):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-user-add path").click()
        self.page.wait_for_timeout(3000)

    def assign_task_to_members_in_bulk_action(self):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".ant-btn-text .anticon-usergroup-add path").click()
        members_dropdown = self.page.locator("div.ant-card-body")
        member = members_dropdown.locator("li.ant-list-item").first
        member.click()
        self.page.get_by_role("button", name="Apply").click()
        self.page.wait_for_timeout(3000)

    def archive_task_in_bulk_action(self):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-inbox path").click()
        self.page.wait_for_timeout(3000)

    def delete_task_in_bulk_action(self):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-delete path").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("button", has_text="Delete").click()
        self.page.wait_for_timeout(3000)

    def create_task_templates_in_bulk_action(self):
        self.template_name = self.faker.word()
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-more svg").click()
        self.page.get_by_text("Create Task Template").click()
        self.page.wait_for_timeout(3000)

        template_card = self.page.locator("div.ant-drawer-header", has_text="Create Task Template")
        assert template_card.is_visible(), "Create task template from bulk action menu failed"

        self.page.get_by_role("textbox", name="* Template Name :").fill(self.template_name)
        self.page.locator("button", has_text="Save").click()
        self.page.wait_for_timeout(3000)

    def verify_import_task(self):
        template_name = self.template_name
        self.page.locator("button.profile-button").click()
        self.page.locator(".ant-card-body a", has_text="Settings").click()
        self.page.wait_for_timeout(3000)
        self.page.locator(".ant-flex-align-center .ant-flex a", has_text="Task Templates").click()
        self.page.wait_for_timeout(3000)
        assert self.page.locator("td:nth-of-type(1)", has_text = template_name).is_visible(), "Create task template from bulk action menu failed"

    def cancel_task_templates_in_bulk_action(self):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-more svg").click()
        self.page.get_by_text("Create Task Template").click()
        self.page.wait_for_timeout(3000)

        template_card = self.page.locator("div.ant-drawer-header", has_text="Create Task Template")
        assert template_card.is_visible(), "cancel create task template from bulk action menu failed"

        self.page.locator("button", has_text="Cancel").click()
        self.page.wait_for_timeout(3000)
        assert not template_card.is_visible(), "Cancel create task template from bulk action menu failed"

    def deselect_task(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.phase_list).first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        task_row.locator(".border-r input").first.click()
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        assert not bulk_actions_menu.is_visible(), "deselect task from bulk action menu failed"

    def open_task_drawer(self):
        task_name = self.test_task_name
        status_phases = self.page.locator(self.phase_list).all()
        for status_phase in status_phases:
            task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
            task_row.scroll_into_view_if_needed()
            if task_row.is_visible():
                task_column = task_row.locator("//*[@data-column-id='title']")
                task_column.hover()
                task_column.locator("button",has_text="Open").first.click()
                self.page.wait_for_timeout(2000)
                break
        assert self.page.locator("div.ant-drawer-header", has_text=task_name).is_visible(), "Open task drawer failed"

    def open_sub_task_drawer(self):
        sub_task_name = self.subtask
        task_name = self.test_task_name
        self.page.locator(".anticon-sync path").click()
        self.page.wait_for_timeout(3000)
        status_phases = self.page.locator(self.phase_list).all()
        for status_phase in status_phases:
            task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                main_task = task_row.locator(".border-r > div > div > button").first
                main_task.click()
                task_column = self.page.locator("div.justify-between",has_text=sub_task_name)
                task_column.hover()
                task_column.locator("button",has_text="Open").first.click()
                self.page.wait_for_timeout(2000)
                break
        assert self.page.locator("div.ant-drawer-header", has_text=sub_task_name).is_visible(), "Open sub task drawer failed"

    def assign_task_to_members_in_drawer(self):
        self.page.locator(".ant-flex-align-center .ant-btn-circle span.anticon-plus").click()
        self.page.locator("li.ant-list-item").first.click()
        self.page.wait_for_timeout(2000)
        assert self.page.locator(".ant-checkbox-wrapper.ant-checkbox-wrapper-checked").is_visible(), "Assign task to members in drawer failed"
        self.page.locator(".ant-flex-align-center .ant-btn-circle span.anticon-plus").click()

    def create_subtask_in_drawer(self):
        self.sub_task = self.faker.word()
        self.page.locator("input[value='Add Sub Task']").click()
        self.page.get_by_role("textbox", name="Type your task and hit enter").fill(self.sub_task)
        self.page.get_by_role("textbox", name="Type your task and hit enter").press('Enter')
        self.page.wait_for_timeout(1000)

    def verify_task_drawer_ui_elements(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()

        drawer_header = "div.ant-collapse-header"

        assert self.page.locator(drawer_header, has_text="Details").is_visible(), "Task drawer UI elements details not visible"
        assert self.page.locator(drawer_header, has_text="Description").is_visible(), "Task drawer UI elements description not visible"
        assert self.page.locator(drawer_header, has_text="Sub Tasks").is_visible(), "Task drawer UI elements sub tasks not visible"
        assert self.page.locator(drawer_header, has_text="Dependencies").is_visible(), "Task drawer UI elements dependencies not visible"
        assert self.page.locator(drawer_header, has_text="Attachments").is_visible(), "Task drawer UI elements attachments not visible"
        assert self.page.locator(drawer_header, has_text="Comments").is_visible(), "Task drawer UI elements comments not visible"

        # tooltips
        # verify assign members
        self.assign_task_to_members_in_drawer()
        assign_members_section = self.page.locator("div#assignees")
        assign_members_section.locator("span.ant-avatar").first.hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div.ant-tooltip-inner").is_visible(), "Task drawer tooltip assigned members not visible"

        #verify subtasks assign members
        self.create_subtask_in_drawer()
        sub_task_row = self.page.locator(".ant-table-row-level-0", has_text=self.sub_task)
        sub_task_row.click()
        self.page.wait_for_timeout(1000)
        self.assign_task_to_members_in_drawer()
        self.page.locator(".ant-drawer-close path").click()
        self.page.wait_for_timeout(2000)
        sub_task_row.locator("span.ant-avatar").first.hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div.ant-tooltip-inner").is_visible(), "Task drawer tooltip assigned members not visible"

        #verify subtask edit icon tooltip
        sub_task_row = self.page.locator(".ant-table-row-level-0", has_text=self.sub_task)
        sub_task_row.hover()
        self.page.locator(".ant-btn-icon .anticon-edit path").hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div.ant-tooltip-inner", has_text="Edit").is_visible(), "Task drawer tooltip subtask edit icon tooltip not visible"

        #verify subtask delete icon tooltip
        sub_task_row = self.page.locator(".ant-table-row-level-0", has_text=self.sub_task)
        sub_task_row.hover()
        self.page.locator(".anticon-delete path").hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div.ant-tooltip-inner", has_text="Delete").is_visible(), "Task drawer tooltip subtask delete icon tooltip not visible"

        #verify subtask member icon tooltip
        sub_task_row = self.page.locator(".ant-table-row-level-0", has_text=self.sub_task)
        sub_task_row.locator("span.ant-avatar").hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div:nth-of-type(3) div.ant-tooltip-inner").is_visible(), "Task drawer tooltip subtask member icon tooltip not visible"

        #verify created date tooltip
        sub_task_row = self.page.locator("span.ant-typography-secondary", has_text="Created")
        sub_task_row.hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div:nth-of-type(n) div.ant-tooltip-inner", has_text="Created").is_visible(), "Task drawer tooltip created date tooltip not visible"

        #verify updated date tooltip
        sub_task_row = self.page.locator("span.ant-typography-secondary", has_text="Updated")
        sub_task_row.hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div:nth-of-type(n) div.ant-tooltip-inner", has_text="Updated").is_visible(), "Task drawer tooltip updated date tooltip not visible"

    def change_task_name_via_task_drawer(self, task_name: bool):
        if task_name:
            new_task_name = self.faker.word()
        else:
            new_task_name = ""
        self.page.locator("p.task-name-display").click()
        self.page.get_by_role("textbox", name = "Type your Task").fill(new_task_name)
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.wait_for_timeout(2000)

        # Verify task name changed
        if task_name:
            drawer_title = self.page.locator("p.task-name-display").inner_text().strip()
            assert new_task_name == drawer_title, "Change task name via task drawer failed"
        else:
            self.page.locator(".ant-drawer-close path").click()
            self.page.wait_for_timeout(2000)
            task_name = self.test_task_name
            status_phase = self.page.locator(self.phase_list).first
            task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
            assert task_row.is_visible(), "Change task name via task drawer with empty name failed"

    def change_task_status_via_task_drawer(self):
        self.page.locator(".ant-select-borderless div").click()
        self.page.locator("div.ant-select-item-option",has_text="Doing").click()
        self.page.wait_for_timeout(2000)

        # Verify task status changed
        status = self.page.locator(".ant-select-borderless div").inner_text().strip()
        assert status == "Doing", "Change task status via task drawer failed"

    def delete_task_via_task_drawer(self):
        self.page.locator(".ant-drawer-title button.ant-dropdown-trigger").click()
        self.page.get_by_text("Delete Task").click()
        self.page.wait_for_timeout(2000)

        # Verify task deleted
        assert self.verify_deleted_task(), "Delete task via task drawer failed"

    def add_phase_to_the_task_via_task_drawer(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        phase_dropdown = self.page.locator("input#phase")
        phase_dropdown.click()
        self.page.locator("div.ant-select-item-option",has_text="Backlog").click()
        self.page.wait_for_timeout(2000)

        # Verify phase added
        phase = self.page.locator(".ant-select-status-success span.ant-select-selection-item").inner_text().strip()
        assert phase == "Backlog", "Add phase to the task via task drawer failed"

    def verify_assigned_members_in_task_drawer(self):
        assign_members_section = self.page.locator("div#assignees")
        assign_members_section.locator("span.ant-avatar").first.hover()
        self.page.wait_for_timeout(1000)
        assert self.page.locator("div.ant-tooltip-inner").is_visible(), "Verify assigned members in task drawer failed"

    def search_members_in_assign_members_section_in_drawer(self):
        self.page.locator(".ant-flex-align-center .ant-btn-circle span.anticon-plus").click()
        self.page.get_by_placeholder("Search or create").click()
        self.page.get_by_placeholder("Search or create").fill("worklenz")
        self.page.locator("li.ant-list-item").first.click()
        self.page.wait_for_timeout(2000)
        assert self.page.locator(".ant-checkbox-wrapper.ant-checkbox-wrapper-checked").is_visible(), "Assign task to members in drawer failed"
        self.page.locator(".ant-flex-align-center .ant-btn-circle span.anticon-plus").click()

    def add_due_date_in_drawer(self):
        due_date_section = self.page.locator(".ant-picker-input input").first
        due_date = due_date_section.input_value().strip() or ""
        due_date_section.click()
        self.page.locator(".ant-picker-dropdown .ant-picker-now-btn").click()

        # Verify due date
        selected_due_date = due_date_section.input_value().strip() or ""
        assert due_date != selected_due_date, "Set due date in task drawer failed"

    def add_start_date_in_drawer(self):
        self.page.locator("#dueDate .ant-btn span", has_text="Show Start Date").click()
        start_date_section = self.page.locator(".ant-picker-input input").first
        start_date = start_date_section.input_value().strip() or ""
        start_date_section.click()
        self.page.locator(".ant-picker-dropdown .ant-picker-now-btn").click()

        # Verify start date
        selected_due_date = start_date_section.input_value().strip() or ""
        assert start_date != selected_due_date, "Set due date in task drawer failed"

    def add_estimated_time_in_drawer(self):
        hours = self.faker.random_int(min=1, max=5)
        minutes = self.faker.random_int(min=10, max=59)
        hours_section = self.page.locator("input#hours")
        minuet_section = self.page.locator("input#minutes")
        hours_section.click()
        hours_section.fill(str(hours))
        minuet_section.click()
        minuet_section.fill(str(minutes))
        self.page.locator(".ant-drawer-close path").click()
        self.page.wait_for_timeout(2000)

        # Verify estimated date
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first
        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        task_name_locator = task_row.locator("[data-column-id='estimation'] div")
        if task_name_locator.is_visible():
            label_text = task_name_locator.inner_text().strip() or ""
            expected_text = f"{hours}h {minutes}m"
            pass

        assert label_text == expected_text, "Set estimated time in task drawer failed"

    def check_estimated_time_minutes_max_in_drawer(self):
        minutes = "60"
        minuet_section = self.page.locator("input#minutes")
        minuet_section.click()
        minuet_section.fill(str(minutes))
        spinner = self.page.locator(".ant-input-number-handler-up-disabled path")
        assert spinner.is_visible(), "Check estimated time minutes max in task drawer failed"

    def change_priority_via_task_drawer(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        priority_dropdown = self.page.locator(".ant-select-selection-item div")
        priority_dropdown.click()
        self.page.locator("div.ant-select-item-option",has_text="High").click()
        self.page.wait_for_timeout(2000)

        # Verify phase added
        priority = priority_dropdown.inner_text().strip()
        assert priority == "High", "Change priority via task drawer failed"

    def change_label_via_task_drawer(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator(".ant-flex-wrap-wrap button").click()
        labels_dropdown = self.page.locator("div.ant-card-body")
        label = labels_dropdown.locator("li.ant-list-item").first
        label_texts = label.inner_text().strip()
        label.click()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.wait_for_timeout(2000)

        # Verify label changed
        self.page.locator(".ant-flex-wrap-wrap button").click()
        labels_dropdown = self.page.locator("div.ant-card-body")
        label = labels_dropdown.locator("li.ant-list-item").all()
        for l in label:
            label_text = l.inner_text().strip()
            if label_texts == label_text:
                assert True, "change label from task drawer failed"
                break
        else:
            assert False, "change label from task drawer failed"
    
    def create_label_via_task_drawer(self):
        new_label = self.faker.word()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator(".ant-flex-wrap-wrap button").click()
        labels_dropdown = self.page.locator("div.ant-card-body")
        label = labels_dropdown.locator("li.ant-list-item").first
        self.page.get_by_placeholder("Search or create").click()
        self.page.get_by_placeholder("Search or create").fill(new_label)
        self.page.get_by_placeholder("Search or create").press("Enter")
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.wait_for_timeout(2000)

        # Verify label changed
        self.page.locator(".ant-flex-wrap-wrap button").click()
        labels_dropdown = self.page.locator("div.ant-card-body")
        label = labels_dropdown.locator("li.ant-list-item").all()
        for l in label:
            label_text = l.inner_text().strip()
            if new_label == label_text:
                assert True, "create label from task drawer failed"
                break
        else:
            assert False, "create label from task drawer failed"

    def billable_toggle_via_task_drawer(self, is_billable: bool):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        toggle = self.page.locator(".ant-form-item-has-success span.ant-switch-inner")
        switch = self.page.locator(".ant-switch-checked div")
        if is_billable:
            toggle.click()
            toggle.click()
            assert switch.is_visible(), "Billable toggle enable via task drawer failed"
        else:
            toggle.click()
            assert not switch.is_visible(), "Billable toggle disable via task drawer failed"

    def notify_members_via_task_drawer(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator('div:nth-child(11) > .ant-row > .ant-col.ant-col-18 > .ant-form-item-control-input > .ant-form-item-control-input-content > .ant-flex > .ant-btn').click()
        self.page.locator("li.ant-list-item").first.click()
        self.page.wait_for_timeout(2000)
        self.page.locator('div:nth-child(11) > .ant-row > .ant-col.ant-col-18 > .ant-form-item-control-input > .ant-form-item-control-input-content > .ant-flex > .ant-btn').click()

        #verify member notified
        self.page.locator('div:nth-child(11) > .ant-row > .ant-col.ant-col-18 > .ant-form-item-control-input > .ant-form-item-control-input-content > .ant-flex > .ant-btn').click()
        assert self.page.locator(".ant-checkbox-wrapper.ant-checkbox-wrapper-checked").is_visible(), "Assign task to members in drawer failed"

    def add_description_via_task_drawer(self):
        description = self.faker.paragraph()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")
        self.page.frame_locator("iframe[title=\"Rich Text Area\"]").get_by_label("Rich Text Area").fill(description)
        self.page.locator(".ant-drawer-close svg").click()
        self.page.wait_for_timeout(2000)

        #verify description
        task_name = self.test_task_name
        phase = self.page.locator(self.phase_list).first
        task_row = phase.locator("div.border-b.flex", has_text=task_name)
        task_description = task_row.locator("p").inner_text().strip()
        assert task_description == description,"Add description in task drawer failed"

        task_column = task_row.locator("div.justify-between")
        task_column.hover()
        task_column.locator("button",has_text="Open").first.click()
        self.page.wait_for_timeout(2000)
        drawer_description = self.page.locator(".description-content p").inner_text().strip()
        assert drawer_description == description,"Add description in task drawer failed"

    def add_bold_and_italic_text_to_description_via_task_drawer(self):
        description = self.faker.paragraph()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")
        editor = self.page.frame_locator("iframe[title=\"Rich Text Area\"]").get_by_label("Rich Text Area")

        #Bold text
        self.page.get_by_label("Bold").click()
        editor.click()
        editor.type(description)
        self.page.get_by_label("Bold").click()
        editor.press("Enter")

        #Italic text
        self.page.get_by_label("Italic").click()
        editor.type(description)
        self.page.get_by_label("Italic").click()
        self.page.locator("div.ant-collapse-item:nth-of-type(3) div.ant-collapse-header").click()
        self.page.wait_for_timeout(2000)

        #verify bold and italic description
        bold_para = self.page.locator(".description-content p").nth(0)
        italic_para = self.page.locator(".description-content p").nth(1)

        # Bold verification
        assert bold_para.locator(":is(strong, b)").is_visible(),"Bold description failed"

        # Italic verification
        assert(italic_para.locator(":is(em, i)")).is_visible(),"Italic description failed"

    def add_bullet_points_to_description_via_task_drawer(self):
        description = self.faker.paragraph()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")
        editor = self.page.frame_locator("iframe[title=\"Rich Text Area\"]").get_by_label("Rich Text Area")

        #Bullet text
        self.page.get_by_label("Bullet list").click()
        editor.click()
        editor.type(description)
        self.page.locator("div.ant-collapse-item:nth-of-type(3) div.ant-collapse-header").click()
        self.page.wait_for_timeout(2000)

        #verify bullet description
        bullet_para = self.page.locator(".description-content li").first
        assert bullet_para.is_visible(),"Bullet description faild"
    
    def add_numbered_list_to_description_via_task_drawer(self):
        description = self.faker.paragraph()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")
        editor = self.page.frame_locator("iframe[title=\"Rich Text Area\"]").get_by_label("Rich Text Area")

        #Numbered text
        self.page.get_by_label("Numbered list").click()
        editor.click()
        editor.type(description)
        self.page.locator("div.ant-collapse-item:nth-of-type(3) div.ant-collapse-header").click()
        self.page.wait_for_timeout(2000)

        #verify numbered description
        numbered_para = self.page.locator(".description-content ol li").nth(0)
        assert numbered_para.is_visible(),"Numbered list description faild"

    def change_text_alignment_to_description_via_task_drawer(self):
        description = self.faker.paragraph()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")
        editor = self.page.frame_locator("iframe[title=\"Rich Text Area\"]").get_by_label("Rich Text Area")

        #Numbered text
        self.page.get_by_label("Numbered list").click()
        editor.click()
        editor.type(description)
        self.page.locator("div.ant-collapse-item:nth-of-type(3) div.ant-collapse-header").click()
        self.page.wait_for_timeout(2000)

        #verify numbered description
        numbered_para = self.page.locator(".description-content ol li").nth(0)
        assert numbered_para.is_visible(),"Numbered list description failed"

    def add_hyperlink_to_description_via_task_drawer(self):
        hyperlink = "https://react.worklenz.com/"
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")

        #Hyperlink
        self.page.get_by_label("Insert/edit link").click()
        self.page.get_by_label("URL").click()
        self.page.get_by_label("URL").fill(hyperlink)
        self.page.get_by_label("Title").fill("worklenz")
        self.page.locator("button[data-mce-name='Save']").click()
        self.page.locator("div.ant-collapse-item:nth-of-type(3) div.ant-collapse-header").click()
        self.page.wait_for_timeout(2000)

        #verify hyperlink description
        numbered_para = self.page.locator(".description-content a").first
        assert numbered_para.is_visible(),"Hyperlink description failed"

    def change_text_type_to_description_via_task_drawer(self):
        description = self.faker.paragraph()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Click to add description\.\.\.$")).nth(3).click()
        self.page.wait_for_timeout(5000)
        self.wait_for_element("div.tox-statusbar")
        editor = self.page.frame_locator("iframe[title=\"Rich Text Area\"]").get_by_label("Rich Text Area")

        #Change_text type
        self.page.get_by_label("Block Paragraph").click()
        self.page.get_by_role("heading", name="Heading 1").click()
        editor.click()
        editor.type(description)
        self.page.locator("div.ant-collapse-item:nth-of-type(3) div.ant-collapse-header").click()
        self.page.wait_for_timeout(2000)

        #verify text type description
        numbered_para = self.page.locator(".description-content h1").first
        assert numbered_para.is_visible(),"Change text type description failed"

    def add_sub_task_via_task_drawer(self, empty:bool):
        if empty:
            subtask = self.faker.word()
        else:
            subtask = ""
        task_name = self.test_task_name
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator("//*[@value = 'Add Sub Task']").click()
        self.page.get_by_placeholder("Type your task and hit enter").fill(subtask)
        self.page.get_by_placeholder("Type your task and hit enter").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify sub task
        if empty == False:
            assert self.page.get_by_placeholder("Type your task and hit enter").is_visible(), "Add empty sub task failed"
        else:
            row_sub_task = self.page.locator("td:nth-of-type(1)").first.inner_text().strip()
            assert row_sub_task == subtask,"Add sub task failed"

            #verify task added in task list
            self.page.locator("button.ant-drawer-close").click()
            self.page.wait_for_timeout(1000)
            phase = self.page.locator(self.phase_list).first
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            main_task = task_row.locator(".border-r > div > div > button")
            main_task.click()
            subtasks = []
            subtask_list = main_task.page.locator(".bg-gray-50 span.text-gray-700.text-sm").all()
            for subtask_item in subtask_list:
                name = subtask_item.inner_text().strip()
                subtasks.append(name)

            assert any(subtask in name for name in subtasks), "Add subtask failed"

    def add_dependency_via_task_drawer(self):
        dependency = self.random_task_name
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.get_by_role("button", name="+ Add new dependency").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='taskName']").click()
        self.page.locator("//*[@id='taskName']").fill(dependency)
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='taskName']").press("Enter")
        self.page.wait_for_timeout(3000)

        #verify dependency
        drawer_dependencies = self.page.locator("span.ant-typography-ellipsis").all()
        for drawer_dependency in drawer_dependencies:
            drawer_dependency = drawer_dependency.inner_text().strip()
            if drawer_dependency == dependency:
                assert True,"Add dependency failed"
                break

    def add_multiple_dependency_via_task_drawer(self):
        dependencies = self.random_task_names
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        for dependency in dependencies:
            self.page.get_by_role("button", name="+ Add new dependency").click()
            self.page.wait_for_timeout(2000)
            self.page.locator("//*[@id='taskName']").click()
            self.page.locator("//*[@id='taskName']").fill(dependency)
            self.page.wait_for_timeout(2000)
            self.page.locator("//*[@id='taskName']").press("Enter")
            self.page.wait_for_timeout(3000)

        #verify dependency
        drawer_dependencies = self.page.locator("span.ant-typography-ellipsis").all()
        values = []
        for drawer_dependency in drawer_dependencies:
            drawer_dependency = drawer_dependency.inner_text().strip()
            values.append(drawer_dependency)
        assert all(dep in values for dep in dependencies),"Add multiple dependency failed"

    def add_attachment_via_task_drawer(self, multiple:bool):
        project_root = Path(__file__).resolve().parents[2]
        files = [
        project_root / "test_data" / "image1.jpeg",
        project_root / "test_data" / "image2.jpeg"
        ]
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        if multiple:
            files_count = len(files)
            self.page.locator("input[type='file']").set_input_files(files)
        else:
            files_count = 1
            self.page.locator("input[type='file']").set_input_files(files[0])
        self.page.wait_for_timeout(3000)

        #verify attachment
        attachment_count = self.page.locator("span.ant-upload-list-item-actions").count()
        assert attachment_count == files_count,"Add attachment failed"

    def add_multiple_attachment_types_via_task_drawer(self):
        project_root = Path(__file__).resolve().parents[2]
        files = [
        project_root / "test_data" / "image1.jpeg",
        project_root / "test_data" / "image2.jpeg",
        project_root / "test_data" / "pdf-test.pdf"
        ]
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        files_count = len(files)
        self.page.locator("input[type='file']").set_input_files(files)
        self.page.wait_for_timeout(3000)

        #verify attachment
        attachment_count = self.page.locator("span.ant-upload-list-item-actions").count()
        assert attachment_count == files_count,"Add attachment failed"

    def tooltips_for_attachments_via_task_drawer(self):
        attachment = self.page.locator("span.ant-upload-list-item-actions").first
        attachment.hover()
        self.page.wait_for_timeout(3000)
        tooltip = self.page.locator("")

        assert tooltip.is_visible(), "Attachments tooltips failed"

    def preview_attachment_via_task_drawer(self):
        attachment = self.page.locator("span.ant-upload-list-item-actions").first
        attachment.hover()
        self.page.wait_for_timeout(1000)
        self.page.locator("div.ant-upload-list-picture-card-container:nth-of-type(1) .anticon-eye path").click()
        self.page.wait_for_timeout(2000)

        preview = self.page.locator("div.preview-container")
        assert preview.is_visible(), "Preview attachments failed"

    def download_attachment_via_task_drawer(self):
        attachment = self.page.locator("span.ant-upload-list-item-actions").first
        attachment.hover()
        # Wait for the download to start
        with self.page.expect_download() as download_info:
            # Click the download button
            self.page.get_by_role("button", name="download").click()
        
        download = download_info.value  # This is a Download object

        # Save to a local path
        download_path = "/tmp/" + download.suggested_filename
        download.save_as(download_path)

        # Verify file exists
        assert Path(download_path).exists(), "Download attachments failed"  

    def delete_attachment_via_task_drawer(self):
        attachment = self.page.locator("span.ant-upload-list-item-actions").first
        attachment.hover()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="delete").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="Yes").click()
        self.page.wait_for_timeout(2000)

        #Verify delete
        preview = self.page.locator("span.ant-upload-list-item-actions")
        assert not preview.is_visible(), "Delete attachments failed"

    def add_comment_via_task_drawer(self, empty:bool):
        if empty:
            comment = self.faker.sentence()
        else:
            comment = ""
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.locator(".custom-mentions-editable").click()
        self.page.locator("#comment div").nth(1).fill(comment)
        if empty == False:
            #Verify comment
            assert self.page.get_by_role("button", name="Comment", exact=True).is_disabled(),"Add empty comment failed"
        else:
            self.page.get_by_role("button", name="Comment", exact=True).click()
            self.page.wait_for_timeout(3000)

            #Verify comment
            comments = self.page.locator("div.ant-comment-inner").first
            thread_comment = comments.locator("div.ant-comment-content-detail").inner_text().strip()
            assert comment == thread_comment, "Add comment failed"

    def add_comment_with_attachment_via_task_drawer(self):
        project_root = Path(__file__).resolve().parents[2]
        files = [
            project_root / "test_data" / "pdf-test.pdf"
        ]
        comment = self.faker.sentence()
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        comment_drawer = self.page.locator(".ant-drawer-footer form")
        self.page.locator(".custom-mentions-editable").click()
        self.page.locator("#comment div").nth(1).fill(comment)
    
        comment_drawer.locator("input[type='file']").set_input_files(files)
        self.page.wait_for_timeout(3000)

        comment_drawer.get_by_role("button", name="Comment", exact=True).click()
        self.page.wait_for_timeout(3000)

        #Verify comment
        comments = self.page.locator("div.ant-comment-inner").first
        attachment = comments.locator(".ant-upload-list div.attachments-grid")
        assert attachment.is_visible(), "Add comment with attachment failed"

    def click_time_logs_tab_via_task_drawer(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Time Log").click()
        self.page.wait_for_timeout(3000)
        assert self.page.locator(".ant-flex-justify-center button").is_visible(), "Time Logs tab open failed"

    def add_time_logs_via_task_drawer(self):
        work_description = self.faker.sentence()
        self.page.get_by_role("button", name="plus Add new time log").click()
        #Date
        self.page.get_by_role("textbox", name="* Date").click()
        self.page.get_by_text("Today").click()
        #Start time
        self.page.get_by_role("textbox", name="* Start Time").click()
        self.page.get_by_text("Now").click()
        #End time
        now = self.page.get_by_role("textbox", name="* Start Time").input_value()
        new_time_value = (datetime.strptime(now, "%H:%M") + timedelta(minutes=30)).strftime("%H:%M")
        self.page.get_by_role("textbox", name="* End Time").fill(new_time_value)
        #Work description
        self.page.get_by_role("textbox", name="Work Description").click()
        self.page.get_by_role("textbox", name="Work Description").fill(work_description)
        self.page.get_by_role("button", name="clock-circle Log time").click()
        self.page.wait_for_timeout(3000)

        #Verify time logs
        logs = self.page.locator(".time-log-item > div > div.ant-flex").first
        start_time = logs.locator(".ant-typography span:nth-of-type(2) strong").inner_text().strip()
        assert start_time == "30m", "Add time log to a task failed"

    def edit_time_log_details_via_task_drawer(self):
        self.page.get_by_role("button", name="plus Add new time log").click()
        self.page.get_by_role("button", name="Edit", exact=True).click()
        #Start time
        self.page.get_by_role("textbox", name="* Start Time").click()
        self.page.get_by_text("Now").click()
        #End time
        now = self.page.get_by_role("textbox", name="* Start Time").input_value()
        new_time_value = (datetime.strptime(now, "%H:%M") + timedelta(minutes=15)).strftime("%H:%M")
        self.page.get_by_role("textbox", name="* End Time").fill(new_time_value)
        self.page.get_by_role("textbox", name="Work Description").click()
        self.page.wait_for_timeout(1000)

        self.page.get_by_role("button", name="clock-circle Update time").click()
        self.page.wait_for_timeout(3000)

        #Verify time logs
        logs = self.page.locator(".time-log-item > div > div.ant-flex").first
        start_time = logs.locator(".ant-typography span:nth-of-type(2) strong").inner_text().strip()

        assert start_time == "15m", "Edit time log details failed"

    def delete_time_log_details_via_task_drawer(self):
        self.page.get_by_role("button", name="plus Add new time log").click()
        self.page.get_by_role("button", name="Delete", exact=True).click()
        self.page.get_by_role("button", name="OK", exact=True).click()
        self.page.wait_for_timeout(3000)

        #Verify time logs
        logs = self.page.locator(".time-log-item > div > div.ant-flex").first
        if logs.is_visible():
            start_time = logs.locator(".ant-typography span:nth-of-type(2) strong").inner_text().strip()
            assert start_time != "30m", "Delete time log details failed"
        else:
            assert True

    def cancel_deletion_of_time_log_details_via_task_drawer(self):
        self.page.get_by_role("button", name="plus Add new time log").click()
        self.page.get_by_role("button", name="Delete", exact=True).click()
        self.page.locator(".ant-popconfirm-buttons button.ant-btn-default").click()
        self.page.wait_for_timeout(1000)

        #Verify time logs
        logs = self.page.locator(".time-log-item > div > div.ant-flex").first
        start_time = logs.locator(".ant-typography span:nth-of-type(2) strong").inner_text().strip()
        assert start_time == "30m", "Cancel Deletion of time log details failed"

    def start_timer_via_task_drawer(self):
        self.page.locator('.ant-flex.css-15i8o2z.ant-flex-align-center.ant-flex-justify-space-between > div > .ant-flex > .ant-btn').click()
        self.page.wait_for_timeout(5000)
        self.page.locator('.ant-flex.css-15i8o2z.ant-flex-align-center.ant-flex-justify-space-between > div > .ant-flex > .ant-btn').click()
        self.page.wait_for_timeout(2000)

        #Verify timer logs
        logs = self.page.locator(".time-log-item > div > div.ant-flex").first
        start_time = logs.locator(".ant-typography span:nth-of-type(2) strong").inner_text().strip()
        assert start_time != "5s", "Timer start failed"

    def export_to_excel_via_task_drawer(self):
        # Wait for the export to start
        with self.page.expect_download() as export_info:
            # Click the export button
            self.page.get_by_role("button", name="download Export to Excel").click()
        
        export = export_info.value  # This is a Download object

        # Save to a local path
        export_path = "/tmp/" + export.suggested_filename
        export.save_as(export_path)

        # Verify file exists
        assert Path(export_path).exists(), "Export to excel failed"

    def click_activity_log_tab_via_task_drawer(self):
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Activity Log").click()
        self.page.wait_for_timeout(3000)
        assert self.page.locator("li.ant-timeline-item").first.is_visible(), "Activity Log tab open failed"

    def change_status_via_task_drawer(self,status):
        status_dropdown = self.page.locator(".ant-select-borderless .ant-select-selection-item span")
        status_dropdown.click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".ant-select-item-option", has_text=status).click()
        self.page.wait_for_timeout(3000)

        status_button = self.page.locator(".ant-select-borderless .ant-select-selection-item span").inner_text().strip()
        assert status_button == status, "Change status via task drawer failed"

    def verify_activities_in_activity_logs_via_task_drawer(self):
        status = False
        phase = False
        priority = False
        assignee = False
        due_date = False
        logs_threads = self.page.locator("li.ant-timeline-item")
        count = logs_threads.count()
        for i in range(count):
            activity = (logs_threads.nth(i).locator(".ant-flex-align-stretch div:nth-of-type(1)").inner_text().strip())      
            if "updated the\nstatus" in activity:
                status = True
            elif "updated the\nphase" in activity:
                phase = True
            elif "updated the\npriority" in activity:
                priority = True
            elif "added an\nassignee" in activity:
                assignee = True
            elif "updated the\nend date" in activity:
                due_date = True
        
        assert any([status, phase, priority, assignee, due_date]),"Verify activities in activity logs via task drawer failed"

    def verify_activities_in_activity_logs_via_bulk_action(self):
        status_count = 0
        phase_count = 0
        priority_count = 0
        assignee_count = 0

        logs_threads = self.page.locator("li.ant-timeline-item")
        count = logs_threads.count()

        for i in range(count):
            activity = (logs_threads.nth(i).locator(".ant-flex-align-stretch div:nth-of-type(1)").inner_text().strip())
            if "updated the\nstatus" in activity:
                status_count += 1
            elif "updated the\nphase" in activity:
                phase_count += 1
            elif "updated the\npriority" in activity:
                priority_count += 1
            elif "added an\nassignee" in activity:
                assignee_count += 1

        #Verify activity logs
        assert (
        status_count == 4 and
        phase_count == 3 and
        priority_count == 3 and
        assignee_count >= 1
    ), "Verify activities in activity logs via bulk action failed"
        
    def verify_activities_in_activity_logs_via_context_menu(self):
        status_count = 0

        logs_threads = self.page.locator("li.ant-timeline-item")
        count = logs_threads.count()

        for i in range(count):
            activity = (logs_threads.nth(i).locator(".ant-flex-align-stretch div:nth-of-type(1)").inner_text().strip())
            if "updated the\nstatus" in activity:
                status_count += 1

        #Verify activity logs
        assert (status_count == 2), "Verify activities in activity logs via context menu failed"

    def verify_activities_in_activity_logs_via_task_table(self):
        status = False
        priority = False
        due_date = False
        logs_threads = self.page.locator("li.ant-timeline-item")
        count = logs_threads.count()
        for i in range(count):
            activity = (logs_threads.nth(i).locator(".ant-flex-align-stretch div:nth-of-type(1)").inner_text().strip())      
            if "updated the\nstatus" in activity:
                status = True
            elif "updated the\npriority" in activity:
                priority = True
            elif "updated the\nend date" in activity:
                due_date = True
        
        assert any([status, priority, due_date]),"Verify activities in activity logs via task table failed"

    def get_random_task_by_phase(self, phase_name):
        status_phase = self.page.locator(self.phase_list, has_text=phase_name).first
        task_rows = status_phase.locator("div.border-b.flex").all()
        for task_row in task_rows:
            dependency_icon = task_row.locator(".anticon.anticon-minus-circle > svg")
            if not dependency_icon.is_visible():
                self.random_task_name = task_row.locator("span.text-gray-700.text-sm").inner_text().strip()
                break

    def get_random_multiple_task_by_phase(self, phase_name):
        status_phase = self.page.locator(self.phase_list, has_text=phase_name).first
        task_rows = status_phase.locator("div.border-b.flex").all()
        self.random_task_names = []
        i = 0
        for task_row in task_rows:
            dependency_icon = task_row.locator(".anticon.anticon-minus-circle > svg")
            if not dependency_icon.is_visible():
                i += 1
                task_name = task_row.locator("span.text-gray-700.text-sm").inner_text().strip()
                self.random_task_names.append(task_name)
                if i == 2:
                    break

    def close_task_drawer(self):
        self.page.locator("button.ant-drawer-close").click()

    def verify_main_task_dependency_in_task_drawer(self, phase_name):
        task_name = self.test_task_name
        self.page.locator(".anticon-sync path").click()
        self.page.wait_for_timeout(3000)

        status_phase = self.page.locator(self.phase_list, has_text=phase_name).first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        if task_row.is_visible():
            task_row.locator(".anticon.anticon-minus-circle > svg").hover()
            self.page.wait_for_timeout(1000)
            tooltip = self.page.get_by_role("tooltip", name="Task has dependencies")
        assert tooltip.is_visible(), "Verify dependency in task drawer failed"

    def verify_sub_task_dependency_in_task_drawer(self, phase_name):
        sub_task_name = self.subtask
        task_name = self.test_task_name
        self.page.locator(".anticon-sync path").click()
        self.page.wait_for_timeout(3000)

        status_phase = self.page.locator(self.phase_list, has_text=phase_name).first
        task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        if task_row.is_visible():
            main_task = task_row.locator(".border-r > div > div > button").first
            main_task.click()
            task_column = self.page.locator("div.justify-between",has_text=sub_task_name)
            task_column.locator(".anticon.anticon-minus-circle > svg").hover()
            self.page.wait_for_timeout(1000)
            tooltip = self.page.get_by_role("tooltip", name="Task has dependencies")
        assert tooltip.is_visible(), "Verify dependency in task drawer failed"

    def delete_dependency_via_task_drawer(self):
        dependency = self.random_task_name
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        dependency_rows = self.page.locator(".ant-table-row-level-0").all()
        for dependency_row in dependency_rows:
            row = dependency_row.locator("span.ant-typography", has_text=dependency)
            if row.is_visible():
                row.hover()
                dependency_row.locator(".anticon-delete path").click()
                self.page.locator(".ant-popconfirm-buttons button.ant-btn-primary").click()
                self.page.wait_for_timeout(3000)
                break
            
        #verify dependency deletion
        for dependency_row in dependency_rows:
            dependency_row = dependency_row.locator("span.ant-typography", has_text=dependency)
            assert not dependency_row.is_visible(), "Delete dependency via task drawer failed"

    def add_same_dependency_via_task_drawer(self):
        dependency = self.random_task_name
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        for i in range(2):
            self.page.get_by_role("button", name="+ Add new dependency").click()
            self.page.wait_for_timeout(2000)
            self.page.locator("//*[@id='taskName']").click()
            self.page.locator("//*[@id='taskName']").fill(dependency)
            self.page.wait_for_timeout(2000)
            self.page.locator("//*[@id='taskName']").press("Enter")
        message = self.page.get_by_text("Task dependency already")
        assert message.is_visible(), "Add same dependency failed"

    def get_all_task_names(self):
        task_rows = self.page.locator("div.border-b.flex").all()
        self.all_tasks = len(task_rows)
        self.all_task_names = []
        
        for task_row in task_rows:            
            task_name_element = task_row.locator("span.text-gray-700.text-sm")
            if not task_name_element.is_visible():
                continue
            task_name = task_name_element.inner_text().strip()
            self.all_task_names.append(task_name)

    def add_non_existing_dependency_via_task_drawer(self):
        task_names = self.all_task_names
        while True:
            dependency = self.faker.word()
            if dependency not in task_names:
                break
            else:
                continue
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.get_by_role("button", name="+ Add new dependency").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='taskName']").click()
        self.page.locator("//*[@id='taskName']").fill(dependency)
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='taskName']").press("Enter")
        self.page.wait_for_timeout(3000)

        #verify dependency
        drawer_dependency = self.page.locator("span.ant-typography-ellipsis")
        assert not drawer_dependency.is_visible(),"Add non existing dependency failed"

    def add_empty_dependency_via_task_drawer(self):
        dependency = ""
        self.page.locator(".ant-tabs-card div.ant-tabs-tab", has_text="Info").click()
        self.page.get_by_role("button", name="+ Add new dependency").click()
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='taskName']").click()
        self.page.locator("//*[@id='taskName']").fill(dependency)
        self.page.wait_for_timeout(2000)
        self.page.locator("//*[@id='taskName']").press("Enter")
        self.page.wait_for_timeout(3000)

        #verify dependency
        drawer_dependency = self.page.locator("span.ant-typography-ellipsis")
        assert not drawer_dependency.is_visible(),"Add non existing dependency failed"

    def change_status_when_dependency_is_not_done(self,status):
        status_dropdown = self.page.locator(".ant-select-borderless .ant-select-selection-item span")
        status_dropdown.click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".ant-select-item-option", has_text=status).click()
        self.page.wait_for_timeout(1000)
        message = self.page.get_by_text("Please complete the task dependencies before proceeding")
        assert message.is_visible(), "Change status to done when dependency is not done failed"

    def change_status_when_dependency_is_not_done_via_bulk_action(self, status: str):
        bulk_actions_menu = self.page.locator("body > div:nth-of-type(2)")
        bulk_actions_menu.page.locator(".anticon-retweet path").click()
        self.page.locator("span.ant-badge-status-text", has_text=status).click()
        self.page.wait_for_timeout(1000)
        message = self.page.get_by_text("Please complete the task dependencies before proceeding")
        assert message.is_visible(), "Change status to done when dependency is not done failed"

    def drag_and_drop_the_dependency_is_not_done_task(self, drop_phase):
        task_name = self.test_task_name
        status_phases = self.page.locator(self.phase_list).all()
        for status_phase in status_phases:
            task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                drop_phase = self.page.locator(self.phase_list, has_text=drop_phase).first
                
                done_row = drop_phase.locator("div.border-b.flex").first
                todo_handle = task_row.locator(".anticon-holder path")
                todo_handle_box = todo_handle.bounding_box()
                done_box = done_row.bounding_box()
                self.page.mouse.move(
                    todo_handle_box["x"] + 5,
                    todo_handle_box["y"] + 5
                )
                self.page.mouse.down()

                self.page.mouse.move(
                    done_box["x"] + 5,
                    done_box["y"] + done_box["height"] / 2,
                    steps=15
                )

                self.page.mouse.up()
                self.page.wait_for_timeout(1000)
                break

        #verify task is moved to correct phase
        message = self.page.get_by_text("Please complete the task dependencies before proceeding")
        assert message.is_visible(), "Drag and drop when dependency is not done task failed"

        task_row = drop_phase.locator("div.border-b.flex", has_text=task_name)
        assert not task_row.is_visible(), "Drag and drop when dependency is not done task failed"

    def change_status_when_dependency_is_not_done_task(self, status):
        task_name = self.test_task_name
        phases = self.page.locator(self.phase_list).all()
        for phase in phases:
            task_row = phase.locator("div.border-b.flex", has_text=task_name)
            if task_row.is_visible():
                # column_selector = self.get_column_selector_by_text("Status", start_index=1)
                task_name_locator = task_row.locator("[data-column-id='status'] button")
                if task_name_locator.is_visible():
                    # task_name_locator.locator("button").first.click()
                    task_name_locator.click()
                    status_dropdown = self.page.locator("div.fixed")
                    status_select_item = status_dropdown.locator("span", has_text=status)
                    status_select_item.click()
                    self.page.wait_for_timeout(1000)
                    break
        # Verify status changed
        message = self.page.get_by_text("Please complete the task dependencies before proceeding")
        assert message.is_visible(), "Change status when dependency is not done task failed"
        self.page.locator(".anticon-sync path").click()
        self.page.wait_for_timeout(3000)
        status_phase = self.page.locator(self.phase_list, has_text=status).first
        new_task_row = status_phase.locator("div.border-b.flex", has_text=task_name)
        new_task_name_locator = new_task_row.locator("[data-column-id='status'] button")
        status_button = new_task_name_locator.inner_text().strip()
        assert status != status_button, "Change status when dependency is not done task failed"

    def change_status_when_dependency_is_not_done_task_via_task_drawer(self,status):
        status_dropdown = self.page.locator(".ant-select-borderless .ant-select-selection-item span")
        status_dropdown.click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".ant-select-item-option", has_text=status).click()
        self.page.wait_for_timeout(1000)

        message = self.page.get_by_text("Please complete the task dependencies before proceeding")
        assert message.is_visible(), "Drag and drop when dependency is not done task failed"

    def change_status_when_dependency_is_not_done_task_via_kanban_board(self,status):
        self.page.get_by_text("Board").click()
        self.page.wait_for_timeout(3000)
        task_name = self.test_task_name
        to_column = self.page.locator("div:nth-of-type(3) div.enhanced-kanban-task-card:nth-of-type(1)").first

        task_card = self.page.locator("div").filter(has_text=re.compile(r"^"+task_name)).first

        task_card.scroll_into_view_if_needed()
        to_column.scroll_into_view_if_needed()

        task_box = task_card.bounding_box()
        target_box = to_column.bounding_box()

        assert task_box, "Task not found"
        assert target_box, "Target column not found"


        # Start drag
        self.page.mouse.move(
            task_box["x"] + task_box["width"] / 2,
            task_box["y"] + task_box["height"] / 2
        )
        self.page.mouse.down()

        # Drag to column center
        self.page.mouse.move(
            target_box["x"] + target_box["width"] / 2,
            target_box["y"] + target_box["height"] / 2,
            steps=15
        )

        # Drop
        self.page.mouse.up()

        #verify task is moved to correct phase
        message = self.page.get_by_text("Please complete the task dependencies before proceeding")
        assert message.is_visible(), "Drag and drop when dependency is not done task failed"

    def create_new_task(self):
        create_task_btn = self.page.locator(self.create_task_button)
        create_task_btn.click()
        self.page.wait_for_timeout(1000)

        create_task_card = self.page.locator(self.create_task_card)
        assert create_task_card.is_visible(), "Create task failed"

        task_name = self.faker.name()
        task_name_input = self.page.locator(self.task_name)
        task_name_input.click()
        self.page.locator("input[placeholder='Type your Task']").clear()
        self.page.locator("input[placeholder='Type your Task']").fill(task_name)

    def create_task_via_create_task_button(self):
        create_task_btn = self.page.locator(self.create_task_button)
        create_task_btn.click()
        self.page.wait_for_timeout(1000)

        create_task_card = self.page.locator(self.create_task_card)
        assert create_task_card.is_visible(), "Create task failed"

        task_name = self.faker.name()
        self.test_task_name = task_name
        task_name_input = self.page.locator(self.task_name)
        task_name_input.click()
        self.page.locator("input[placeholder='Type your Task']").clear()
        self.page.locator("input[placeholder='Type your Task']").fill(self.test_task_name)

    def recurring_toggle_via_task_drawer(self, is_billable: bool):
        toggle = self.page.locator(".ant-form-item-control-input-content div span.ant-switch-inner")
        switch = self.page.locator(".ant-switch-checked div").nth(1)
        if is_billable:
            toggle.click()
            self.page.wait_for_timeout(3000)
            assert switch.is_visible(), "Recurring toggle enable via task drawer failed"
        else:
            toggle.click()
            self.page.wait_for_timeout(3000)
            assert not switch.is_visible(), "Recurring toggle disable via task drawer failed"

    def verify_recurring_toggle_enabled(self, is_billable: bool):
        switch = self.page.locator(".ant-switch-checked div").nth(1)
        if is_billable:
            assert switch.is_visible(), "Recurring toggle enable via task drawer failed"
        else:
            assert not switch.is_visible(), "Recurring toggle disable via task drawer failed"

    def verify_enabled_recurring_type_show_via_task_drawer(self):
        recurring_value = self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value != "", "Recurring type show on the dask drawer failed"

    def verify_recurring_task_in_task_list(self, is_enabled: bool):
        task_row = self.page.locator("div.border-b.flex", has_text=self.test_task_name).first
        dependency_icon = task_row.locator(".anticon.anticon-retweet > svg")
        if is_enabled:
            assert dependency_icon.is_visible(), "Recurring task show on the task list failed"
        else:
            assert not dependency_icon.is_visible(), "Recurring task not show on the task list failed"

    def configure_recurring_repeats_to_daily(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"

        self.page.get_by_title("Daily").click()
        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Daily", "Configure recurring task to daily failed"

    def configure_recurring_repeats_to_weekly(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()

        self.page.get_by_title("Weekly").click()
        self.page.get_by_role("checkbox", name="Mon").check()
        self.page.get_by_role("checkbox", name="Wed").check()

        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Weekly", "Configure recurring task to weekly failed"

    def configure_recurring_repeats_to_monthly_on_specific_date(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()

        self.page.get_by_title("Monthly").click()
        self.page.get_by_text("On a specific date").click()
        self.page.get_by_title("1", exact=True).click()
        self.page.get_by_title("5").click()

        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Monthly", "Configure recurring task to monthly on specific date failed"

    def configure_recurring_repeats_to_monthly_on_specific_day(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()

        self.page.get_by_title("Monthly").click()
        self.page.get_by_text("On a specific day").click()
        self.page.locator("div.ant-form-item:nth-of-type(3) div.ant-select-selector").click()
        self.page.get_by_title("Third").click()
        self.page.wait_for_timeout(1000)
        config_card.locator("div.ant-select-selector").last.click()
        self.page.get_by_title("Wed").click()

        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Monthly", "Configure recurring task to monthly on specific day failed"

    def configure_recurring_repeats_to_x_days(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()

        self.page.get_by_title("Every X Days").click()
        self.page.get_by_role("tooltip", name="Recurring task configuration").get_by_role("spinbutton").fill("5")

        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Every X Days", "Configure recurring task to x days failed"

    def configure_recurring_repeats_to_x_weeks(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()

        self.page.get_by_title("Every X Weeks").click()
        self.page.get_by_role("tooltip", name="Recurring task configuration").get_by_role("spinbutton").fill("2")

        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Every X Weeks", "Configure recurring task to x weeks failed"

    def configure_recurring_repeats_to_x_months(self):
        self.page.get_by_label("Info").get_by_role("button", name="setting").click()
        config_card =self.page.get_by_role('tooltip', name="Recurring task configuration")
        assert config_card.is_visible(), "Configure recurring task failed"
        self.page.locator(".ant-form-vertical div.ant-select-selector").click()

        self.page.get_by_title("Every X Months").click()
        self.page.get_by_role("tooltip", name="Recurring task configuration").get_by_role("spinbutton").fill("2")

        self.page.get_by_role("button", name="Save Changes").click()
        self.page.wait_for_timeout(3000)
        recurring_value =self.page.locator("button.ant-btn-link").inner_text().strip()
        assert recurring_value == "Every X Months", "Configure recurring task to x months failed"

    def move_to_next_task_via_task_drawer(self):
        current_task_value = self.page.locator("p.task-name-display").inner_text().strip()
        self.page.locator(".ant-btn-text .anticon-down path").click()
        self.page.wait_for_timeout(3000)
        next_task_value = self.page.locator("p.task-name-display").inner_text().strip()
        assert next_task_value != current_task_value, "Move to previous task via task drawer failed"

    def move_to_previous_task_via_task_drawer(self):
        self.page.get_by_role("button", name="up", exact=True).click()
        self.page.wait_for_timeout(3000)
        previous_task_value = self.page.locator("p.task-name-display").inner_text().strip()
        assert previous_task_value != self.test_task_name, "Move to previous task via task drawer failed"

    def open_first_task_via_task_drawer(self):
        status_phases = self.page.locator(self.phase_list).all()
        for status_phase in status_phases:
            task_row = status_phase.locator("div.border-b.flex").first
            task_column = task_row.locator("span.text-gray-700.text-sm")
            task_name = task_column.inner_text().strip()
            task_row.scroll_into_view_if_needed()
            if task_row.is_visible():
                task_column = task_row.locator("//*[@data-column-id='title']")
                task_column.hover()
                task_column.locator("button",has_text="Open").first.click()
                self.page.wait_for_timeout(2000)
                break
        assert self.page.locator("div.ant-drawer-header", has_text=task_name).is_visible(), "Open first task via task drawer failed"

    def task_counts_in_task_drawer(self):
        task_count_value = self.page.locator(".ant-drawer-title .ant-flex > span").inner_text().strip()
        match = re.search(r"(?<=/)\s*\d+", task_count_value)
        task_count = match.group().strip()
        task_row_count = self.task_counts_in_task_list()
        assert task_row_count == int(task_count), "Task count in task drawer is not correct"

    def task_counts_in_task_list(self):
        status_phases = self.page.locator(self.phase_list).all()
        for status_phase in status_phases:
            status_phase = self.page.locator(self.phase_list).first
            if status_phase.is_visible():
                task_row_count = status_phase.locator("div.border-b.flex").count()
                break
        return task_row_count
    
    def copy_task_link_in_task_drawer(self):
        self.page.get_by_role("button", name="ellipsis").click()
        self.page.get_by_text("Copy link to task").click()
        self.page.wait_for_timeout(1000)
        message = self.page.get_by_text("Link copied to clipboard")
        assert message.is_visible(), "Copy task link in task drawer failed"

        copied_link = self.page.evaluate("navigator.clipboard.readText()")
        assert copied_link != "", "Clipboard is empty"

    def past_task_link(self):
        copied_link = self.page.evaluate("navigator.clipboard.readText()")
        self.page.goto(copied_link)
        self.page.wait_for_timeout(5000)
        task_name = self.page.locator("p.task-name-display").inner_text().strip()
        assert task_name == self.test_task_name, "Paste task link failed"

    def delete_task_in_task_drawer(self):
        self.page.get_by_role("button", name="ellipsis").click()
        delete_button = self.page.get_by_text("Delete Task")
        delete_button.click()
        self.page.wait_for_timeout(3000)
        assert not delete_button.is_visible(), "Delete task in task drawer failed"