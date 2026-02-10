from playwright.sync_api import Page ,expect
from pages.products_page import ProductPage

def test_cart_brand(page : Page , start_home):
    product = ProductPage(page)
    
    start_home.click_products_button()
    product.check_brand_bar()
    product.click_polo_brand()
    product.check_brand_polo()
    product.click_brand_hnm()
    product.check_hnm_brand()


