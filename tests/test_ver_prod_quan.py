from playwright.sync_api import Page 
from pages.cart_page import CartPage


def test_prod_quan(page : Page , start_home):
    cart = CartPage(page)
    quantity = "4"

    start_home.click_view_prod()
    cart.fill_quantity(quantity)
    cart.click_add_to_cart()
    cart.click_view_cart()
    cart.check_correct_quantity(quantity)
    