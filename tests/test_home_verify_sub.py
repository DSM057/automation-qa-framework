from playwright.sync_api import Page
from pages.home_page import HomePage

def test_verify_sub(page : Page):
    home = HomePage(page)
    email = "testmail@gmail.com"

    home.open()
    if home.consent_button.count() > 0:
        home.consent_action()
    home.check_homepage_url()
    home.scroll_to_footer()
    home.check_sub()
    home.fill_email_sub(email)
    home.click_sub_button()
    home.check_successful_sub()
    