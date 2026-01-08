from pandas.core.arrays.string_ import BaseStringArray

from driver import create_driver
import random

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.order_history_page import OrderHistoryPage
from pages.warning_page import WarningPage
from utils import short_delay

BASE_URL = "http://localhost:8081/pl/"
DOWNLOAD_DIR = "./downloads"


def warning_page(driver):
    warning_page = WarningPage(driver, BASE_URL)
    warning_page.accept_warning()


def category_page(driver, home, search_text: str):
    categories = home.pick_category_links()
    # categories = [("", "https://localhost/pl/43-collecta"), ("", "https://localhost/pl/14-breyer")]
    total_added = []

    undone_adds = 0
    for name, url in categories:
        cat_page = CategoryPage(driver, BASE_URL)
        cat_page.open(url)
        added, undone_adds = cat_page.add_first_n_products_to_cart(n=5, undone_adds=undone_adds)
        total_added.append(added)

    print(f"Added products: {total_added}")

    home.open(BASE_URL)

    home.search(search_text)
    cat_page = CategoryPage(driver, BASE_URL)
    results = cat_page.list_product_links()

    if not results:
        return

    result = False
    product = ""
    while not result:
        product = random.choice(results)
        result = cat_page.add_given_product_to_cart(product["url"])

    print(f"Added product: {product}\n\n")
    short_delay(2,3)


def cart_page(driver):
    cart = CartPage(driver, BASE_URL)
    cart.open_cart()
    removed = cart.remove_n_items(n=3)
    print(f"Removed {removed} products from the cart\n\n")


def account_page(driver, type="register", email: str = "", password: str = ""):
    account = AccountPage(driver, BASE_URL)

    if type == "register":
        user_data = account.register_new_user()
    else:
        user_data = account.login(email=email, password=password)

    print(f"Registered user: {user_data}\n\n")


def checkout_page(driver):
    payment_type = "przelew"

    checkout = CheckoutPage(driver, BASE_URL)
    checkout.open_page()
    checkout.select_delivery_info(address="Testowa 1", postcode="30-230", city="Testowanie", phone="123456789")
    checkout.choose_carrier()
    checkout.choose_payment(payment_type)
    checkout.accept_terms()
    checkout.place_order()
    print("Accepted new order")


def order_history_page(driver):
    history = OrderHistoryPage(driver, BASE_URL)
    newest_order_info = history.get_newest_order()
    history.download_invoice()
    print(f"Newest order: {newest_order_info}")


def main():
    driver = create_driver(download_dir=DOWNLOAD_DIR, headless=False)
    try:

        home = HomePage(driver, BASE_URL)
        home.open(BASE_URL)
        short_delay()

        if "https" in BASE_URL:
            warning_page(driver)

        category_page(driver, home, "pies")
        cart_page(driver)
        account_page(driver, type="register")
        checkout_page(driver)
        order_history_page(driver)

    finally:
        short_delay(2,2)
        driver.quit()


if __name__ == "__main__":
    main()