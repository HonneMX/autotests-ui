from compoents.base_component import BaseComponent
from playwright.sync_api import Page, expect

from compoents.courses.course_view_menu_component import CourseViewMenuComponent


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.widget_title = page.get_by_test_id('course-widget-title-text')
        self.widget_image = page.get_by_test_id('course-preview-image')
        self.widget_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.widget_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.widget_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

    def check_visible(
            self,
            index: int,
            widget_title: str,
            max_score: str,
            min_score: str,
            estimation_time: str
    ):
        expect(self.widget_image.nth(index)).to_be_visible()

        expect(self.widget_title.nth(index)).to_be_visible()
        expect(self.widget_title.nth(index)).to_have_text(widget_title)

        expect(self.widget_max_score_text.nth(index)).to_be_visible()
        expect(self.widget_max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.widget_min_score_text.nth(index)).to_be_visible()
        expect(self.widget_min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.widget_estimated_time_text.nth(index)).to_be_visible()
        expect(self.widget_estimated_time_text.nth(index)).to_have_text(f"Estimated time: {estimation_time}")
