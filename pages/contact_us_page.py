from playwright.sync_api import expect , Page

class ContactUs:
    def __init__(self , page : Page):
        self.page = page
        self.get_in_touch = page.get_by_text("GET IN TOUCH")
        self.name_textbox = page.get_by_role("textbox" , name = "Name")
        self.email_textbox = page.get_by_role("textbox" , name = "Email" , exact = True)
        self.subject_textbox = page.get_by_role("textbox" , name = "Subject")
        self.message_textbox = page.get_by_role("textbox" , name = "Your Message Here")
        self.upload_button = page.locator('input[type="file"]')
        self.submit_button = page.get_by_role("button" , name = "Submit")
        self.confirm_button = page.get_by_role("button" , name = "OK")
        self.successful_text = page.locator('div.status').get_by_text("Success! Your details have been submitted successfully.")
        self.homepage_link = page.locator('a.btn.btn-success')







    def check_get_in_touch(self):
        expect(self.get_in_touch).to_be_visible()

    def fill_info(self , name , email , subject) :
        self.name_textbox.fill(name)
        self.email_textbox.fill(email)
        self.subject_textbox.fill(subject)

    def fill_message(self):
        self.message_textbox.fill("Lorem 1234 Lorem 1234 Nike Adidas")

    def upload_files(self):
        self.upload_button.set_input_files("test_data/nike.jpg")

    def click_submit(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.submit_button.first.click()

    def check_successful_text(self):
        expect(self.successful_text).to_be_visible()

    def go_to_homepage(self):
        self.homepage_link.click()

 