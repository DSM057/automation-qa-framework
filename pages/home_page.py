from playwright.sync_api import expect , Page

class HomePage:
    def __init__(self , page: Page):
        self.page = page
        self.url = ("https://automationexercise.com/")
        self.consent_button = page.get_by_role("button", name="Consent")
        self.signup_login_link = page.get_by_role("link" , name = "Signup / Login")
        self.delete_link = page.get_by_role("link" , name = "Delete Account")
        self.account_delete_message = page.get_by_text("ACCOUNT DELETED!")
        self.continue_button = page.get_by_role("link" , name = "Continue")
        self.logout_link = page.get_by_role("link" , name = "Logout")
        self.contact_us = page.get_by_role("link" , name = "Contact us")
        self.test_case = page.get_by_role("link" , name = "Test Cases" , exact = True)
        # self.test_test_case = page.locator("div.shop-menu").get_by_role("link" , name = "Test Cases")
        self.product_button = page.get_by_role("link" , name = "Products")
        self.footer = page.locator('footer')
        self.sub_text = page.get_by_text("SUBSCRIPTION")
        self.email_sub = page.locator("footer").get_by_role("textbox")
        self.sub_button = page.locator("footer").get_by_role("button")
        self.success_sub_text = page.get_by_text("You have been successfully subscribed!")
        self.cart_link = page.get_by_role("link" , name = "Cart")
        self.view_cart = page.get_by_role("link" , name = "View Cart")
        self.view_prod = page.get_by_text("View Product")
        self.first_prod = self.page.locator('div.productinfo.text-center').get_by_text("Add to cart").first
        self.continue_link_message = page.get_by_role("button" , name="Continue Shopping")
        self.left_category_bar = page.locator('#accordian')
        self.woman_category = page.locator('#accordian').get_by_text("WOMEN")
        self.men_category = page.locator('#accordian [href="#Men"]')
        self.type_woman_category = page.locator('#accordian ul li a')
        self.type_men_category = page.locator('div.panel-body').get_by_text("TSHIRTS")
        # self.type_woman_category = page.locator('#accordian').get_by_text("Dress")
        self.men_text = page.get_by_text("Men - Tshirts Products")
        self.reccomended_items_text = page.get_by_text("RECOMMENDED ITEMS")
        self.recomended_products = page.locator('div#recommended-item-carousel div.col-sm-4 [data-product-id="4"]')


    def open(self):
        self.page.goto(self.url)
        
    def consent_action(self):
        self.consent_button.click()

    def check_homepage_url(self):
        expect(self.page).to_have_url(self.url)

    def go_to_signup_login(self):
        self.signup_login_link.click()
        
    def check_correct_user(self , name):
        expect(self.page.get_by_text(f"Logged in as {name}")).to_be_visible()
    
    def delete_acc_click(self):
        self.delete_link.click()

    def check_delete_message(self):
        expect(self.account_delete_message).to_be_visible()

    def continue_button_click(self):
        self.continue_button.click()

    def logout_click(self):
        self.logout_link.click()

    def contact_us_click(self):
        self.contact_us.click()
    
    def testcase_click(self):
        self.test_case.click()

    def click_products_button(self):
        self.product_button.click()

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def check_sub(self):
        expect(self.sub_text).to_be_visible()

    def fill_email_sub(self,email):
        self.email_sub.fill(email)

    def click_sub_button(self):
        self.sub_button.click(timeout=4000)

    def check_successful_sub(self):
        expect(self.success_sub_text).to_be_visible()

    def click_cart_button(self):
        self.cart_link.click()

    def click_view_prod(self):
        self.view_prod.first.click()

    def add_product(self):
        self.first_prod.click()

    def continue_shopping(self):
        self.continue_link_message.click()

    def click_view_cart(self):
        self.view_cart.click()
    
    def click_women_category(self , n):

        women_text = {0 : "Women - Dress Products" , 1 : "Women - Tops Products" , 2 : "Women - Saree Products"}
        dress_text = self.page.get_by_text(women_text[n])


        expect(self.left_category_bar).to_be_visible()
        self.woman_category.click()
        self.type_woman_category.nth(n).wait_for(state="visible")
        self.type_woman_category.nth(n).click()
        prod_map = {0 : 1 , 1 : 2 , 2 : 7}
        expect(dress_text).to_be_visible(timeout=5000)
        expect(self.page).to_have_url(f"https://automationexercise.com/category_products/{prod_map[n]}")

    def click_men_category(self):
        self.men_category.click()
        self.type_men_category.click()
        expect(self.men_text).to_be_visible()
        expect(self.page).to_have_url("https://automationexercise.com/category_products/3")

    def scroll_to_reccomended(self):
        self.reccomended_items_text.scroll_into_view_if_needed()
        expect(self.reccomended_items_text).to_be_visible()

    def add_product_from_reccomended(self):
        self.recomended_products.click()