from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_cart_verify_sub(page:Page):

    home = HomePage(page)
    cart = CartPage(page)
    email = "vladyslavchor@gmail.com"

    home.open()

    if home.consent_button.count() > 0 :
        home.consent_action()

    home.check_homepage_url()
    home.click_cart_button()
    cart.scroll_to_footer()
    cart.check_sub_text()
    cart.fill_email_sub(email)
    cart.click_sub_button()
    cart.check_successful_sub()

