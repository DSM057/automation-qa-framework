from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.signin_register_page import SigninRegisterPage
from pages.checkout_page import CheckoutPage

def test_registration_with_checkout(page: Page, start_home):
    home = HomePage(page)
    cart = CartPage(page)
    signin = SigninRegisterPage(page)
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
    signin.fill_login_email("wladek123456@gmail.com")
    signin.fill_login_password("qwerty123")
    signin.login_button_click()
    home.check_correct_user(name)
    home.add_product()
    home.click_view_cart()
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



    

    






  
    