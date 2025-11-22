from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import random_string, short_delay


class AccountPage(BasePage):
    CREATE_ACCOUNT_PAGE = "https://monocerus.pl/logowanie?create_account=1"
    LOGIN_PAGE = "https://monocerus.pl/logowanie"
    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    CONFIRMATION = (By.NAME, "agreement_1")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


    def open_registration(self):
        self.open(self.CREATE_ACCOUNT_PAGE)


    def open_login_page(self):
        self.open(self.LOGIN_PAGE)


    def register_new_user(self):
        self.open_registration()
        short_delay(2,3)
        first = "Michael"
        last = "Jordan"
        email = "psscarpeta@gmail.com"
        password = "qwerty65"
        # email = random_string(prefix="test") + "@test.com"
        # password = random_string(n=10)

        try:
            self.driver.find_element(*self.FIRST_NAME).send_keys(first)
            short_delay()
            self.driver.find_element(*self.LAST_NAME).send_keys(last)
            short_delay()
            self.driver.find_element(*self.EMAIL).send_keys(email)
            short_delay()
            self.driver.find_element(*self.PASSWORD).send_keys(password)
            short_delay()
            self.driver.find_element(*self.CONFIRMATION).click()
            short_delay()
            self.safe_click(self.SUBMIT_BUTTON)
            short_delay()
        except Exception as e:
            raise Exception(f"Error registering new user: {e}")

        return {"first": first, "last": last, "email": email, "password": password}


    def login(self, email, password):
        self.open_login_page()
        short_delay(2,3)

        try:
            self.driver.find_element(*self.EMAIL).send_keys(email)
            short_delay()
            self.driver.find_element(*self.PASSWORD).send_keys(password)
            short_delay()
            self.safe_click(self.SUBMIT_BUTTON)
            short_delay()
        except Exception as e:
            raise Exception(f"Error logging in: {e}")

        return {"email": email, "password": password}

