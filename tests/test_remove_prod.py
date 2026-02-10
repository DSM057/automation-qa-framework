from playwright.sync_api import Page ,expect
from pages.home_page import HomePage
from pages.cart_page import CartPage


def test_remove_prod(page : Page , start_home):
    home = HomePage(page)
    cart = CartPage(page)
    
    start_home.add_product()
    home.click_view_cart()
    expect(page).to_have_url(cart.url)
    cart.click_delete_prod()
    cart.check_zero_prod()
