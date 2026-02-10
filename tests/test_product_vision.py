from playwright.sync_api import expect , Page
from pages.home_page import HomePage
from pages.products_page import ProductPage


def test_poducts(page : Page):
    home = HomePage(page)
    product = ProductPage(page)
    product_name = "Blue Top" 
    category = "Women > Tops" 
    price = "500" 
    availability = "In Stock" 
    condition = "New" 
    brand = "Polo"

    home.open()
    if home.consent_button.count() > 0:
        home.consent_action()

    home.check_homepage_url()
    home.click_products_button()
    product.check_url()
    product.check_all_products()
    product.click_view_first()
    expect(page).to_have_url("https://automationexercise.com/product_details/1")
    product.check_details(product_name , category , price , availability , condition , brand)