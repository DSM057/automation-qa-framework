from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.contact_us_page import ContactUs


def test_contact_us_form(page : Page):
    home = HomePage(page)
    contact = ContactUs(page)
    name = "Vladyslav"
    email = "wladek12345@gmail.com"
    subject = "Shoes"

    home.open()
    if home.consent_button.count() > 0:
        home.consent_action()
    home.check_homepage_url()
    home.contact_us_click()
    contact.check_get_in_touch()
    contact.fill_info(name , email , subject)
    contact.fill_message()
    contact.upload_files()
    contact.click_submit()
    contact.check_successful_text()
    contact.go_to_homepage()

