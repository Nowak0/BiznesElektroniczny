from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, '.cart-items .cart-item, .cart-summary .cart-line, .cart .product-line')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '.remove-from-cart, .cart-line .delete, .product-line .remove')

    def open_cart(self):
        self.driver.get("https://monocerus.pl/koszyk")


    def list_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)


    def remove_n_items(self, n=1):
        removed = 0
        items = self.list_items()
        for item in items:
            try:
                button = item.find_element(*self.REMOVE_BUTTON)
                button.click()
                short_delay()
                removed += 1
                if removed >= n:
                    break
            except:
                continue

        return removed