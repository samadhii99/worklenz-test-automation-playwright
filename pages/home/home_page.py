from cmath import phase
from pages.base_page import BasePage
from playwright.sync_api import Page
from datetime import date, datetime, timedelta
from faker import Faker
from pathlib import Path
import random
import re

from tests.conftest import page

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.faker = Faker()
        self.header_menu = "ul.ant-menu-overflow"
        self.task_list_card = "div.task-list-card"
        self.task_list_table = ".task-list-card div.ant-card-body"
        self.todo_list_header = "div.ant-collapse-header"
        self.table_card = ".ant-col-lg-8 div.ant-card"
        self.todo_list_add_task_input = ".ant-collapse-content-box input"
        self.switch_team_button = "div.ant-dropdown-trigger.ant-flex.ant-flex-align-center.ant-flex-justify-center"
        self.task_name_rows = ".ant-table-cell span.ant-typography"
        self.task_project_rows = ".custom-row-height div.ant-typography"
        self.task_status_rows = ".ant-select-borderless div"
        self.task_due_date_rows = ".ant-picker-input input"
        self.todo_list_mark_as_done = ".ant-table-small td:nth-of-type(1)"
        self.todo_list_rows = ".ant-table-small td:nth-of-type(2)"

        #create project drawer
        self.name_input = "input#name"
        self.project_color = "div.ant-color-picker-color-block-inner"
        self.project_color_menu = "div.ant-popover-inner"
        self.status_dropdown_button = "div.ant-form-item:nth-of-type(3) div.ant-select-selector"
        self.health_dropdown_button = "div:nth-of-type(4) div.ant-select-selector"
        self.category_dropdown_button = "input#category_id"
        self.notes_input = "textarea"
        self.client_input = "input#client_name"
        self.project_manager_add_button = "button.ant-btn-dashed.ant-btn-circle"
        self.start_date_input = "input#start_date"
        self.end_date_input = "input#end_date"
        self.working_days_input = "input#working_days"
        self.man_days_input = "input#man_days"
        self.hours_per_day_input = "input#hours_per_day"
        self.manual_progress_toggle = "#use_manual_progress span.ant-switch-inner"
        self.weighted_progress_toggle = "#use_weighted_progress span.ant-switch-inner"
        self.time_based_progress_toggle = "#use_time_progress span.ant-switch-inner"
        self.create_button = ".ant-space-item button.ant-btn-primary"
        self.close_drawer = ".anticon-close path"
        self.drop_down_menu = "div.ant-select-dropdown"
        self.project_manager_dropdown = "div.ant-dropdown"
        self.project_manager_list = "li.ant-dropdown-menu-item"

    def open_home_page(self):
        self.wait_for_selector("li[data-menu-id*='home']")
        self.page.locator("li[data-menu-id*='home']").click()
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/worklenz/home"), "Home page not loaded properly"

    def open_home_page_in_ipad(self):
        self.page.get_by_role("button").locator("span[aria-label='menu']").click()
        self.page.locator("//div[text()='Home']").click()
        self.page.wait_for_timeout(2000)
        assert self.page.url.endswith("/worklenz/home"), "Home page not loaded properly"        
    
    def verify_ui_elements(self):
        assert self.page.locator(self.header_menu).is_visible(), "Header menu not visible"
        assert self.page.get_by_role("button", name = "crown Upgrade Plan").is_visible(), "Upgrade Plan button not visible"
        assert self.page.get_by_role("button", name = "usergroup-add Invite").is_visible(), "Invite button not visible"
        assert self.page.get_by_role("button", name = "bell").is_visible(), "Notifications icon not visible"
        assert self.page.get_by_role("button", name = "user", exact=True).is_visible(), "Profile icon not visible"
        assert self.page.get_by_role("button").nth(3).is_visible(), "Running timers icon not visible"
        assert self.page.get_by_role("button", name = "edit Create Project").is_visible(), "Create Project button not visible"

        self.page.get_by_role("button", name = "down").click()
        self.wait_for_timeout(1000)
        assert self.page.get_by_text("Import from template").is_visible(), "Import from template button not visible"

        self.page.get_by_role("button", name = "user", exact=True).click()
        self.wait_for_timeout(1000)
        first_name = self.page.locator(".ant-flex .ant-flex-align-stretch span").first.inner_text().strip().split()[0]
        assert self.page.locator("H3", has_text=f"Hi {first_name}").is_visible(), "Welcome message visible failed"
        today_formatted = datetime.today().strftime("%A, %B %d, %Y")
        assert self.page.locator("H4", has_text=f"Today is {today_formatted}").is_visible(), "Today's date not visible"

        #task list card
        assert self.page.locator(self.task_list_table).is_visible(), "Task list table not visible"
        assert self.page.get_by_text("List", exact=True).is_visible(), "List tab not visible"
        assert self.page.get_by_text("Calendar", exact=True).is_visible(), "Calendar tab not visible"
        self.page.get_by_text("Calendar", exact=True).click()
        self.wait_for_timeout(1000)
        assert self.page.locator("div.ant-picker-calendar-header").is_visible(), "Calendar header not visible"
        assert self.page.locator("div.ant-picker-body").is_visible(), "Calendar body not visible"
        assert self.page.locator(self.task_list_card).get_by_text("Assigned to me").is_visible(), "Assigned to me button not visible"
        assert self.page.locator(self.task_list_card).get_by_role("button", name="sync").is_visible(), "Sync button not visible in task list table"

        #todo list card
        assert self.page.locator(self.todo_list_header).is_visible(), "Todo list header not visible"
        self.page.locator(self.todo_list_header).click()
        self.wait_for_timeout(1000)
        assert self.page.locator(self.table_card, has_text="To do list").is_visible(), "Recent Activity card not visible"
        todo_list_card = self.page.locator(self.table_card, has_text="To do list")
        assert todo_list_card.locator(self.todo_list_add_task_input).is_visible(), "Add task input not visible"
        assert todo_list_card.locator(".anticon-sync").is_visible(), "Sync button not visible in todo list table"

        #projects card
        assert self.page.locator(self.table_card, has_text="Projects").is_visible(), "Projects card not visible"
        assert self.page.locator(self.table_card, has_text="Projects").locator(".anticon-star").first.is_visible(), "Add to favorites icon not visible in projects table"
        assert self.page.locator(self.table_card, has_text="Projects").get_by_text("Recent", exact=True).is_visible(), "Recent tab not visible in projects table"
        assert self.page.locator(self.table_card, has_text="Projects").get_by_text("Favourites", exact=True).is_visible(), "Favourites tab not visible in projects table"
        assert self.page.locator(self.table_card, has_text="Projects").locator(".anticon-sync").is_visible(), "Sync button not visible in projects table"

        #recent activity card
        assert self.page.locator(self.table_card, has_text="Recent Activity").is_visible(), "Recent Activity card not visible"
        assert self.page.locator(self.table_card, has_text="Recent Activity").get_by_text("Time Logged", exact=True).is_visible(), "Time Logged tab not visible in recent activity table"
        assert self.page.locator(self.table_card, has_text="Recent Activity").get_by_text("Recent Tasks", exact=True).is_visible(), "Recent Tasks tab not visible in recent activity table"
        assert self.page.locator(self.table_card, has_text="Recent Activity").locator(".anticon-sync").is_visible(), "Sync button not visible in recent recent activity table"

    def verify_tooltips(self):
        self.page.get_by_role("button", name = "crown Upgrade Plan").hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Upgrade Plan").is_visible(), "Upgrade Plan tooltip not visible on hover"

        self.page.get_by_role("button", name = "usergroup-add Invite").hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Invite team members to join").is_visible(), "Invite team members to join tooltip not visible on hover"

        self.page.locator(self.switch_team_button).hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Switch team").is_visible(), "Switch team tooltip not visible on hover"

        self.page.get_by_role("button", name = "bell").hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="View notifications").is_visible(), "View notifications tooltip not visible on hover"

        self.page.get_by_role("button", name = "user", exact=True).hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="View profile").is_visible(), "View profile tooltip not visible on hover"

        self.page.get_by_role("button").nth(3).hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Running Timers").is_visible(), "Running Timers tooltip not visible on hover"

        self.page.locator(self.task_list_card).get_by_role("button", name="sync").hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Refresh").is_visible(), "Refresh tooltip not visible on hover"

        task_name_row = self.page.locator(self.task_name_rows).first
        task_name = task_name_row.inner_text().strip()
        task_name_row.hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text=task_name).is_visible(), f"{task_name} row in task table tooltip not visible on hover"

        self.page.locator(task_name_row, has_text="Open").hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Click open task form").is_visible(), "Click open task form tooltip not visible on hover"

        task_project_row = self.page.locator(self.task_project_rows).first
        task_project_name = task_project_row.inner_text().strip()
        task_project_row.hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text=task_project_name).is_visible(), f"{task_name} row in task table tooltip not visible on hover"

        self.page.locator(self.todo_list_header).click()
        self.wait_for_timeout(1000)
        todo_list_card = self.page.locator(self.table_card, has_text="To do list")
        todo_list_card.locator(".anticon-sync").hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Refresh").is_visible(), "Refresh tooltip not visible on hover"

        self.page.locator(self.todo_list_mark_as_done).first.hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Mark as done").is_visible(), "Mark as done tooltip not visible on hover"

        todo_list_row = self.page.locator(self.todo_list_rows).first
        todo_list_name = todo_list_row.inner_text().strip()
        todo_list_row.hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text=todo_list_name).is_visible(), f"{todo_list_name} row in todo list table tooltip not visible on hover"

        self.page.locator(self.table_card, has_text="Projects").get_by_text("Recent", exact=True).hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Recent").is_visible(), "Recent tooltip not visible on hover"

        self.page.locator(self.table_card, has_text="Projects").get_by_text("Favourites", exact=True).hover()
        self.wait_for_timeout(500)
        assert self.page.locator("//*[@role='tooltip']", has_text="Favourites").is_visible(), "Favourites tooltip not visible on hover"

    def open_create_project_drawer(self):
        self.page.get_by_role("button", name = "edit Create Project").click()
        self.wait_for_timeout(3000)
        assert self.page.get_by_role("dialog").get_by_text("Create project").is_visible(), "Create project drawer not visible"

    def verify_ui_elements_in_create_project_drawer(self):
        assert self.page.locator(self.name_input).is_visible(),"Name input not visible"
        self.page.locator(self.project_color).click()
        self.wait_for_timeout(1000)
        assert self.page.locator(self.project_color_menu).is_visible(),"Project color menu not visible"
        assert self.page.locator(self.status_dropdown_button).is_visible(),"Status field not visible"
        self.page.locator(self.status_dropdown_button).click()
        self.wait_for_timeout(1000)
        assert self.page.locator(self.drop_down_menu).is_visible(),"Status dropdown menu not visible"
        self.page.keyboard.press("Escape")
        self.wait_for_timeout(1000)
        assert self.page.locator(self.health_dropdown_button).is_visible(),"Health field not visible"
        self.page.locator(self.health_dropdown_button).click()
        self.wait_for_timeout(1000)
        assert self.page.locator(self.drop_down_menu).nth(1).is_visible(),"Health dropdown menu not visible"
        self.page.keyboard.press("Escape")
        self.wait_for_timeout(1000)
        assert self.page.locator(self.category_dropdown_button).is_visible(),"Category field not visible"
        self.page.locator(self.category_dropdown_button).click()
        self.wait_for_timeout(1000)
        assert self.page.locator(self.drop_down_menu).nth(2).is_visible(),"Category dropdown menu not visible"
        assert self.page.get_by_role("button", name = "plus New Category").is_visible(), "New category button not visible"
        self.page.keyboard.press("Escape")
        self.wait_for_timeout(1000)
        assert self.page.locator(self.notes_input).is_visible(),"Notes input not visible"
        assert self.page.locator(self.client_input).is_visible(),"Client input not visible"
        assert self.page.locator(self.project_manager_add_button).is_visible(),"Project manager add button not visible"
        self.page.locator(self.project_manager_add_button).click()
        self.wait_for_timeout(1000)
        assert self.page.locator(self.project_manager_dropdown).is_visible(),"Project manager dropdown not visible"
        self.page.locator(self.project_manager_add_button).click()
        assert self.page.locator(self.start_date_input).is_visible(),"Start date input not visible"
        assert self.page.locator(self.end_date_input).is_visible(),"End date input not visible"
        assert self.page.locator(self.working_days_input).is_visible(),"Estimated working days input not visible"
        assert self.page.locator(self.man_days_input).is_visible(),"Estimated man days input not visible"
        assert self.page.locator(self.hours_per_day_input).is_visible(),"Hours per day input not visible"
        assert self.page.locator(self.manual_progress_toggle).is_visible(),"Manual progress toggle not visible"
        assert self.page.locator(self.weighted_progress_toggle).is_visible(),"Weighted progress toggle not visible"
        assert self.page.locator(self.time_based_progress_toggle).is_visible(),"Time based progress toggle not visible"
        assert self.page.locator(self.create_button).is_visible(),"Create button not visible"

    def insert_project_details(self):
        self.project_name = self.faker.word()
        category_name = self.faker.word()
        notes = self.faker.sentence()
        client = self.faker.name()
        start_date = date.today()
        end_date = start_date + timedelta(days=random.randint(1, 60))
        end_date_str = end_date.strftime("%Y-%m-%d")
        self.page.locator(self.name_input).fill(self.project_name)
        self.page.locator(self.project_color).click()
        self.random_color_select()
        self.page.locator(self.status_dropdown_button).click()
        self.wait_for_timeout(1000)
        random_status = random.choice(self.page.locator("div.ant-select-item").all())
        random_status.click()
        self.page.locator(self.health_dropdown_button).click()
        self.wait_for_timeout(1000)
        random_health = random.choice(self.page.locator(self.drop_down_menu).nth(1).locator("div.ant-select-item").all())
        random_health.click()
        category_dropdown = self.page.locator(self.category_dropdown_button)
        category_dropdown.click()
        self.wait_for_timeout(1000)
        random_category = random.choice(self.page.locator(self.drop_down_menu).nth(2).locator("div.ant-select-item").all())
        random_category_name = random_category.inner_text().strip()
        random_category.click()
        assert self.page.get_by_role("dialog").get_by_title(random_category_name), "Category not selected"
        self.page.get_by_role("dialog").get_by_title(random_category_name).click()
        self.page.get_by_role("button", name = "plus New Category").click()
        category_input = self.page.get_by_role("textbox", name = "Enter a name for the category")
        category_input.fill(category_name)
        category_input.press("Enter")
        self.wait_for_timeout(1000)
        self.page.locator(self.notes_input).fill(notes)
        self.page.locator(self.client_input).fill(client)
        self.page.get_by_text("+ Add " + client + " as client").click()
        self.page.locator(self.project_manager_add_button).click()
        project_manager = random.choice(self.page.locator(self.project_manager_list).all())
        project_manager.click()
        self.page.locator(self.start_date_input).click()
        self.page.get_by_text("Today", exact=True).click()
        self.page.locator(self.end_date_input).fill(end_date_str)
        working_days = self.page.locator(self.working_days_input)
        working_days.click()
        working_days.clear()
        working_days.fill(str(random.randint(1, 60)))
        man_days = self.page.locator(self.man_days_input)
        man_days.clear()
        man_days.fill(str(random.randint(1, 60)))
        pass

    def click_create_project(self):
        self.page.locator(self.create_button).click()
        self.wait_for_timeout(4000)
        assert self.page.get_by_role("heading", name=self.project_name).is_visible(), "Project not created"

    def verify_hours_per_day(self):
        hours_per_day = self.page.locator(self.hours_per_day_input)
        hours_per_day.clear()
        hours_per_day.fill("25")
        validation_message = self.page.get_by_text("Hours per day must be a number between 1 and 24")
        assert validation_message.is_visible(), "Validation message for hours per day not visible"

    def verify_project_name_validation(self):
        self.page.locator(self.create_button).click()
        self.wait_for_timeout(1000)
        validation_message = self.page.get_by_text("Please enter a name")
        assert validation_message.is_visible(), "Validation message for project name not visible"