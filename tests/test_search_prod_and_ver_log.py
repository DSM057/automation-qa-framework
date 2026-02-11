from playwright.sync_api import Page
from pages.products_page import ProductPage
from pages.signin_register_page import SigninRegisterPage
from pages.cart_page import CartPage

def test_search_ver_cart(page : Page , start_home):
    product = ProductPage(page)
    cart = CartPage(page)
    login = SigninRegisterPage(page)
    search_prod = "Blue Top"
    email = "wladek12345@gmail.com"
    password = "qwerty123"


    start_home.click_products_button()
    product.check_url()
    product.fill_search(search_prod)
    product.verify_search_text()
    product.verify_items(search_prod)
    product.hover_and_click_prod(0)
    product.view_cart()
    cart.check_prod(search_prod)
    cart.goto_singin()
    login.fill_login_email(email)
    login.fill_login_password(password)
    login.click_cart_link()
    cart.check_prod(search_prod)
