from playwright.sync_api import sync_playwright, Page, Playwright, expect
import pytest


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    # Работа над ошибками
    # with sync_playwright() as playwright:
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
    context.storage_state(path='browser-state.json')


# Работа над ошибками
# @pytest.fixture(autouse=True)
# def chromium_page_with_state():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(storage_state='browser-state.json')
#         yield context.new_page()

@pytest.fixture
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
