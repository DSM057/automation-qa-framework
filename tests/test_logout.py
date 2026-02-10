from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.signin_register_page import SigninRegisterPage

def test_logout(page : Page):
    home = HomePage(page)
    login = SigninRegisterPage(page)
    email = "wladek12345@gmail.com"
    password = "qwerty123"
    user = "Vladyslav"


    home.open()
    home.consent_action()
    home.check_homepage_url()
    home.go_to_signup_login()
    login.login_text_check()
    login.fill_login_email(email)
    login.fill_login_password(password)
    login.login_button_click()
    home.check_correct_user(user)
    home.logout_click()
    login.check_login_link()
