from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_add_to_cart_from_rec(page: Page , start_home):
    home = HomePage(page)
    cart = CartPage(page)
    
    product_name = "Stylish Dress"

    start_home.scroll_to_reccomended()
    home.add_product_from_reccomended()
    home.click_view_cart()
    cart.check_prod(product_name)
