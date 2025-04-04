from compoents.base_component import BaseComponent
from playwright.sync_api import Page, expect


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')

    def click_edit(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.edit_menu_button.nth(index)).to_be_visible()
        self.edit_menu_button.click()

    def click_delete(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.delete_menu_button.nth(index)).to_be_visible()
        self.delete_menu_button.click()