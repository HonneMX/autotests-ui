from compoents.views.empty_view_component import EmptyViewComponent
from navigation.navbar_component import NavbarComponent
from navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier='courses-list')

        self.courses_list_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.course_widget_title = page.get_by_test_id('course-widget-title-text')
        self.course_widget_image = page.get_by_test_id('course-preview-image')
        self.course_widget_max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_widget_min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_widget_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')


    def check_courses_list_title(self):
        expect(self.courses_list_title).to_be_visible()
        expect(self.courses_list_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'

        )

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.check_visible_create_course_button()
        self.create_course_button.click()

    def check_visible_course_card(
            self,
            index: int,
            widget_title: str,
            max_score: str,
            min_score: str,
            estimation_time: str
    ):
        expect(self.course_widget_image.nth(index)).to_be_visible()

        expect(self.course_widget_title.nth(index)).to_be_visible()
        expect(self.course_widget_title.nth(index)).to_have_text(widget_title)

        expect(self.course_widget_max_score.nth(index)).to_be_visible()
        expect(self.course_widget_max_score.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.course_widget_min_score.nth(index)).to_be_visible()
        expect(self.course_widget_min_score.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.course_widget_estimated_time.nth(index)).to_be_visible()
        expect(self.course_widget_estimated_time.nth(index)).to_have_text(f"Estimated time: {estimation_time}")

    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_menu_button.nth(index)).to_be_visible()
        self.course_edit_menu_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_button.nth(index)).to_be_visible()
        self.course_delete_menu_button.nth(index).click()
