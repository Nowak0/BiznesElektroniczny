from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import short_delay


class OrderHistoryPage(BasePage):
    ORDER_HISTORY_PAGE_URL = "http://localhost:8080/pl/historia-zamowien"
    ORDER_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")
    ORDER_STATUS = (By.CSS_SELECTOR, "td span.label.label-pill.bright")
    INVOICE_LINK = (By.CSS_SELECTOR, "td.hidden-md-down a")


    def get_newest_order(self):
        self.open(self.ORDER_HISTORY_PAGE_URL)
        short_delay(2,3)

        rows = self.driver.find_elements(*self.ORDER_ROWS)
        if not rows:
            return None

        last_row = rows[0]
        status = last_row.find_element(*self.ORDER_STATUS).text.strip()

        try:
            invoice_link = last_row.find_element(*self.INVOICE_LINK).get_attribute("href")
        except:
            invoice_link = None

        return {"status": status, "invoice_link": invoice_link}


    def download_invoice(self):
        info = self.get_newest_order()
        if not info or not info["invoice_link"]:
            return None

        try:
            href = info["invoice_link"]
            self.driver.get(href)
            short_delay(3,4)
            print("Invoice downloaded successfully")
        except Exception as e:
            raise f"Error downloading invoice: {e}"

        return href

