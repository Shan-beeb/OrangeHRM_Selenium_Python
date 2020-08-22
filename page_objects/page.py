from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep


class Page:
    def __init__(self, driver: webdriver, max_time_out=30):
        self.driver = driver
        self.max_time_out = max_time_out
        self.wait = WebDriverWait(driver, self.max_time_out)

    def find_element(self, *element):
        return self.driver.find_element(*element)

    def wait_for_element(self, *element):
        try:
            self.wait.until(EC.element_to_be_clickable(*element))
        except TimeoutException as e:
            print(f"Loading takes more than {self.max_time_out}")
            self.driver.quit()

    def navigate_to_url(self, url: str):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='./browser_drivers/chromedriver.exe')
    page = Page(driver)
    page.navigate_to_url("https://www.google.com")
    sleep(3)
    page.quit_browser()
