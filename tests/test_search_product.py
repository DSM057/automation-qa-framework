from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.products_page import ProductPage


def test_search_product(page : Page):
    home = HomePage(page)
    product = ProductPage(page)
    name_product = "Women"

    home.open()
    if home.consent_button.count() > 0:
        home.consent_action()

    home.check_homepage_url()
    home.click_products_button()
    product.check_url()
    product.fill_search(name_product)
    product.verify_search_text()
    product.verify_items(name_product)
    
    

