from playwright.sync_api import expect , Page
from pages.home_page import HomePage

def test_testcase(page : Page):
    home = HomePage(page)
    
    home.open()
    if home.consent_button.count() > 0:
        home.consent_action()
    home.check_homepage_url()
    home.testcase_click()
    expect(page).to_have_url("https://automationexercise.com/test_cases")