from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def create_driver(download_dir: str = None, headless: bool = False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920x1080") # moze byc zamiast x ,
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}

    if download_dir:
        os.makedirs(download_dir, exist_ok=True)
        chrome_prefs = {
            "download.default_directory": os.path.abspath(download_dir),
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_settings.popups": 0
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)

    ChromeDriverManager().install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(69)
    driver.implicitly_wait(6.9)\

    return driver