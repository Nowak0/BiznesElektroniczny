from pydoc import safeimport

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay, random_string


class CheckoutPage(BasePage):
    CHECKOUT_PAGE_LINK = "https://localhost/pl/zamówienie"
    ADDRESS_SELECT = (By.NAME, "address1")
    POSTAL_CODE_SELECT = (By.NAME, "postcode")
    CITY_SELECT = (By.NAME, "city")
    PHONE_SELECT = (By.NAME, "phone")
    CARRIER_OPTION = (By.CSS_SELECTOR, ".row.delivery-option.js-delivery-option")
    PAYMENT_OPTIONS = (By.CSS_SELECTOR, ".payment-option")
    TERMS_CHECK = (By.CSS_SELECTOR, "input[name='conditions_to_approve[terms-and-conditions]']")
    ADDRESS_BUTTON = (By.NAME, "confirm-addresses")
    CARRIER_BUTTON = (By.NAME, "confirmDeliveryOption")
    PAYMENT_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], .btn.btn-primary.center-block")
    PAYMENT_TYPE = "gotówk"


    def open_page(self):
        self.open(self.CHECKOUT_PAGE_LINK)
        short_delay(2,3)


    def select_delivery_info(self, address, postcode, city, phone):
        try:
            self.driver.find_element(*self.ADDRESS_SELECT).send_keys(address)
            short_delay()
            self.driver.find_element(*self.POSTAL_CODE_SELECT).send_keys(postcode)
            short_delay()
            self.driver.find_element(*self.CITY_SELECT).send_keys(city)
            short_delay()
            self.driver.find_element(*self.PHONE_SELECT).send_keys(phone)
            short_delay()
        except Exception as e:
            # raise Exception(f"Error: {e}")
            pass

        self.driver.find_element(*self.ADDRESS_BUTTON).click()
        short_delay()

    def choose_carrier(self):
        try:
            carriers = self.driver.find_elements(*self.CARRIER_OPTION)
            if not carriers:
                raise NoSuchElementException()

            carriers[0].click()
            short_delay()
            self.driver.find_element(*self.CARRIER_BUTTON).click()
            short_delay()

        except Exception as e:
            raise Exception(f"Error: {e}")


    def choose_payment(self):
        payment_options = self.driver.find_elements(*self.PAYMENT_OPTIONS)

        if not payment_options:
            raise Exception("No payment options found")

        for option in payment_options:
            label = option.find_element(By.CSS_SELECTOR, "label").text.strip().lower()
            if self.PAYMENT_TYPE in label:
                radio = option.find_element(By.CSS_SELECTOR, ".custom-radio")
                radio.click()
                short_delay()
                return

        raise Exception("Could not choose payment option")


    def accept_terms(self):
        checkbox = self.driver.find_element(*self.TERMS_CHECK)
        self.driver.execute_script("arguments[0].click();", checkbox)
        short_delay(3,3)


    def place_order(self):
        buttons = self.driver.find_elements(*self.PAYMENT_BUTTON)
        button = buttons[-1]
        button.click()
        # self.safe_click(self.PAYMENT_BUTTON)
        short_delay()