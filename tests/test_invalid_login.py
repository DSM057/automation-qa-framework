from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signin_register_page import SigninRegisterPage

def test_invalid_login(page : Page):
    home = HomePage(page)
    singin = SigninRegisterPage(page)
    home.open()
    home.consent_action()
    home.check_homepage_url()
    home.go_to_signup_login()
    singin.check_login_text()
    singin.fill_login_email("Vladtslav@gmail.com")
    singin.fill_login_password("qwertyyyyyy213543")
    singin.login_button_click()
    singin.check_inccorect_message()