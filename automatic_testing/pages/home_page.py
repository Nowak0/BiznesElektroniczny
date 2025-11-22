import random
from operator import truediv

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class HomePage(BasePage):
    COOKIE_ACCEPT = (By.CSS_SELECTOR, "button.x13eucookies__btn--accept-all")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='s']")
    CATEGORY_LINKS = (By.CSS_SELECTOR, ".block-categories a")


    def accept_cookies(self):
        try:
            self.safe_click(self.COOKIE_ACCEPT)
            print("✅ Accepted cookies 🍪")
            return True
        except:
            print("❌Could not accept cookies 🍪")
            return False


    def search(self, text):
        element = self.driver.find_element(*self.SEARCH_INPUT)
        element.clear()
        element.send_keys(text)
        short_delay()
        element.send_keys(Keys.ENTER)
        short_delay(1.5,2)


    def pick_category_links(self, limit=2):
        categories = self.driver.find_elements(*self.CATEGORY_LINKS)
        urls = []
        for category in categories:
            href = category.get_attribute("href")
            text = category.text.strip()
            if href and href not in urls and text:
                urls.append((text, href))

        if len(urls) <= limit:
            print("Chosen categories:")
            print(urls)
            return urls
        else:
            chosen_urls = random.sample(urls, limit)
            print("Chosen categories:")
            print(chosen_urls)
            return chosen_urls