from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.signin_register_page import SigninRegisterPage
from pages.register_form_page import RegisterFormPage
from pages.checkout_page import CheckoutPage

def test_registration_with_checkout(page: Page, start_home):
    home = HomePage(page)
    cart = CartPage(page)
    signin = SigninRegisterPage(page)
    registration_form = RegisterFormPage(page)
    checkout = CheckoutPage(page)

    name = "Vladyslav"
    last_name = "Chornii"
    address1 = "NewYork Street 573"
    city = "NewYork"
    state = "NewYork"
    postcode = "10001"
    country = "United States"
    number = "+123456789"
    address2 = "NewYork Street 572"
    card_name = "Petro Kovalev"
    card = "1234123412341234"
    cvc = "123"
    month = "03"
    year = "2026"

    start_home.go_to_signup_login()
    signin.fill_name(name)
    signin.fill_email("vladyslav77@yahoo.com")
    signin.click_signup_button()
    registration_form.check_new_user_signup_visible()
    registration_form.male_or_female()
    registration_form.fill_name(name)
    registration_form.fill_password("qwerty12345")
    registration_form.fill_hb_date("12" , "March" , "2005")
    registration_form.click_checkboxes()
    registration_form.fill_fullname(name , last_name)
    registration_form.fill_company("Google")
    registration_form.fill_address(address1 , address2)
    registration_form.fill_location(country, city , state , postcode)
    registration_form.fill_number(number)
    registration_form.create_account_click()
    registration_form.continue_and_check()
    home.check_correct_user(name)
    home.add_product()
    home.click_cart_button()
    expect(page).to_have_url(cart.url)
    expect(page.locator("section#cart_items")).to_be_visible()
    cart.click_to_proceed()
    checkout.expect_address_delivery(name , last_name , address1 , city , state ,postcode , country , number , address2)
    checkout.check_review("Blue Top")
    checkout.fill_description()
    checkout.click_place_order()
    if checkout.ads_button.count() > 0:
        checkout.close_add()
    checkout.fill_card_info(card_name , card , cvc , month , year)
    checkout.check_success_message()
    checkout.delete_account()


    

    






  
    