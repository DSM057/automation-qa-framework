from playwright.sync_api import expect , Page


class SigninRegisterPage:
    def __init__(self , page: Page):
        self.page = page
        self.new_user_messange = page.get_by_text("New User Signup!")
        self.name_input = page.get_by_role("textbox" , name = "Name")
        self.email_input = page.locator("form").filter(has_text = "Signup").get_by_role("textbox" , name="Email Address")
        self.button_signup = page.get_by_role("button" , name="Signup")
        self.login_text = page.get_by_text("Login to your account")
        self.email_login =  page.locator('[data-qa="login-email"]')
        self.email_password = page.get_by_role("textbox" , name="Password")
        self.login_button = page.get_by_role("button" , name = "Login" , exact = True)
        self.delete_account = page.get_by_role("link" , name = "Delete Account")
        self.delete_text = page.get_by_text("ACCOUNT DELETED!")
        self.login_text = page.get_by_text("Login to your account")
        self.incorrect_password = page.get_by_text("Your email or password is incorrect!")
        self.login_link = ("https://automationexercise.com/login")
        self.email_exist = page.get_by_text("Email Address already exist!")
        self.cart_link = page.get_by_role("link" , name="Cart")


    def check_new_user_signup_visible(self):
        expect(self.new_user_messange).to_be_visible()

    def fill_name(self , name : str):
        self.name_input.fill(name)

    def fill_email(self , email : str):
        self.email_input.fill(email)

    def click_signup_button(self):
        self.button_signup.click()

    def login_text_check(self):
        expect(self.login_text).to_be_visible()

    def fill_login_email(self,email : str):
        self.email_login.fill(email)

    def fill_login_password(self,password : str):
        self.email_password.fill(password)

    def login_button_click(self):
        self.login_button.click()

    def check_login_text(self):
        expect(self.login_text).to_be_visible()

    def check_inccorect_message(self):
        expect(self.incorrect_password).to_be_visible()

    def check_login_link(self):
        expect(self.page).to_have_url(self.login_link)

    def expect_email_exist(self):
        expect(self.email_exist).to_be_visible()

    def click_cart_link(self):
        self.cart_link.click()

   