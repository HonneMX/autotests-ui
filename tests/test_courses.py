from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # Открыть страницу
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполнить форму регистрации и нажать на кнопку "Registration"
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохранить состояние браузера
        context.storage_state(path='browser-state-playwright-courses.json')

    # Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state-playwright-courses.json')
        page = context.new_page()

        # Открыть страницу "Courses" должна открыться без авторизации
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        # Проверить наличие и текст заголовка "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        # Проверить наличие и текст блока "There is no results"
        result_text_block = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_text_block).to_be_visible()
        expect(result_text_block).to_have_text('There is no results')
