from playwright.sync_api import sync_playwright, Page, expect
import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_succesfull_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email='user@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_page_title()

    # chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    #
    # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.fill('user@gmail.com')
    #
    # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.fill('username')
    #
    # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.fill('password')
    #
    # registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()
    #
    # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()
