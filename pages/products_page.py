from playwright.sync_api import Page , expect

class ProductPage:
    def __init__(self,page : Page):
        self.page = page
        self.url = "https://automationexercise.com/products"
        self.all_poduct_text = page.get_by_text("All Products")
        self.view_first_product = page.locator('a[href="/product_details/1"]')
        #self.view_first = page.get_by_role("link" , name = "View Product").nth(0)
        self.search_input = page.get_by_role("textbox" , name = "Search Product")
        self.search_button = page.locator("button#submit_search")
        self.search_text = page.get_by_text("SEARCHED PRODUCTS")
        self.view_cart_button = page.get_by_text("View Cart")

        self.continue_shopping_button = page.get_by_role("button" , name="Continue Shopping" , exact=True)
        self.brand_bar = page.locator("div.brands_products")
        self.polo_brand = page.locator("div.brands_products").get_by_text("POLO")
        self.visible_prod = page.locator('div.features_items div.col-sm-4')
        self.hnm_brand = page.locator("div.brands_products").get_by_text("H&M")
        self.review_text = page.get_by_text("Write Your Review")

        self.name_review = page.get_by_role("textbox" , name = "Your Name")
        self.email_review = page.get_by_role("textbox" , name = "Email Address" , exact = True)
        self.text_review = page.get_by_role("textbox" , name = "Add Review Here!")
        self.review_submit_button = page.get_by_role("button" , name = "Submit")
        self.end_review_text = page.get_by_text("Thank you for your review.")

        

       

        
        
    def get_item_price(self,number):
        return self.page.locator('div.productinfo.text-center h2').nth(number).inner_text()


    def check_url(self):
        expect(self.page).to_have_url(self.url)

    def check_all_products(self):
        expect(self.all_poduct_text).to_be_visible()

    def click_view_first(self):
        self.view_first_product.click()

    def hover_and_click_prod(self , n):
        self.hover_prod = self.page.locator('div.productinfo.text-center').nth(n)
        self.hover_add = self.hover_prod.get_by_text("Add to cart")
        self.hover_prod.hover()
        self.hover_add.click()


    def view_cart(self):
        self.view_cart_button.click()
       

    def click_continue_shopping(self):
        self.continue_shopping_button.click()

    def check_details(self , product_name , category , price , availability , condition , brand):
        expect(self.page.get_by_text(product_name)).to_be_visible()
        expect(self.page.get_by_text(category)).to_be_visible()
        expect(self.page.get_by_text(price)).to_be_visible()
        expect(self.page.get_by_text(availability)).to_be_visible()
        expect(self.page.get_by_text(condition)).to_be_visible()
        expect(self.page.locator("div.product-information").get_by_text("Polo")).to_be_visible()

    def fill_search(self,product):
        self.search_input.fill(product)
        self.search_button.click()

    def verify_search_text(self):
        expect(self.search_text).to_be_visible()
        
    def verify_items(self,product):
        self.all_products = self.page.locator("div.col-sm-4").filter(has_text=product)
        count = self.all_products.count()
        if count > 0:
            print(count , "elements found")
            for i in range(count):
                expect(self.all_products.nth(i)).to_be_visible()      
        else:
            print("Elements not found") 

    def check_brand_bar(self):
        expect(self.brand_bar).to_be_visible()

    
    def click_polo_brand(self):
        self.polo_brand.click()

    def check_brand_polo(self):
        polo_url ="https://automationexercise.com/brand_products/Polo"
        
        prod_count = self.visible_prod.count()

        for i in range(prod_count):
             expect(self.visible_prod.nth(i)).to_be_visible()


        expect(self.page).to_have_url(polo_url)
        # expect(self.visible_prod).to_be_visible()

    def click_brand_hnm(self):
        self.hnm_brand.click()

    def check_hnm_brand(self):
        url_hnm = "https://automationexercise.com/brand_products/H&M"
        prod_count = self.visible_prod.count()

        for i in range(prod_count):
            expect(self.visible_prod.nth(i)).to_be_visible()

        expect(self.page).to_have_url(url_hnm)

    def check_review_text(self):
        expect(self.review_text).to_be_visible()

    def fill_review_form(self , name , email, review):
        self.name_review.fill(name)
        self.email_review.fill(email)
        self.text_review.fill(review)
        self.review_submit_button.click()

    def check_successful_review(self):
        expect(self.end_review_text).to_be_visible()