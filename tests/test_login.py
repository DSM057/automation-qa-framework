from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.signin_register_page import SigninRegisterPage

def test_login(page : Page , creating_user):
    home = HomePage(page)
    singin = SigninRegisterPage(page)
    home.open()
    if home.consent_button.count() > 0:
        home.consent_button.click()
    home.check_homepage_url()
    home.go_to_signup_login()
    singin.login_text_check()
    singin.fill_login_email(creating_user["email"])
    singin.fill_login_password(creating_user["password"])
    singin.login_button_click()
    home.check_correct_user(creating_user["name"])
    home.delete_acc_click()
    home.check_delete_message()
    
