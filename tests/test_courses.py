from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
# Работа над ошибками.
# @pytest.mark.usefixtures(
#     "initialize_browser_state"
# )
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

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
    page.wait_for_timeout(5000)
