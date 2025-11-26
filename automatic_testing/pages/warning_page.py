from pydoc import safeimport

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay, random_string

class WarningPage(BasePage):
    ADVANCED_BUTTON = (By.CSS_SELECTOR, '#details-button')
    PROCEED_LINK = (By.CSS_SELECTOR, '#proceed-link')


    def accept_warning(self):
        self.driver.find_element(*self.ADVANCED_BUTTON).click()
        short_delay()
        self.safe_click(self.PROCEED_LINK)
        short_delay(3,3)