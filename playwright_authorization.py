from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    #//div[@data-testid="login-form-email-input"]//input

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//input')
    email_input.fill('user.name@gmail.com')

    #//div[@data-testid="login-form-password-input"]//input

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//input')
    password_input.fill('Password')

    #//button[@data-testid='login-page-login-button']

    login_button = page.locator("//button[@data-testid='login-page-login-button']")
    login_button.click()

    #//div[@data-testid='login-page-wrong-email-or-password-alert']

    wrong_email_or_password_alert = page.locator("//div[@data-testid='login-page-wrong-email-or-password-alert']")
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
    page.wait_for_timeout(5000)