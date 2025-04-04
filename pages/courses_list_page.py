from compoents.courses.course_view_component import CourseViewComponent
from compoents.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
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
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier='courses-list')
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'

        )
