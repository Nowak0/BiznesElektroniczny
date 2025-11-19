from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay, random_string
import random


class CategoryPage(BasePage):
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "ol.products li, .product-items .product, .product-list .product")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.product-name, a.product-title, a.product_img_link, a[data-product-link")

    def list_product_links(self, max_items=10):
        items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        links = []
        for item in items[:max_items]:
            try:
                a = item.find_element(*self.PRODUCT_LINK)
                href = a.get_attribute("href")
                title = a.text.strip() or a.get_attribute("title")
                if href:
                    links.append({"name": title, "href": href})
            except:
                continue
        return links


    def add_first_n_products_to_cart(self, n=5, quantity_choices=(1,2,3)):
        links = self.list_product_links(n)
        added = []

        for p in links:
            self.driver.get(p["url"])
            short_delay()
            try:
                qty_input = self.driver.find_element(By.CSS_SELECTOR, "input.qty, input[name='qty], input[name='quantity']")
                qty = str(random.choice(quantity_choices))
                qty_input.clear()
                qty_input.send_keys(qty)
            except:
                qty = "1"

            add = (By.CSS_SELECTOR, "button.add-to-cart, button[name='add'], button.add-to-cart-button, .add-to-cart")
            self.safe_click(add, timeout=6)
            added.append({"name": p["name"], "url": p["url"], "qty": qty})
            short_delay()
        return added