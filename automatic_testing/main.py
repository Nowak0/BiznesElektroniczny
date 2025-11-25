from _pyrepl.commands import home

from driver import create_driver
import time, random

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.order_history_page import OrderHistoryPage
from utils import short_delay

BASE_URL = "https://localhost/pl/"
DOWNLOAD_DIR = "./downloads"


def category_page(driver, home):
    categories = home.pick_category_links()
    # categories = [("", "http://localhost:8080/pl/3-clothes"), ("", "http://localhost:8080/pl/6-accessories")]
    total_added = []

    undone_adds = 0
    for name, url in categories:
        cat_page = CategoryPage(driver)
        cat_page.open(url)
        added, undone_adds = cat_page.add_first_n_products_to_cart(n=5, undone_adds=undone_adds)
        total_added.append(added)

    print(f"Added products: {total_added}")

    home.open(BASE_URL)
    search_text = "kubek"
    home.search(search_text)
    cat_page = CategoryPage(driver)
    results = cat_page.list_product_links()

    if not results:
        return

    result = False
    product = ""
    while not result:
        product = random.choice(results)
        result = cat_page.add_given_product_to_cart(product["url"])

    print(f"Added product: {product}\n\n")


def cart_page(driver):
    cart = CartPage(driver)
    cart.open_cart()
    removed = cart.remove_n_items(n=3)
    print(f"Removed {removed} products from the cart\n\n")


def account_page(driver, type="register"):
    account = AccountPage(driver)

    if type == "register":
        user_data = account.register_new_user()
    else:
        user_data = account.login(email="psscarpeta@gmail.com", password="qwerty")

    print(f"Registered user: {user_data}\n\n")


def checkout_page(driver):
    checkout = CheckoutPage(driver)
    checkout.open_page()
    checkout.select_delivery_info(address="Testowa 1", postcode="30-230", city="Testowanie", phone="123456789")
    checkout.choose_carrier()
    checkout.choose_payment()
    checkout.accept_terms()
    checkout.place_order()
    print("Accepted new order")


def order_history_page(driver):
    history = OrderHistoryPage(driver)
    newest_order_info = history.get_newest_order()
    history.download_invoice()
    print(f"Newest order: {newest_order_info}")


def main():
    driver = create_driver(download_dir=DOWNLOAD_DIR, headless=False)
    try:
        home = HomePage(driver)
        home.open(BASE_URL)
        short_delay(10,10)

        category_page(driver, home)
        cart_page(driver)
        account_page(driver, type="register")
        checkout_page(driver)
        order_history_page(driver)

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()