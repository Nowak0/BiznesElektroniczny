from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay


class HomePage(BasePage):
    COOKIE_CLOSE = (By.CSS_SELECTOR, "button.close, .cookie-close, .js-cookie-accept")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='s'], input[name='search'], input[type='search']")
    SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[type='submit'], .search-button")
    CATEGORY_LINKS = (By.CSS_SELECTOR, "ul.menu li a, nav .category-item a")

    def accept_cookies(self):
        try:
            return self.safe_click(self.COOKIE_CLOSE, timeout=3)
        except:
            return False


    def search(self, text):
        element = self.driver.find_element(*self.SEARCH_INPUT)
        element.clear()
        element.send_keys(text)
        short_delay()
        self.safe_click(self.SEARCH_SUBMIT)


    def pick_category_links(self, limit=2):
        anchors = self.driver.find_elements(*self.CATEGORY_LINKS)
        urls = []
        for anchor in anchors:
            href = anchor.get_attribute("href")
            text = anchor.text.strip()
            if href and href not in urls and text:
                urls.append((text, href))
            if len(urls) >= limit:
                break

        return urls