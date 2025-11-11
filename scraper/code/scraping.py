import requests
from bs4 import BeautifulSoup
import time
import json
import os
from requests.compat import urljoin
import random

# SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# KONFIGURACJA
MAIN_URL = 'https://8a.pl/'

# Nagłówki są dla get_main_categories()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': MAIN_URL
}

CATEGORIES_FILE = 'scraper/results/main_categories.json'
OUTPUT_FILE = 'scraper/results/links_products.json'
INPUT_LINKS_FILE = 'scraper/results/links_products.json'
OUTPUT_DATA_FILE = 'scraper/results/detailed_products_data.json'
MAX_PRODUCTS_PER_CATEGORY = 10
DELAY_SECONDS = 5
DELAY_SECONDS_MAX = 8

# INICJALIZACJA STEROWNIKA SELENIUM

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

def initialize_driver():    
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    
    try:
        service = Service(log_path='NUL')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(30)
        return driver
    
    except WebDriverException as e:
        print(f"❌ Błąd inicjalizacji sterownika: {e}")
        print("Upewnij się, że masz zainstalowaną przeglądarkę Chrome oraz odpowiedni 'chromedriver' (lub nowsze Selenium).")
        return None
        
# POBIERANIE KATEGORII (requests)

def get_main_categories():
    categories_data = []

    print(f"Pobieranie strony głównej: {MAIN_URL}...")
    
    try:
        response = requests.get(MAIN_URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        main_menu_items = soup.find_all('li', class_='level0') # klasa nagłówka menu głównego
        
        if not main_menu_items:
            print("Nie znaleziono elementów menu z klasą 'level0'.")
            return []


        for item in main_menu_items:
            link_tag = item.find('a', class_='level-top') # klasa pojedyńczych kategorii
            
            if link_tag:
                category_name_tag = link_tag.find('span') # nazwa
                name = category_name_tag.get_text(strip=True) if category_name_tag else 'Brak nazwy'
                href = link_tag.get('href') # link
                full_url = requests.compat.urljoin(MAIN_URL, href)

                if full_url and full_url != MAIN_URL:
                    categories_data.append({'name': name, 'url': full_url})
        
        print(f"✅ Znaleziono {len(categories_data)} głównych kategorii.")
        return categories_data

    except requests.exceptions.RequestException as e:
        print(f"❌ Wystąpił błąd sieciowy lub błąd statusu HTTP (MAIN_URL): {e}")
        return []
    finally:
        time.sleep(DELAY_SECONDS)
        
def load_categories(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Błąd: Nie znaleziono pliku kategorii: {file_path}. Uruchom najpierw funkcję create_categories.")
        return []

# POBIERANIE PRODUKTU (selenium)

def scrape_product_links_selenium(driver, category_url, category_name):
    
    product_links = []
    print(f"\n---> Scrapowanie kategorii: {category_name} ({category_url})")

    WAIT_TIME = 15 # Czas czekania na strone

    try:
        driver.get(category_url)
        
        products_container_xpath = '//ol[contains(@class, "products list items product-items")]' # link listy produtków
        wait = WebDriverWait(driver, WAIT_TIME)
        
        # Pobieranie kontenera
        product_list = wait.until(
            EC.visibility_of_element_located((By.XPATH, products_container_xpath))
        )
        print("   -> Znaleziono kontener listy produktów.")

        # Pobieranie produktu
        product_item_css = 'a[data-category-product-main-image]'
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, product_item_css))
        )
        print("   -> Pierwszy produkt załadowany pomyślnie.")
        
        product_items = product_list.find_elements(By.CSS_SELECTOR, product_item_css)[:MAX_PRODUCTS_PER_CATEGORY]

        if not product_items:
            print("   ⚠️ Znaleziono kontener, ale linki produktów nie są widoczne (pusta lista).")
            return []
        
        for item in product_items:
            href = item.get_attribute('href')
            title = item.get_attribute('title') 
            
            if href and title:
                product_links.append({
                    'category': category_name,
                    'name': title,
                    'url': href
                })
        
        print(f"   ✅ Zebrano {len(product_links)} / {MAX_PRODUCTS_PER_CATEGORY} linków produktowych.")
        
    except TimeoutException:
        print(f"   ❌ Przekroczono limit czasu ładowania (TIMEOUT) lub nie znaleziono kluczowego elementu w ciągu {WAIT_TIME}s.")
    except NoSuchElementException:
        print("   ❌ Nie znaleziono kontenera listy produktów lub pierwszego elementu.")
    except Exception as e:
        print(f"   ❌ Wystąpił nieznany błąd: {e}")
    finally:
        # Losowe opoznienie, trickowanie strony 🤡
        sleep_duration = random.uniform(DELAY_SECONDS, DELAY_SECONDS_MAX) 
        print(f"   -> Oczekiwanie {sleep_duration:.2f}s przed kolejnym żądaniem...")
        time.sleep(sleep_duration)
        
    return product_links

