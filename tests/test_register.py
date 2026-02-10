from playwright.sync_api import expect , Page
from pages.home_page import HomePage
from pages.signin_register_page import SigninRegisterPage
from pages.register_form_page import RegisterFormPage
import time




def test_register_page(page: Page):
    name = "Vladyslav"
    home = HomePage(page)
    signin = SigninRegisterPage(page)
    registration_form = RegisterFormPage(page)
    home.open()
    home.consent_action()
    home.check_homepage_url()
    home.go_to_signup_login()
    signin.check_new_user_signup_visible()
    signin.fill_name(name)
    signin.fill_email("vladyslav22@yahoo.com")
    signin.click_signup_button()
    registration_form.check_new_user_signup_visible()
    registration_form.male_or_female()
    registration_form.fill_name(name)
    registration_form.fill_password("qwerty12345")
    registration_form.fill_hb_date("12" , "March" , "2005")
    registration_form.click_checkboxes()
    registration_form.fill_fullname("Vladyslav" , "Chornii")
    registration_form.fill_company("Google")
    registration_form.fill_address("NewYork Street 573" , "NewYork Street 572")
    registration_form.fill_location("United States", "NewYork" , "NewYork" , "10001")
    registration_form.fill_number("+123456789")
    registration_form.create_account_click()
    registration_form.continue_and_check()
    home.check_correct_user(name)
    home.delete_acc_click()
    home.check_delete_message()
    home.continue_button_click()


  
    
    