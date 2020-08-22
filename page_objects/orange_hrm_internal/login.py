import os.path as path

from selenium.webdriver.common.by import By
from selenium import webdriver
from page_objects.page import Page
from time import sleep


class LoginPage:
    # Locators
    orange_hrm_logo_id = (By.ID, 'divLogo')
    username_input_id = (By.ID, 'txtUsername')
    password_input_id = (By.ID, 'txtPassword')
    login_button_id = (By.ID, 'btnLogin')
    forgot_your_password_hyper_link_id = (By.ID, 'forgotPasswordLink')

    # WebElements
    orange_hrm_logo = property(lambda self: self.page.find_element(*self.orange_hrm_logo))
    username_input = property(lambda self: self.page.find_element(*self.username_input_id))
    password_input = property(lambda self: self.page.find_element(*self.password_input_id))
    login_button = property(lambda self: self.page.find_element(*self.login_button_id))
    forgot_your_password_hyper_link = property(
        lambda self: self.page.find_element(*self.forgot_your_password_hyper_link_id))

    def __init__(self, page):
        self.page = page

    def navigate_to_orange_hrm_internal_login_page(self, url: str = ''):
        if not url:
            url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        self.page.navigate_to_url(url)

    def wait_for_login_page(self):
        self.page.wait_for_element(self.username_input_id)

    def fill_username(self, username: str):
        self.username_input.send_keys(username)
        return self

    def fill_password(self, password: str):
        self.password_input.send_keys(password)
        return self

    def click_login(self):
        self.login_button.click()


if __name__ == "__main__":
    driver = webdriver.Chrome(
        executable_path=f'{path.abspath(path.join(__file__, "../../../"))}\\browser_drivers\\chromedriver.exe')
    page = Page(driver)
    loginPage = LoginPage(page)
    loginPage.navigate_to_orange_hrm_internal_login_page()
    loginPage.wait_for_login_page()
    loginPage.fill_username("Admin").fill_password("admin123").click_login()
    sleep(4)
    page.quit_browser()
