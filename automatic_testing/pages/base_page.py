from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from utils import short_delay, wait_for


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open(self, url):
        self.driver.get(url)


    def safe_click(self, locator, timeout=10):
        try:
            element = wait_for(self.driver, locator, timeout, ec.element_to_be_clickable)
            element.click()
            short_delay()
            return True
        except TimeoutException:
            return False