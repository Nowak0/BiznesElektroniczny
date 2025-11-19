from driver import create_driver
import time, random
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage


BASE_URL = "https://monocerus.pl/"
DOWNLOAD_DIR = "./downloads"


def main():
    driver = create_driver(download_dir=DOWNLOAD_DIR, headless=False)
    try:
        home = HomePage(driver)
        home.open(BASE_URL)
        home.accept_cookies()

        categories = home.pick_category_links(limit=2)
        total_added = []

        for name,url in categories:
            cat_page = CategoryPage(driver)
            cat_page.open(url)
            added = cat_page.add_first_n_products_to_cart(n=5)
            total_added.extend(added)

        print(f"Added products: {total_added}")

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

        cart = CartPage(driver)
        cart.open(BASE_URL)
        removed = cart.remove_n_items(n=2)
        print(f"Removed {removed} products from the cart")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()