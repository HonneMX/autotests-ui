from pages.dashboard_page import DashboardPage
import  pytest

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_display(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.navbar.check_visible('username')
    dashboard_page_with_state.check_dashboard_title_visible()
    dashboard_page_with_state.check_scores_widget_visible()
    dashboard_page_with_state.check_courses_widget_visible()
    dashboard_page_with_state.check_activities_widget_visible()
    dashboard_page_with_state.check_students_widget_visible()

