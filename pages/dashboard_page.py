from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.navigation_title_text = page.get_by_test_id('navigation-navbar-app-title-text')
        self.navigation_welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')


        self.dashboard_list_item_title = page.get_by_test_id('dashboard-drawer-list-item-title-text').locator('span')
        self.courses_list_item_title = page.get_by_test_id('courses-drawer-list-item-title-text').locator('span')
        self.logout_button = page.get_by_test_id('logout-drawer-list-item-title-text').locator('span')


        self.dashboard_toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')


        self.student_widget_title = page.get_by_test_id('students-widget-title-text')
        self.student_widget_bar_char = page.get_by_test_id('students-bar-chart')
        self.activities_widget_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_widget_line_char = page.get_by_test_id('activities-line-chart')
        self.courses_widget_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_widget_pie_char = page.get_by_test_id('courses-pie-chart')
        self.scores_widget_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_widget_scatter_char = page.get_by_test_id('scores-scatter-chart')

    def check_dashboard_title_visible(self):
        expect(self.dashboard_toolbar_title).to_be_visible()