# POBIERANIE DANYCH PRODUKTU (selenium)

def scrape_product_data_selenium(driver, product_url, product_name):
    
    product_data = {
        'name': product_name,
        'url': product_url,
        'price': None,
        'description_snippet': None,
        'Kolor/Rozmiar': None,
        'last_category': None,
        'image_urls': [] 
    }
    
    # Ustawienie czasu oczekiwania
    WAIT_TIME = 30

    # Kolor/rozmiar - bierzemy z nazwy, zawsze jest po "-" w nazwie
    try:
        separator = " - "
        if separator in product_name:
            variant_info = product_name.split(separator)[-1].strip()
            product_data['Kolor/Rozmiar'] = variant_info
        
    except Exception as e:
        print(f"   Błąd przy ekstrakcji Kolor/Rozmiar z nazwy: {e}")
            
    try:
        driver.get(product_url)
        wait = WebDriverWait(driver, WAIT_TIME)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        
        # Cena
        try:
            price_element_css = '.price-wrapper .price' 
            price_element = driver.find_element(By.CSS_SELECTOR, price_element_css)
            price_text = price_element.text.strip().replace('\xa0', ' ').replace(',', '.') 
            
            # Pobieramy cenę z data-price-amount, jeśli element nadrzędny jest dostępny
            price_amount = price_element.find_element(By.XPATH, '..').get_attribute('data-price-amount')
            
            product_data['price'] = price_amount if price_amount else price_text
        except NoSuchElementException:
            pass 
            
        # Podkategoria
        try:
            breadcrumb_items = driver.find_elements(By.CSS_SELECTOR, 'ul.items li')
            
            # Ostatnia kategoria to przedostatni element (ostatni to nazwa produktu)
            if len(breadcrumb_items) >= 2:
                # Element <li> zawierający link do kategorii
                last_category_li = breadcrumb_items[-2] 
                # Wewnątrz tego <li> szukamy linku <a>, aby pobrać tekst
                last_category_a = last_category_li.find_element(By.TAG_NAME, 'a')
                category_name = last_category_a.text.strip()
                product_data['last_category'] = category_name
        except Exception:
            pass 

        # Opis
        try:
            desc_container_css = '.product.attribute.description .value'
            desc_container = driver.find_element(By.CSS_SELECTOR, desc_container_css)
            
            first_paragraph = desc_container.find_element(By.TAG_NAME, 'p')
            product_data['description_snippet'] = first_paragraph.text.strip()
        except NoSuchElementException:
            pass

        # Zdjecia - TODO
        # Wymagamy dwóch zdjęć w dużej rozdzielczości.
        try:
            image_elements = driver.find_elements(By.CSS_SELECTOR, '.product-image-container .gallery-placeholder__image')
            
            if not image_elements:
                 image_elements = driver.find_elements(By.CSS_SELECTOR, '.fotorama__img')

            urls = set()
            for img in image_elements:
                url = img.get_attribute('src') or img.get_attribute('data-src')
                
                if url:
                    cleaned_url = url.split('?')[0]
                    urls.add(cleaned_url)
                    if len(urls) >= 2:
                        break
            
            product_data['image_urls'] = list(urls)
            
        except Exception as e:
            print(f"   Wystąpił błąd przy pobieraniu URL-i zdjęć: {e}")
            
        print(f"   ✅ Zebrano dane: Cena: {product_data['price']}, Kolor/Rozmiar: {product_data['Kolor/Rozmiar']}")
        
    except TimeoutException:
        print(f"   ❌ Przekroczono limit czasu ładowania (TIMEOUT) dla produktu.")
    except Exception as e:
        print(f"   ❌ Wystąpił nieznany błąd podczas scrapowania produktu: {e}")
        
    finally:
        time.sleep(DELAY_SECONDS) 
        
    return product_data

# FUNKCJA ZAPISUJĄCA KATEGORIE

