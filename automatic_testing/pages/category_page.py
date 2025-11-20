from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay, random_string
import random


class CategoryPage(BasePage):
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "#js-product-list article.product-miniature")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.thumbnail.product-thumbnail")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")

    def list_product_links(self, max_items=10):
        items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        links = []
        for item in items[:max_items]:
            try:
                a = item.find_element(*self.PRODUCT_LINK)
                href = a.get_attribute("href")
                # title = (a.get_attribute((By.CSS_SELECTOR, "img"))).get_attribute("alt")
                title = ""
                if href:
                    links.append({"name": title, "url": href})
            except:
                continue
        return links


    def add_first_n_products_to_cart(self, n=2, quantity_choices=(1,2,3), undone_adds=0):
        links = self.list_product_links(n)
        added = []

        for p in links:
            self.driver.get(p["url"])
            short_delay()
            try:
                quantity = str(random.choice(quantity_choices) + undone_adds)
                self.driver.execute_script("document.getElementById('quantity_wanted').value = arguments[0];", quantity)
                undone_adds = 0
            except:
                undone_adds += 1
                continue

            self.safe_click(self.ADD_TO_CART_BUTTON, timeout=2)
            added.append({"name": p["name"], "url": p["url"], "qty": quantity})
            short_delay()
        return added, undone_adds