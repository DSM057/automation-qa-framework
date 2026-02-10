from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.signin_register_page import SigninRegisterPage


def test_reg_invalid(page : Page):
    home = HomePage(page)
    login = SigninRegisterPage(page)
    name = "Vladyslav"
    email = "wladek12345@gmail.com"
    


    home.open()
    if home.consent_button.count() > 0:
        home.consent_action()
    home.check_homepage_url()
    home.go_to_signup_login()
    login.check_new_user_signup_visible()
    login.fill_name(name)
    login.fill_email(email)
    login.click_signup_button()
    login.expect_email_exist()