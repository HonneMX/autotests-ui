from playwright.sync_api import Page, expect

from compoents.courses.create_course_exercise_form_component import CreateCourseExerciseFromComponent
from compoents.views.empty_view_component import EmptyViewComponent
from compoents.views.image_upload_widget_component import ImageUploadWidgetComponent
from navigation.navbar_component import NavbarComponent
from navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)

        self.create_course_form= CreateCourseExerciseFromComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.exercise_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.create_course_form_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_form_estimate_time_input = page.get_by_test_id(
            'create-course-form-estimated-time-input').locator('input')
        self.create_course_form_description_input = page.get_by_test_id('create-course-form-description-input').locator(
            'textarea').first
        self.create_course_form_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator(
            'input')
        self.create_course_form_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator(
            'input')

        self.exercises_form_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercises_form_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_form(
            self,
            title: str,
            estimation_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        expect(self.create_course_form_title_input).to_be_visible()
        expect(self.create_course_form_title_input).to_have_value(title)

        expect(self.create_course_form_estimate_time_input).to_be_visible()
        expect(self.create_course_form_estimate_time_input).to_have_value(estimation_time)

        expect(self.create_course_form_description_input).to_be_visible()
        expect(self.create_course_form_description_input).to_have_value(description)

        expect(self.create_course_form_max_score_input).to_be_visible()
        expect(self.create_course_form_max_score_input).to_have_value(max_score)

        expect(self.create_course_form_min_score_input).to_be_visible()
        expect(self.create_course_form_min_score_input).to_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimation_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form_title_input.fill(title)
        expect(self.create_course_form_title_input).to_have_value(title)

        self.create_course_form_estimate_time_input.fill(estimation_time)
        expect(self.create_course_form_estimate_time_input).to_have_value(estimation_time)

        self.create_course_form_description_input.fill(description)
        expect(self.create_course_form_description_input).to_have_value(description)

        self.create_course_form_max_score_input.fill(max_score)
        expect(self.create_course_form_max_score_input).to_have_value(max_score)

        self.create_course_form_min_score_input.fill(min_score)
        expect(self.create_course_form_min_score_input).to_have_value(min_score)

    def check_visible_exercise_title(self):
        expect(self.exercises_form_title).to_be_visible()
        expect(self.exercises_form_title).to_have_text('Exercises')

    def check_visible_exercise_button(self):
        expect(self.exercises_form_button).to_be_visible()

    def click_exercise_create_button(self):
        self.exercises_form_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercise_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )


