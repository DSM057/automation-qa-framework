from playwright.sync_api import expect , Page

class RegisterFormPage:
    def __init__(self , page: Page):
        self.page = page
        self.starting_new_form = page.get_by_text("ENTER ACCOUNT INFORMATION")
        self.gender_selection = page.locator("input[type='radio']")
        self.name_textbox = page.locator('[data-qa="name"]')
        self.password_textbox = page.get_by_role("textbox" , name = "Password")
        self.day_select = page.locator('select[data-qa="days"]')
        self.month_select = page.locator('select[data-qa="months"]')
        self.year_select = page.locator('select#years')
        self.news_checkbox = page.get_by_role("checkbox" , name = "newsletter")
        self.agree_checkbox = page.locator('input#optin')
        self.first_name = page.locator('input#first_name')
        self.last_name = page.locator('input#last_name')
        self.company = page.locator('input#company')
        self.address1 = page.locator('input#address1')
        self.address2 = page.locator('input#address2')  
        self.country_textbox = page.locator('select[name="country"]')   
        self.state_textbox = page.locator('input#state')
        self.city_textbox = page.locator('input#city')
        self.zipcode_textbox = page.locator('input#zipcode')
        self.number_textbox = page.locator('input#mobile_number')
        self.create_account = page.get_by_role("button" , name = "Create Account")
        self.is_account_create = page.get_by_text("ACCOUNT CREATED!")
        self.continue_button = page.locator('[data-qa="continue-button"]')

    
    def check_new_user_signup_visible(self):
        expect(self.starting_new_form).to_be_visible(timeout=4000)

    def male_or_female(self):
        self.gender_selection.first.click()

    def fill_name(self,name : str):
        self.name_textbox.click()
        self.name_textbox.fill(name)
    
    def fill_password(self,password : str):
        self.password_textbox.click()
        self.password_textbox.fill(password)

    def fill_hb_date(self,day : str,month : str,year : str):
        self.day_select.select_option(day)
        self.month_select.select_option(month)
        self.year_select.select_option(year)

    def click_checkboxes(self):
        self.news_checkbox.click()
        self.agree_checkbox.click()

    def fill_fullname(self, name : str , surname : str):
        self.first_name.fill(name)
        self.last_name.fill(surname)

    def fill_company(self , company : str):
        self.company.fill(company)

    def fill_address(self , address1 : str , address2 : str):
        self.address1.fill(address1)
        self.address2.fill(address2)

    def fill_location(self , country : str , state : str , city : str , zipcode : str):
        self.country_textbox.select_option(country)
        self.state_textbox.fill(state)
        self.city_textbox.fill(city)
        self.zipcode_textbox.fill(zipcode)
        
    def fill_number(self,number : str):
        self.number_textbox.fill(number)

    def create_account_click(self):
        self.create_account.click()
  
    def continue_and_check(self):
        expect(self.is_account_create).to_be_visible()
        self.continue_button.click()
   
   