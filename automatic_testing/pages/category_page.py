from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay, random_string
import random


class CategoryPage(BasePage):
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "#js-product-list article.product-miniature")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.thumbnail.product-thumbnail")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, "#product-availability")


    def check_availability(self):
        element = self.driver.find_element(*self.PRODUCT_AVAILABILITY)
        txt = element.text.strip().lower()

        if "ostatnie" in txt:
            return "ostatnie"
        elif "brak" in txt:
            return "brak"
        else:
            return "ok"


    def list_product_links(self, max_items=10):
        items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        links = []
        for item in items[:max_items]:
            try:
                a = item.find_element(*self.PRODUCT_LINK)
                href = a.get_attribute("href")
                title = href.split("/")[-1].replace(".html", "")
                if href:
                    links.append({"name": title, "url": href})
            except:
                continue
        return links


    def add_first_n_products_to_cart(self, n=2, quantity_choices=(1,2,3), undone_adds=0):
        links = self.list_product_links(n)
        added = []

        for p in links:
            print(p["url"])
            self.driver.get(p["url"])
            short_delay()
            try:
                txt = self.check_availability()

                if txt == "ostatnie":
                    quantity = 1
                elif txt == "brak":
                    undone_adds+=1
                    continue
                else:
                    quantity = str(random.choice(quantity_choices) + undone_adds)
                    undone_adds = 0

                self.driver.execute_script("document.getElementById('quantity_wanted').value = arguments[0];", quantity)
            except:
                undone_adds += 1
                continue

            self.safe_click(self.ADD_TO_CART_BUTTON, timeout=2)
            added.append({"name": p["name"], "url": p["url"], "quantity": quantity})
            short_delay()
        return added, undone_adds


    def add_given_product_to_cart(self, url):
        self.driver.get(url)
        short_delay()
        try:
            txt = self.check_availability()

            if "brak" in txt:
                return False
            else:
                self.driver.execute_script("document.getElementById('quantity_wanted').value = arguments[0];", "1")
        except Exception as e:
            raise Exception(f"Error adding product to cart: {e}")

        self.safe_click(self.ADD_TO_CART_BUTTON, timeout=2)
        short_delay()

        return True