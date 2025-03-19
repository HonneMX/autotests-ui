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
    dashboard_page.check_dashboard_title_visible()
