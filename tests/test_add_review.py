from playwright.sync_api import Page
from pages.products_page import ProductPage

def test_review(page : Page , start_home):
    product = ProductPage(page)
    name = "Vladyslav"
    email = "wladek12345@gmail.com"
    review = "Lorem 123"

    start_home.click_products_button()
    product.check_url()
    product.click_view_first()
    product.check_review_text()
    product.fill_review_form(name , email, review)
    product.check_successful_review()
