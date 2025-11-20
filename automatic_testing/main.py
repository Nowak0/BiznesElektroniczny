from driver import create_driver
import time, random

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.order_history_page import OrderHistoryPage
from utils import short_delay

BASE_URL = "https://monocerus.pl/"
DOWNLOAD_DIR = "./downloads"


def category_page(driver, home):
    categories = home.pick_category_links()
    categories = [("", "https://monocerus.pl/112-artist-resin"), ("", "https://monocerus.pl/2-glowna")]
    total_added = []

    # undone_adds = 0
    # for name, url in categories:
    #     cat_page = CategoryPage(driver)
    #     cat_page.open(url)
    #     added, undone_adds = cat_page.add_first_n_products_to_cart(n=5, undone_adds=undone_adds)
    #     total_added.append(added)
    #
    # print(f"Added products: {total_added}")

    home.open(BASE_URL)
    search_text = "kon"
    home.search(search_text)
    cat_page = CategoryPage(driver)
    results = cat_page.list_product_links()

    if results:
        product = random.choice(results)
        cat_page.driver.get(product["url"])
        cat_page.add_first_n_products_to_cart(n=1)
        print(f"Added product: {product}")


def cart_page(driver):
    cart = CartPage(driver)
    cart.open(BASE_URL)
    removed = cart.remove_n_items(n=2)
    print(f"Removed {removed} products from the cart")


def account_page(driver):
    account = AccountPage(driver)
    user_data = account.register_new_user()
    print(f"Registered user: {user_data}")


def checkout_page(driver):
    checkout = CheckoutPage(driver)
    checkout.select_address()
    checkout.choose_carrier()
    checkout.choose_payment()
    checkout.accept_terms()
    # checkout.place_order()
    print("Accepted new order")


def order_history_page(driver):
    history = OrderHistoryPage(driver)
    driver.get(BASE_URL + "?controller=history")
    downloaded = history.download_invoice()
    if downloaded:
        print("Downloaded invoice")
    else:
        print("No downloaded invoice")

    last_order_info = history.get_last_order()
    print(f"Last order info: {last_order_info['status']}")


def main():
    driver = create_driver(download_dir=DOWNLOAD_DIR, headless=False)
    try:
        home = HomePage(driver)
        home.open(BASE_URL)
        short_delay(3,3)
        home.accept_cookies()

        category_page(driver, home)
        # cart_page(driver)
        # account_page(driver)
        # checkout_page(driver)
        # order_history_page(driver)

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()