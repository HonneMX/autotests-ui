from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    # Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполнит поле "Email" значением "user.name@gmail.com"
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Заполнит поле "Username" значением "username"

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Заполнит поле "Password" значением "password"

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard" registration-page-registration-button
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()
    registration_button.click()

    # Проверит, что на странице "Dashboard" отображается заголовок "Dashboard" dashboard-toolbar-title-text
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_have_text('Dashboard')

    page.wait_for_timeout(5000)