from playwright.sync_api import Page , expect

class CartPage:
    def __init__(self, page : Page):
        self.page = page
        self.url = "https://automationexercise.com/view_cart"
        self.footer = page.locator("footer")
        self.sub_text = page.get_by_text("SUBSCRIPTION")
        self.email_sub = page.locator("footer").get_by_role("textbox")
        self.sub_button = page.locator("footer").get_by_role("button")
        self.success_sub_text = page.get_by_text("You have been successfully subscribed!")
        self.quantity = page.locator('input#quantity')
        self.add_to_cart = page.get_by_role("button" , name="Add to cart")
        self.sum_view_cart = page.get_by_role("link" , name="View Cart")
        self.proceed_to_checkout = page.locator("a.btn").get_by_text("Proceed To Checkout")
        self.signup_login_link = page.locator('p.text-center a ').get_by_text("Register / Login")
        self.delete_prod_button = page.locator('a.cart_quantity_delete')
        self.cart_sum = page.locator('tbody tr[id^="product-"]')
        self.navigator_login_link = page.get_by_role("link" , name = "Signup / Login")

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()
        

    def click_register(self):
        self.signup_login_link.click()

    def check_sub_text(self):
        expect(self.sub_text).to_be_visible()


    def fill_email_sub(self,email):
        self.detail_prod = self.page.locator("div.product-information")
        # expect(self.detail_prod).to_be_visible()
        self.email_sub.fill(email)

    def click_sub_button(self):
        self.sub_button.click()

    def check_successful_sub(self):
        expect(self.success_sub_text).to_be_visible()

    def fill_quantity(self , number):
        self.quantity.fill(number)

    def click_add_to_cart(self):
        self.add_to_cart.click()

    def click_view_cart(self):
        self.sum_view_cart.click()

    def check_correct_quantity(self , number):
        self.quant_text = self.page.locator("td.cart_quantity").get_by_role("button")
        expect(self.quant_text).to_have_text(number)

    def check_count_prod(self , count):
        self.list_items = self.page.locator('tbody tr[id*="product-"]')
        expect(self.list_items).to_have_count(count)

    def get_item_price(self,number):
        return self.page.locator('tbody tr[id^="product-"] td.cart_price p').nth(number).inner_text()

    def get_quantity(self , number):
       return self.page.locator("td.cart_quantity button[class='disabled']").nth(number).inner_text()
    
    def total_price(self , number):
        return self.page.locator('tbody p.cart_total_price').nth(number).inner_text()
    
    def click_to_proceed(self):
        self.proceed_to_checkout.click()

    def click_delete_prod(self):
        self.delete_prod_button.click()

    def check_zero_prod(self):
        expect(self.cart_sum).not_to_be_visible()


    def check_prod(self, name):
        search_name = self.page.get_by_text(name) 
        expect(search_name).to_be_visible()

    def goto_singin(self):
        self.navigator_login_link.click()