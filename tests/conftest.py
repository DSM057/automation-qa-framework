import pytest
from playwright.sync_api import Page , expect  
from pages.home_page import HomePage
from pages.register_form_page import RegisterFormPage
from pages.signin_register_page import SigninRegisterPage

@pytest.fixture()
def creating_user(page):
    
    home = HomePage(page)
    register = RegisterFormPage(page)
    signin = SigninRegisterPage(page)

    name = "Vladyslav"
    password =  "qwerty54321"
    email = "vladyyslav321@gmail.com"

    home.open()
    home.consent_action()
    home.check_homepage_url()
    home.go_to_signup_login()
    signin.check_new_user_signup_visible()
    signin.fill_name(name)
    signin.fill_email(email)
    signin.click_signup_button()
    register.check_new_user_signup_visible()
    register.male_or_female()
    register.fill_name(name)
    register.fill_password(password)
    register.fill_hb_date("12" , "March" , "2005")
    register.click_checkboxes()
    register.fill_fullname("Vladyslav" , "Chornii")
    register.fill_company("Google")
    register.fill_address("NewYork Street 573" , "NewYork Street 572")
    register.fill_location("United States", "NewYork" , "NewYork" , "10001")
    register.fill_number("+123456789")
    register.create_account_click()
    register.continue_and_check()
    home.check_correct_user(name)
    home.logout_click()

    yield {"name": name, "email": email, "password": password}

    
@pytest.fixture()
def start_home(page):
    home = HomePage(page)
    home.open()

    if home.consent_button.count() > 0 :
        home.consent_action()

    home.check_homepage_url()
    return home

    

