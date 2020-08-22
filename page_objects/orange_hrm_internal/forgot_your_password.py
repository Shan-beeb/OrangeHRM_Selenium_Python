from selenium.webdriver.common.by import By
from selenium import webdriver
from page_objects.page import Page


class ForgotYourPassword:
    # Locators
    orange_hrm_username_input_id = (By.ID, 'securityAuthentication_userName')
    reset_password_button_id = (By.ID, 'btnSearchValues')
    cancel_button_id = (By.ID, 'btnCancel')
    # Web elements
    orange_hrm_username_input = property(lambda self: self.page.find_element(*self.orange_hrm_username_input_id))
    reset_password_button = property(lambda self: self.page.find_element(*self.reset_password_button_id))
    cancel_button = property(lambda self: self.page.find_element(*self.cancel_button_id))

    def __init__(self, page):
        self.page = page

    def wait_for_forgot_password_page(self):
        self.page.wait_for_element(self.orange_hrm_username_input_id)

    def fill_orange_hrm_username(self, username: str):
        self.orange_hrm_username_input.send_keys(username)

    def click_reset_password(self):
        self.reset_password_button.click()

    def click_cancel(self):
        self.cancel_button.click()
