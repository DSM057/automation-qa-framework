from playwright.sync_api import Page , expect
from pages.home_page import HomePage


def test_view_category(page : Page , start_home):
    
    home = HomePage(page)

    start_home.click_women_category(1)
    home.click_men_category()
    




