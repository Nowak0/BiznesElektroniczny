from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import random_string, short_delay


class AccountPage(BasePage):
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".user-info a[href*='my-account'], .register-link, a.create-account")
    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirmation")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button#submit-account, button[type='submit']")


    def open_registration(self):
        self.safe_click(self.CREATE_ACCOUNT_BUTTON)


    def register_new_user(self):
        self.open_registration()
        short_delay()
        first = "Test"
        last = "User"
        email = random_string(prefix="test") + "@test.com"
        password = random_string(n=10)

        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)
        short_delay()
        self.safe_click(self.REGISTER_BUTTON)
        short_delay()

        return {"first": first, "last": last, "email": email, "password": password}
