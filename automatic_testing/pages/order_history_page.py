from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay
import os, time


class OrderHistoryPage(BasePage):
    ORDER_ROWS = (By.CSS_SELECTOR, ".order-row, .history-row, .order-list tr")
    ORDER_STATUS = (By.CSS_SELECTOR, ".order-status, .status-label")
    INVOICE_LINK = (By.CSS_SELECTOR, "a[href*='invoice'], a.download-invoice")


    def get_last_order(self):
        rows = self.driver.find_elements(*self.ORDER_ROWS)
        if not rows:
            return None

        last_row = rows[0]
        status = last_row.find_element(*self.ORDER_STATUS).text().strip()
        invoice_link = None

        try:
            invoice_link = last_row.find_element(*self.INVOICE_LINK).get_attribute("href")
        except:
            pass

        return {"status": status, "invoice_link": invoice_link}


    def download_invoice(self):
        info = self.get_last_order()
        if info and info["invoice_link"]:
            self.driver.get(info["invoice_link"])
            short_delay(3,4)
            return True

        return False
