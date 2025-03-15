from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # //div[@data-testid="login-form-email-input"]//input

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # //div[@data-testid="login-form-password-input"]//input

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('Password')

    # //button[@data-testid='login-page-login-button']

    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    # //div[@data-testid='login-page-wrong-email-or-password-alert']

    wrong_email_or_password_alert = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