def create_categories():
    kategorie = get_main_categories()

    if kategorie:
        os.makedirs('scraper/results', exist_ok=True)
        file_path = 'scraper/results/main_categories.json'
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(kategorie, f, indent=4, ensure_ascii=False)
        
        print(f"\n[CREATE] Dane zostały pomyślnie zapisane do: {file_path}")
    
    return kategorie

# PĘTLA GŁÓWNA - merge z tą na dole

# def main_scraper():
#     # Sprawdzenie, czy kategorie zostały już pobrane i zapisane.
#     kategorie = load_categories(CATEGORIES_FILE)
#     if not kategorie:
#         kategorie = create_categories()
#         if not kategorie:
#              return

#     all_product_links = []
    
#     # Iteracja po kategoriach i pobranie linków
#     for i, kategoria in enumerate(kategorie):
#         print(f"\n======== ROZPOCZYNAM KATEGORIĘ {i + 1}/{len(kategorie)} ========")
        
#         # Inicjalizacja sterownika przed każdą kategorią
#         driver = initialize_driver()
#         if not driver:
#             print("Nie można zainicjalizować sterownika, przerywam.")
#             break 
            
#         try:
#             # Scrapowanie linków
#             links = scrape_product_links_selenium(driver, kategoria['url'], kategoria['name'])
#             all_product_links.extend(links)
            
#         finally:
#             # Zamykamy przeglądarkę po zakończeniu scrapowania tej kategorii
#             driver.quit()
#             print("Zakończono sesję przeglądarki.")
            
#             # 🤡
#             sleep_duration = random.uniform(DELAY_SECONDS, DELAY_SECONDS_MAX) 
#             print(f"Czekanie {sleep_duration:.2f}s przed uruchomieniem następnej sesji.")
#             time.sleep(sleep_duration)


#     # Zapis końcowy
#     if all_product_links:
#         os.makedirs('scraper/results', exist_ok=True)
#         with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
#             json.dump(all_product_links, f, indent=4, ensure_ascii=False)
        
#         print(f"\n==========================================")
#         print(f"Sukces! Zebrano łącznie {len(all_product_links)} linków produktowych.")
#         print(f"Zapisano w: {OUTPUT_FILE}")
#         print(f"==========================================")
#     else:
#         print("Nie zebrano żadnych linków produktowych.")

# if __name__ == "__main__":
#     main_scraper()
    
def main_scraper():
    # Wczytanie linków do produktów z jsona z linkami
    try:
        with open(INPUT_LINKS_FILE, 'r', encoding='utf-8') as f:
            product_links_to_scrape = json.load(f)
        print(f"✅ Wczytano {len(product_links_to_scrape)} linków do produktów.")
    except FileNotFoundError:
        print(f"❌ Błąd: Nie znaleziono pliku linków: {INPUT_LINKS_FILE}. Uruchom najpierw etap zbierania linków.")
        return

    all_detailed_data = []
    
    # Iteracja po produktach, używając nowej sesji na każdy produkt 🤡
    for i, product_info in enumerate(product_links_to_scrape):
        product_url = product_info['url']
        product_name = product_info['name']
        
        print(f"\n======== ROZPOCZYNAM PRODUKT {i + 1}/{len(product_links_to_scrape)}: {product_name} ========")
        
        driver = initialize_driver()
        if not driver:
            print("Nie można zainicjalizować sterownika, przerywam.")
            break 
            
        try:
            # Scrapowanie szczegółów produktu
            data = scrape_product_data_selenium(driver, product_url, product_name)
            all_detailed_data.append(data)
            
        finally:
            driver.quit()
            
            sleep_duration = random.uniform(DELAY_SECONDS, DELAY_SECONDS_MAX) 
            print(f"Czekanie {sleep_duration:.2f}s przed uruchomieniem następnej sesji.")
            time.sleep(sleep_duration)


    # Zapis końcowy
    if all_detailed_data:
        os.makedirs('scraper/results', exist_ok=True)
        with open(OUTPUT_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_detailed_data, f, indent=4, ensure_ascii=False)
        
        print(f"\n==========================================")
        print(f"Sukces! Zebrano dane dla {len(all_detailed_data)} produktów.")
        print(f"Zapisano w: {OUTPUT_DATA_FILE}")
        print(f"==========================================")
    else:
        print("Nie zebrano żadnych szczegółowych danych.")

if __name__ == "__main__":
    main_scraper()