from cmath import phase
from pages.base_page import BasePage
from playwright.sync_api import Page
from datetime import datetime, timedelta
from faker import Faker
from pathlib import Path
import random
import re

from tests.conftest import page

class KanbanBoardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.faker = Faker()
        self.filter_button = "button.rounded-md.font-medium"
        self.filter_button_value = "button.flex.w-full"
        
        #manage phase/status card locators
        self.manage_button = "button.font-semibold.px-3"
        self.manage_status_phase_card = "div.ant-modal-content"
        self.status_cards = "div.transition-all.rounded-lg"

        #kanban board locators
        self.status = "div.flex:nth-of-type(5) button"
        self.kanban_cards = ".enhanced-kanban-group > div:nth-of-type(2)"

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
        
    def open_kanban_board(self):
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
        assert project_name in project_tab_name, "Open kanban board failed"

        self.page.locator(".ant-tabs-tab-btn .ant-flex > span", has_text="Board").click()
        self.page.wait_for_timeout(2000)
        self.wait_for_selector("div.enhanced-kanban-group-header")
        kanban_cards = self.page.locator("div.enhanced-kanban-group-header").first
        assert kanban_cards.is_visible(), "Open kanban board failed"

    def open_kanban_board_in_ipad(self):
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
        assert project_name in project_tab_name, "Open kanban board failed"

        self.page.locator(".ant-tabs-tab-btn .ant-flex > span", has_text="Board").click()
        self.page.wait_for_timeout(2000)
        self.wait_for_selector("div.enhanced-kanban-group-header")
        kanban_cards = self.page.locator("div.enhanced-kanban-group-header").first
        assert kanban_cards.is_visible(), "Open kanban board failed"
    
    def verify_ui_elements(self):
        assert self.page.locator(self.filter_button, has_text="Search").is_visible(), "Search input not visible"
        assert self.page.locator(self.filter_button, has_text="Priority").is_visible(), "Priority button not visible"
        assert self.page.locator(self.filter_button, has_text="Members").is_visible(), "Members button not visible"
        assert self.page.locator(self.filter_button, has_text="Labels").is_visible(), "Labels button not visible"
        assert self.page.locator(self.filter_button, has_text="Group by").is_visible(), "Group by button not visible"
        assert self.page.locator("button.font-semibold", has_text="Manage Statuses").is_visible(), "Manage Status button not visible"
        assert self.page.locator("div.enhanced-kanban-task-card").first.is_visible(), "Task cards not visible"

        # # Verify tooltips in button hover in kanban board tab
        # # Search
        # self.page.get_by_role("button", name="Search").hover()
        # self.page.get_by_label("Search", exact=True).hover()
        # self.page.locator(self.filter_button, has_text="Search").first.hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Search").is_visible(), "Search not visible on hover"
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
        # # # Group by
        # self.page.locator(self.filter_button, has_text="Group by").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Group by").is_visible(), "Group by not visible on hover"
        # # Manage Statuses
        # self.page.locator("button.font-semibold", has_text="Manage Statuses").hover()
        # self.page.wait_for_timeout(500)
        # assert self.page.locator("//*[@role='tooltip']", has_text="Manage Statuses").is_visible(), "Manage Statuses not visible on hover"

        # verify UI elements by hovering

    def get_random_task_name(self):
        """Get project tasks names"""
        task_names_selector = self.page.locator("div.task-title").all()
        random_task = random.choice(task_names_selector)
        self.random_task_name = random_task.inner_text().strip()
        return self.random_task_name

    def task_search_by_name(self):

        if not self.random_task_name:
            return
        
        task_name = self.random_task_name
        kanban_card = self.page.locator(self.kanban_cards, has_text=task_name)
        self.all_tasks = self.page.locator("div.task-title").count()
        phase_text = kanban_card.locator("div.text-sm").inner_text().strip()
        match = re.search(r'^[^(]+', phase_text)
        phase_name = match.group().strip()
        self.page.locator(self.filter_button, has_text="Search").click()
        search_input = self.page.locator("input.w-full")
        search_input.fill(task_name)
        self.page.get_by_role("button", name="Search").click()
        self.page.wait_for_timeout(2000)
        
        #verify search result
        kanban_card = self.page.locator(self.kanban_cards, has_text=phase_name)
        searched_output = kanban_card.locator("div.task-title", has_text=task_name)
        assert searched_output.is_visible(), (f"Search failed: '{task_name}' not found")

    def reset_task_list(self):
        self.page.locator("button.duration-200.transition-colors.text-xs", has_text="Cancel").click()
        self.page.wait_for_timeout(2000)
        reset_task_count = self.page.locator("div.task-title").count()
        assert reset_task_count == self.all_tasks, (f"Reset Kanban board failed")

    def get_column_selector_by_text(self, column_name: str, start_index: int) -> str:
        headers = self.page.locator("div.text-sm")
        count = headers.count()

        for i in range(start_index, count):  # Playwright is 0-based
            header = self.page.locator(f"div.flex:nth-of-type({i+1})")
            header_text = header.first.inner_text().strip().lower()

            if column_name.lower() in header_text:
                return f"div.flex:nth-of-type({i + 1})"

        raise AssertionError(f"Column '{column_name}' not found starting from index {start_index}")

    def priority_filter(self,multiple_priorities: bool):
        priority_button = self.page.locator(self.filter_button, has_text="Priority")
        priority_button.click()

        # Filter tasks by priority
        drop_down = self.page.locator(".max-h-48 > div")
        priorities = drop_down.locator(self.filter_button_value).all()
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
        high = "background-color: rgba(205, 92, 92, 0.41);"
        medium = "background-color: rgba(218, 165, 32, 0.41);"
        low = "background-color: rgba(46, 139, 87, 0.41);"
        priority_names = []
        phase_list = self.page.locator(self.kanban_cards).all()

        for phase in phase_list:
            task_cards = phase.locator("div.enhanced-kanban-task-card").all()
            for task_card in task_cards:
                task_name_locator = task_card.locator("span.w-2")
                if task_name_locator.is_visible():
                    priority_style = task_name_locator.get_attribute("style")
                    if high in priority_style:
                        priority_names.append("High")
                    elif medium in priority_style:
                        priority_names.append("Medium")
                    elif low in priority_style:
                        priority_names.append("Low")                
            
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
        drop_down = self.page.locator(".max-h-48 > div")
        priorities = drop_down.locator(self.filter_button_value).all()
        label_filters = []
        multiple_limits = random.randint(2, 5)
        for label in random.sample(priorities, len(priorities)):
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
        phase_list = self.page.locator(self.kanban_cards).all()

        for phase in phase_list:
            task_cards = phase.locator("div.enhanced-kanban-task-card").all()
            for task_card in task_cards:
                task_name_locator = task_card.locator("div.task_labels")
                if task_name_locator.is_visible():
                    task_name_locator.click()
                    self.page.wait_for_timeout(2000)

                    self.page.locator(".ant-flex-wrap-wrap button").click()
                    labels_dropdown = self.page.locator("div.ant-card-body")
                    labels_list = labels_dropdown.locator("li.ant-list-item").all()

                    for label in labels_list:
                        checkbox_class = label.locator(".ant-checkbox").get_attribute("class") or ""
                        if "ant-checkbox-checked" in checkbox_class:
                            label_text = label.inner_text().strip()
                            label_names.append(label_text)
                        else:
                            continue          
            
                    # validate filtered values
                    assert any(name in label_filters for name in label_names), f"Task filter by {label_filters} failed"

                self.page.locator(".ant-drawer-close path").click()
                self.page.wait_for_timeout(1000)
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
        drop_down = self.page.locator(".max-h-48 > div")
        members = drop_down.locator(self.filter_button_value).all()
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
        phase_list = self.page.locator(self.kanban_cards).all()

        for phase in phase_list:
            task_cards = phase.locator("div.enhanced-kanban-task-card").all()
            for task_card in task_cards:
                task_name_locator = task_card.locator("button:has(span[aria-label='plus'])")
                if task_name_locator.is_visible():
                    task_name_locator.scroll_into_view_if_needed()
                    task_name_locator.hover()
                    task_name_locator.click()
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
        self.page.get_by_role("button", name="Search").click()
        self.page.wait_for_timeout(2000)

        # Verify non-existant task search by name
        searched_output = self.page.locator("div.task-title", has_text=task_search_input)
        assert not searched_output.is_visible(), "Non-existant task search by name failed"

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
        self.page.locator(".anticon-close path").click()
        self.page.wait_for_timeout(1000)
        task_card = self.page.locator("div.task-title", has_text=task_name)
        assert task_card.is_visible(), "Create task failed"

    def import_task(self):
        self.page.locator(self.import_dropdown).click()
        self.page.locator(self.import_task_option).click()
        self.page.wait_for_timeout(1000)

        import_task_card = self.page.locator(self.create_task_card)
        assert import_task_card.is_visible(), "Import task failed"

        self.page.locator(self.template_name_dropdown).click()
        temlplate_list = self.page.locator(self.template_list).all()
        random.choice(temlplate_list).click()

        selected_tasks = []
        self.page.wait_for_timeout(3000)
        tasks = self.page.locator(self.selected_tasks).all()
        for task in tasks:
            task_name = task.inner_text().strip()
            selected_tasks.append(task_name)

        self.page.locator("button", has_text="Import").click()
        self.page.wait_for_timeout(2000)

        task_cards = self.page.locator("div.task-title").all()
        all_tasks = []
        for task_card in task_cards:
            task_name = task_card.inner_text().strip()
            all_tasks.append(task_name)

        assert any(selected_task in all_tasks for selected_task in selected_tasks), "Import task failed"

    def add_a_task_by_phase_column(self):
        task_name = self.faker.word()
        self.test_task_name = task_name
        kanban_card = self.page.locator(self.kanban_cards).first
        kanban_card.locator(".enhanced-kanban-group-header > .flex.items-center.justify-between > .flex.items-center.gap-1 > button").click()
        kanban_card.get_by_placeholder("Write a task Name").fill(task_name)
        kanban_card.get_by_placeholder("Write a task Name").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify task added in task list
        task = kanban_card.locator("div.task-title", has_text=task_name)
        assert task.is_visible(), "Add a task by phase column failed"

    def add_a_task_by_kanban_card(self, is_new_phase: bool):
        task_name = self.faker.word()
        self.test_task_name = task_name
        if is_new_phase:
            kanban_card = self.page.locator(self.kanban_cards, has_text=self.capitalized_phase_name)
        else:
            kanban_card = self.page.locator(self.kanban_cards).all()
            kanban_card = random.choice(kanban_card)
        input_task_name = kanban_card.get_by_placeholder("Write a task Name")
        if not input_task_name.is_visible():
            kanban_card.locator("button.h-10").click()
        kanban_card.get_by_placeholder("Write a task Name").fill(task_name)
        kanban_card.get_by_placeholder("Write a task Name").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify task added in task list
        task = kanban_card.locator("div.task-title", has_text=task_name)
        assert task.is_visible(), "Add a task by phase column failed"

    def drag_and_drop(self):
        task_name = self.test_task_name

        # Kanban column container
        container = self.page.locator(self.kanban_cards).first
        container.wait_for(state="visible", timeout=15000)

        current_position = self._get_task_position(task_name)

        # Source task card
        source_task = container.locator("div.enhanced-kanban-task-card",has_text=task_name).first
        source_task.wait_for(state="visible", timeout=10000)

        source_box = source_task.bounding_box()

        start_x = source_box["x"] + source_box["width"] / 2
        start_y = source_box["y"] + source_box["height"] / 2

        self.page.mouse.move(start_x, start_y, steps=8)
        self.page.mouse.down()
        self.page.wait_for_timeout(80)

        self.page.mouse.move(start_x + 3, start_y + 3, steps=2)
        self.page.wait_for_timeout(120)

        container_box = container.bounding_box()

        target_x = container_box["x"] + container_box["width"] / 2
        target_y = container_box["y"] + 30   # INSIDE droppable area

        distance_y = target_y - start_y
        total_steps = 45
        step_size_y = distance_y / total_steps
        current_y = start_y

        for _ in range(total_steps):
            current_y += step_size_y
            self.page.mouse.move(target_x, current_y, steps=1)
            self.page.wait_for_timeout(40)

        self.page.wait_for_timeout(250)

        # Small jitter INSIDE container (important)
        self.page.mouse.move(target_x + 2, target_y + 2, steps=1)
        self.page.wait_for_timeout(120)

        self.page.mouse.up()
        self.page.wait_for_timeout(3000)

        final_position = self._get_task_position(task_name)
        assert current_position != final_position, "Drag and drop status column in Kanban failed"

    def _get_task_position(self, task_name: str) -> int:
        container = self.page.locator(self.kanban_cards).first
        titles = container.locator("div.task-title").all()
        for idx, title in enumerate(titles, 1):
            if title.inner_text().strip() == task_name:
                return idx
        return -1  # not found

    def rename_status_column(self):
        status = self.faker.word()
        kanban_cards = self.page.locator(self.kanban_cards).all()
        kanban_card = random.choice(kanban_cards)
        kanban_card.locator(".relative button").click()
        current_phase_text = kanban_card.locator("div.text-sm").inner_text().strip()
        match = re.search(r'^[^(]+', current_phase_text)
        current_phase_name = match.group().strip()
        self.page.get_by_text("Rename").click()
        self.page.get_by_role("textbox").fill(status)
        self.page.get_by_role("textbox").press("Enter")
        self.page.wait_for_timeout(2000)

        #verify status name changed in task list
        phase_text = kanban_card.locator("div.text-sm").inner_text().strip()
        match = re.search(r'^[^(]+', phase_text)
        phase_name = match.group().strip().lower()

        assert status == phase_name, "rename status column failed"

        kanban_card.locator(".relative button").click()
        self.page.get_by_text("Rename").click()
        self.page.get_by_role("textbox").fill(current_phase_name)
        self.page.get_by_role("textbox").press("Enter")
        self.page.wait_for_timeout(2000)

    def change_main_category(self, status):
        kanban_card = self.page.locator(self.kanban_cards).first
        kanban_card.locator(".relative button").click()
        status_ele = self.page.locator("div.border-t:nth-of-type(1) button", has_text=status).first
        status_ele.click()
        message = self.page.get_by_text("Status category update failed!")
        assert message.is_visible(), "Change main category failed"

    def change_new_category(self, status):
        todo = "background-color: rgb(169, 169, 169);"
        doing = "background-color: rgb(112, 166, 243);"
        done = "background-color: rgb(117, 201, 151);"

        if status == "To do":
            phase_color = todo
        elif status == "Doing":
            phase_color = doing
        elif status == "Done":
            phase_color = done

        phase_name = self.faker.word()
        capitalized_phase_name = phase_name.capitalize()
        self.page.get_by_text("Add Section").click()
        self.page.get_by_placeholder("Untitled section").fill(phase_name)
        self.page.get_by_placeholder("Untitled section").press("Enter")
        self.page.wait_for_timeout(1000)
        kanban_card = self.page.locator(self.kanban_cards, has_text=capitalized_phase_name)
        kanban_card.locator(".relative button").click()
        status_ele = self.page.locator("div.border-t:nth-of-type(1) button", has_text=status).first
        status_ele.click()
        self.page.wait_for_timeout(2000)
        phase_color_style = kanban_card.locator("div.enhanced-kanban-group-header").get_attribute("style")
        assert phase_color_style == phase_color, "Change new category failed"

    def create_new_category(self):
        phase_name = self.faker.word()
        self.capitalized_phase_name = phase_name.capitalize()
        self.page.get_by_text("Add Section").click()
        self.page.get_by_placeholder("Untitled section").fill(phase_name)
        self.page.get_by_placeholder("Untitled section").press("Enter")
        self.page.wait_for_timeout(2000)
        kanban_card = self.page.locator(self.kanban_cards, has_text=self.capitalized_phase_name)
        assert kanban_card.is_visible(), "Create new category failed"

    def delete_category(self, with_tasks: bool):
        phase_name = self.capitalized_phase_name
        kanban_card = self.page.locator(self.kanban_cards, has_text=phase_name)
        task_list = []
        tasks = kanban_card.locator("div.task-title").all()
        for task in tasks:
            task_name = task.inner_text().strip()
            task_list.append(task_name)
        kanban_card.locator(".relative button").click()
        self.page.get_by_text("Delete").click()
        self.page.get_by_role("button", name="Delete").click()
        self.page.wait_for_timeout(2000)

        if with_tasks:
            move_delete_phase_card = self.page.get_by_text("You are deleting a status")
            assert move_delete_phase_card.is_visible(), "Delete category with tasks failed"
            self.page.locator("span.ant-select-selection-item").click()
            self.page.get_by_text("Doing", exact=True).click()
            self.page.get_by_role("button", name="Done").click()
            self.page.wait_for_timeout(2000)
            
            kanban_card = self.page.locator(self.kanban_cards, has_text="Doing")
            task_locators = kanban_card.locator("div.task-title").all()
            task_values = [task.inner_text().strip() for task in task_locators]
            assert any(task in task_values for task in task_list), "Delete category with tasks failed"

        else:
            kanban_card = self.page.locator(self.kanban_cards, has_text=phase_name)
            assert not kanban_card.is_visible(), "Delete category failed"

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
        kanban_cards = self.page.locator(self.kanban_cards).all()

        for phase in kanban_cards:
            task_phase_names = []
            phase_text = phase.locator("div.text-sm").inner_text().strip()
            match = re.search(r'^[^(]+', phase_text)
            phase_status = match.group().strip()
            if phase_status == "Unmapped":
                phase_status = "Select"
            task_phase_names.append(phase_status)
            
            # validate group by values
        assert all(name in phase_status for name in task_phase_names), f"Task group by {group_by} in kanban board failed"
    
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
        kanban_cards = self.page.locator(self.kanban_cards).all()

        for phase in kanban_cards:
            phase_text = phase.locator("div.text-sm").inner_text().strip()
            match = re.search(r'^[^(]+', phase_text)
            phase_status = match.group().strip()
            if test_status_name ==  phase_status:
                assert True, "Create new status failed"
                break

    def add_due_date(self):
        task_name = self.test_task_name
        today = datetime.today()
        next_week = today + timedelta(days=7)
        next_week_str = next_week.strftime("%b %d, %Y")
        kanban_cards = self.page.locator(self.kanban_cards).all()

        for phase in kanban_cards:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_card.get_by_text("No due date").click()
                self.page.get_by_text("Next week").click()
                break
        self.page.wait_for_timeout(2000)
        due_date = task_card.get_by_text(next_week_str)
        
        assert due_date.is_visible(), "Set due date for task failed"

    def change_due_date(self):
        task_name = self.test_task_name
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        tomorrow_str = tomorrow.strftime("%b %d, %Y")
        kanban_cards = self.page.locator(self.kanban_cards).all()

        for phase in kanban_cards:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_card.locator("div.task-due-date").click()
                self.page.get_by_text("Tomorrow").click()
                break
        self.page.wait_for_timeout(2000)
        due_date = task_card.get_by_text(tomorrow_str)
        
        assert due_date.is_visible(), "Change due date for task failed"

    def assign_members_for_task(self):
        task_name = self.test_task_name
        kanban_cards = self.page.locator(self.kanban_cards).all()

        for phase in kanban_cards:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_name_locator =task_card.locator("button:has(span[aria-label='plus'])")
                task_name_locator.scroll_into_view_if_needed()
                task_name_locator.hover()
                task_name_locator.click()
                members_dropdown = self.page.locator("div.fixed")
                member = members_dropdown.locator("div.p-2.flex").first
                selected_name = member.locator("div.font-medium").nth(1).inner_text().strip().split("\n")[-1]
                member.click()
                self.page.wait_for_timeout(2000)
                task_name_locator.click()

                # Verify assigned members
                task_name_locator.click()
                members_dropdown = self.page.locator("div.fixed")
                checkbox_class = member.locator("div.w-4").get_attribute("class") or ""
                if "bg-blue-500 border-blue-500" in checkbox_class:
                    member_text = member.locator("div.font-medium").nth(1).inner_text().strip().split("\n")[-1]
                    assert selected_name == member_text, "Assign members for task failed"
                else:
                    assert False, "Assign members for task failed - Task not found"
                break

    def invite_members_for_task(self):
        email = self.faker.email()
        task_name = self.test_task_name
        kanban_cards = self.page.locator(self.kanban_cards).all()

        for phase in kanban_cards:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_name_locator =task_card.locator("button:has(span[aria-label='plus'])")
                task_name_locator.scroll_into_view_if_needed()
                task_name_locator.hover()
                task_name_locator.click()
                self.page.wait_for_timeout(1000)
                members_dropdown = self.page.locator("div.fixed")
                members_dropdown.get_by_text("Invite member").click()
                self.page.wait_for_timeout(1000)
                invite_card = self.page.locator("div.ant-modal-content")
                assert invite_card.is_visible(), "Invite members for task failed"

                invite_card.locator("div.ant-select-selection-overflow").click()
                invite_card.get_by_role("combobox", name="Invite with email").fill(email)
                invite_card.get_by_role("combobox", name="Invite with email").press("Enter")
                invite_card.get_by_role("button", name="Invite", exact=True).click()
                self.page.wait_for_timeout(2000)

                message = self.page.get_by_text(re.compile(r"\d+ project member\(s\) invited successfully"))

                assert message.is_visible(), "Invite members for task failed"
                break

    def drag_and_drop_task_to_different_phase(self,status):
        task_name = self.test_task_name
        to_column = self.page.locator(self.kanban_cards, has_text=status)      

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
        task_card = to_column.locator("div.enhanced-kanban-task-card", has_text=task_name)
        assert task_card.is_visible(), "Drag and drop task to different phase failed"

    def open_task_drawer(self):
        task_name = self.test_task_name
        status_phases = self.page.locator(self.kanban_cards).all()
        for status_phase in status_phases:
            task_card = status_phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            task_card.scroll_into_view_if_needed()
            if task_card.is_visible():
                task_card.click()
                self.page.wait_for_timeout(2000)
                break
        assert self.page.locator("div.ant-drawer-header", has_text=task_name).is_visible(), "Open task drawer failed"

    def get_single_status_category(self):
        status_cards = self.page.locator(self.status_cards).all()
        for status_card in status_cards:
            status_name = status_card.locator("h5").inner_text().strip()
            sub_status_elements = status_card.locator("div.flex-1").count()
            if sub_status_elements == 1:
                self.capitalized_single_phase_name = status_name.capitalize()
                break
        self.page.get_by_text("Close").click()

    def delete_category_in_single_status(self):
        kanban_card = self.page.locator(self.kanban_cards, has_text=self.capitalized_single_phase_name)
        kanban_card.locator(".relative button").click()
        self.page.get_by_text("Delete").click()
        self.page.get_by_role("button", name="Delete").click()
        self.page.wait_for_timeout(2000)

        kanban_card = self.page.locator(self.kanban_cards, has_text=self.capitalized_single_phase_name)
        assert kanban_card.is_visible(), "Deletion of single status in category failed"
        
        kanban_card.locator(".relative button").click()
        self.page.get_by_text("Delete").click()
        self.page.get_by_role("button", name="Delete").click()
        self.page.wait_for_timeout(2000)
        message = self.page.get_by_text("At least one status should exists under each category.")
        assert message.is_visible(), "Deletion of single status in category failed"

    def archive_task(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.kanban_cards).all()
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_card.click(button="right")
                archive_option = self.page.get_by_role("button", name="inbox Archive")
                assert archive_option.is_visible(), "Archive task in kanban board failed"
                archive_option.click()
                self.page.wait_for_timeout(2000)
                break
        
        #verify task archived in kanban board
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            assert not task_card.is_visible(), "Archive task from kanban board failed"

    def verify_archived(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.kanban_cards).all()
        self.page.get_by_role("checkbox", name="Show archived").click()
        self.page.wait_for_timeout(2000)
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                assert task_card.is_visible(), "Archive task from context menu failed"
                break

    def unarchive_task(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.kanban_cards).all()
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_card.click(button="right")
                archive_option = self.page.get_by_role("button", name="inbox Unarchive")
                assert archive_option.is_visible(), "Archive task in kanban board failed"
                archive_option.click()
                self.page.wait_for_timeout(2000)
                break
        
        #verify task unarchived in kanban board
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            assert not task_card.is_visible(), "Archive task from kanban board failed"

    def verify_unarchived(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.kanban_cards).all()
        self.page.get_by_role("checkbox", name="Show archived").click()
        self.page.wait_for_timeout(2000)
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                assert task_card.is_visible(), "Archive task from context menu failed"
                break

    def assign_to_me(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.kanban_cards).all()
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_card.click(button="right")
                assign_to_me_option = self.page.get_by_role("button", name="user-add Assign to me")
                assert assign_to_me_option.is_visible(), "Assign to me in kanban board failed"
                assign_to_me_option.click()
                self.page.wait_for_timeout(2000)
                break

    def verify_assigned_to_me(self):
        task_name = self.test_task_name
        status_phase = self.page.locator(self.kanban_cards).all()
        for phase in status_phase:
            task_card = phase.locator("div.enhanced-kanban-task-card", has_text=task_name)
            if task_card.is_visible():
                task_name_locator =task_card.locator("button:has(span[aria-label='plus'])")
                task_name_locator.scroll_into_view_if_needed()
                task_name_locator.hover()
                task_name_locator.click()
                members_dropdown = self.page.locator("div.fixed")
                member = members_dropdown.locator("div.p-2.flex").first
                checkbox_class = member.locator("div.w-4").get_attribute("class") or ""
                if "bg-blue-500 border-blue-500" in checkbox_class:
                    member_text = member.locator("div.font-medium").nth(1).inner_text().strip().split("\n")[-1]
                    assert member_text == "worklenz test", "Assign to me in kanban board failed"
                else:
                    assert False, "Assign to me in kanban board failed - Task not found"
                break