from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, '.cart-item')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '.remove-from-cart')
    PRODUCT_INFO = (By.CSS_SELECTOR, 'a.label')


    def open_cart(self):
        self.driver.get("https://localhost/pl/koszyk")


    def list_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)


    def remove_n_items(self, n=1):
        removed = 0

        print("Removed products:")
        while removed < n:
            items = self.list_items()

            if not items:
                break

            item = items[0]
            try:
                print((item.find_element(*self.PRODUCT_INFO)).get_attribute("href"))
                button = item.find_element(*self.REMOVE_BUTTON)
                button.click()
                short_delay(2,3)
                removed += 1

            except Exception as e:
                raise Exception(f"Error removing product: {e}")

        return removed