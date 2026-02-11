from playwright.sync_api import Page , expect

class CheckoutPage:
    def __init__(self , page:Page):
        self.page = page
        self.first_last_name= page.locator('ul#address_delivery li.address_firstname.address_lastname') 
        self.address = page.locator('ul#address_delivery li.address_address1.address_address2').nth(1)
        self.address2 = page.locator('ul#address_delivery li.address_address1.address_address2').nth(2)
        self.city_state_postcode = page.locator('ul#address_delivery li.address_city.address_state_name.address_postcode')
        self.contry = page.locator('ul#address_delivery li.address_country_name')
        self.number = page.locator('ul#address_delivery li.address_phone')
        self.discription = page.locator('div#ordermsg').get_by_role("textbox")
        self.place_order = page.get_by_role("link" , name = "Place Order")
        self.name_on_card = page.locator("[data-qa='name-on-card']")
        self.card_num = page.locator("[data-qa='card-number']")
        self.card_cvc = page.locator("[data-qa='cvc']")
        self.card_month = page.locator("[data-qa='expiry-month']")
        self.card_year = page.locator("[data-qa='expiry-year']")
        self.pay_button = page.get_by_role("button" , name = "Pay and Confirm Order")
        self.successful_order = page.get_by_text("Congratulations! Your order has been confirmed!")
        self.delete_link = page.get_by_role("link" , name = "Delete Account")
        self.delete_message = page.get_by_text("ACCOUNT DELETED!")
        self.continue_button = page.get_by_role("link" , name = "Continue")
        self.ads_button = page.get_by_role("button" , name = "Close")




    def expect_address_delivery(self, first_name : str , last_name : str , address1 : str , city : str , state : str ,postcode : str , country : str , number : str  , address2 = None ):
        expect(self.first_last_name).to_contain_text(first_name)
        expect(self.first_last_name).to_contain_text(last_name)
        expect(self.address).to_contain_text(address1)
        expect(self.address2).to_contain_text(address2)
        expect(self.city_state_postcode).to_contain_text(city)
        expect(self.city_state_postcode).to_contain_text(state)
        expect(self.city_state_postcode).to_contain_text(postcode)
        expect(self.contry).to_contain_text(country)
        expect(self.number).to_contain_text(number)


    def check_review(self , nameprod : str):
        review = self.page.get_by_text(nameprod)
        expect(review).to_be_visible()

    def fill_description(self):
        self.discription.fill("Lorem 123123123213")

    def click_place_order(self):
        self.place_order.click()

    def fill_card_info(self, name : str , card : str , cvc : str , month : str , year : str):
        self.name_on_card.fill(name)
        self.card_num.fill(card)
        self.card_cvc.fill(cvc)
        self.card_month.fill(month)
        self.card_year.fill(year)
        self.pay_button.click(timeout=10000)

    def check_success_message(self):
        expect(self.successful_order).to_be_visible()

    def delete_account(self):
        self.delete_link.click()
        expect(self.delete_message).to_be_visible()
        self.continue_button.click()

    def close_add(self):
        self.ads_button.click()