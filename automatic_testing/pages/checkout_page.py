from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay


class CheckoutPage(BasePage):
    ADDRESS_SELECT = (By.CSS_SELECTOR, "select#address, .address-selector")
    CARRIER_OPTION = (By.CSS_SELECTOR, "input[name='delivery_option']")
    PAYMENT = (By.CSS_SELECTOR, "input[name='payment-option'][value*='cod'], label[for*='payment-cod']")
    TERMS_CHECK = (By.NAME, "conditions_to_approve[terms-and-conditions]")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button#payment-confirmation, button.place-order, button.btn-primary")


    def select_address(self):
        try:
            self.safe_click(self.ADDRESS_SELECT)
            short_delay()
        except:
            pass


    def choose_carrier(self):
        try:
            carriers = self.driver.find_elements(*self.CARRIER_OPTION)
            if carriers:
                carriers[0].click()
                short_delay()
        except:
            pass


    def choose_payment(self):
        self.safe_click(self.PAYMENT)


    def accept_terms(self):
        self.driver.find_element(*self.TERMS_CHECK).click()
        short_delay()


    def place_order(self):
        self.safe_click(self.PLACE_ORDER_BUTTON)
        short_delay()