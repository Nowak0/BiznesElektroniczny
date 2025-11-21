import os
import requests
import json
import re
from bs4 import BeautifulSoup
from time import sleep

MAIN_URL = "https://monocerus.pl/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTOS_DIR = os.path.join(BASE_DIR, '..', 'photos')
RESULTS_CATEGORIES_DIR = os.path.join(BASE_DIR, '..', 'results', 'categories.json')
RESULTS_PRODUCTSLINKS_DIR = os.path.join(BASE_DIR, '..', 'results', 'products_links.json')
RESULTS_PRODUCT_DETAILED_DIR = os.path.join(BASE_DIR, '..', 'results', 'product_detail.json')

MAX_PRODUCTS_PP = 7

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
       
def build_subcategories(main_li):    
    
    results = []
    
    for li in main_li:
        
        main_link_tag = li.find('a', class_=False) 
        if not main_link_tag:
            return None
        
        category_data = {
            "nazwa": main_link_tag.get_text(strip=True),
            "link": main_link_tag.get('href'),
            "podkategorie": []
        }
    
        sub_menu_ul = li.find('ul', class_='category-sub-menu')
        
        if sub_menu_ul:
            all_sub_lis = sub_menu_ul.find_all('li', recursive=False)
            
            def process_sub_list(parent_li):
                link_tag = parent_li.select_one('a.category-sub-link')
                
                if not link_tag:
                    return None
                
                sub_category = {
                    "nazwa": link_tag.get_text(strip=True),
                    "link": link_tag.get('href'),
                    # Inicjalizacja listy na niższe poziomy zagnieżdżenia
                    "podkategorie": [] 
                }
                
                # Sprawdź, czy istnieje głębsze zagnieżdżenie (div.collapse)
                nested_div = parent_li.select_one('div.collapse')
                if nested_div:
                    # Znajdź listę podkategorii wewnątrz tego zagnieżdżenia
                    nested_ul = nested_div.select_one('ul.category-sub-menu')
                    if nested_ul:
                        # Znajdź bezpośrednie elementy <li> w tym zagnieżdżeniu (Poziom + 1)
                        nested_lis = nested_ul.find_all('li', recursive=False)
                        for nested_li in nested_lis:
                            # Wywołanie rekurencyjne dla kolejnego poziomu
                            child_data = process_sub_list(nested_li)
                            if child_data:
                                sub_category['podkategorie'].append(child_data)
                                
                return sub_category

            # Przetwarzamy elementy Poziomu 1
            for li_level_1 in all_sub_lis:
                sub_cat_data = process_sub_list(li_level_1)
                if sub_cat_data:
                    category_data['podkategorie'].append(sub_cat_data)
        
        results.append(category_data)

    return results
       
def build_categories():
    
    response = requests.get(MAIN_URL, headers=header, timeout=10)
    response.raise_for_status()
        
    soup = BeautifulSoup(response.text, 'html.parser')
        
    main_li = soup.find_all('li', {'data-depth': '0'})
        
    if main_li:
        nested_data = build_subcategories(main_li)
        return nested_data
    
    return None
       
def extract_product_data(product_html_block):
    soup = BeautifulSoup(str(product_html_block), 'html.parser')
    
    product_data = {}

    title_element = soup.select_one('h2.product-title a')
    if title_element:
        product_data['name'] = title_element.get_text(strip=True)
        product_data['link'] = title_element.get('href')
    else:
        thumbnail_link = soup.select_one('a.product-thumbnail')
        if thumbnail_link:
             product_data['link'] = thumbnail_link.get('href')
             product_data['name'] = soup.select_one('article').get('data-id-product') # Jeśli nie ma nazwy, użyj ID

    price_element = soup.select_one('span.price')
    if price_element:
        price_text = price_element.get_text(strip=True)
        clean_price = re.sub(r'[^\d,]', '', price_text).replace(',', '.')
        product_data['price'] = clean_price
    else:
        product_data['price'] = None

    return product_data

def scrape_category_products(category_url):
    products_list = []
    category_list_data = []
    
    try:
        response = requests.get(category_url, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Błąd podczas pobierania strony {category_url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_containers = soup.select('div.js-product.product')
    
    category_list_data = extract_breadcrumbs_data(soup)
    
    if not product_containers:
        print(f"Brak produktów w kategorii: {category_url}")
        return []

    for container in product_containers:
        data = extract_product_data(container)
        data['kategorie'] = category_list_data
        
        if len(products_list) >= MAX_PRODUCTS_PP:
            return products_list
        
        products_list.append(data)
    
    return products_list

def find_deepest_links(category_node, deepest_links):
    if not category_node.get('podkategorie'):
        deepest_links.append(category_node['link'])
        return
    
    for sub_category in category_node['podkategorie']:
        find_deepest_links(sub_category, deepest_links)

def load_json_and_find_links(json_filepath):

    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            categories_tree = json.load(f)
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {json_filepath}.")
        return []
    
    if not isinstance(categories_tree, list):
         categories_tree = [categories_tree] 

    deepest_links = []
    
    for main_category in categories_tree:
        find_deepest_links(main_category, deepest_links)
    
    return list(set(deepest_links))

def extract_breadcrumbs_data(soup):
    breadcrumbs_list = soup.select('nav.breadcrumb ol li')
    
    category_names = [
        li.get_text(strip=True) for li in breadcrumbs_list if li.get_text(strip=True) != 'Strona główna'
    ]
    
    return category_names[:3]

def main():
    # kategorie = build_categories() 
        
    # with open(RESULTS_CATEGORIES_DIR, 'w', encoding='utf-8') as f:
    #     json.dump(kategorie, f, indent=4, ensure_ascii=False)

    deepest_links = load_json_and_find_links(RESULTS_CATEGORIES_DIR)
    
    all_products_data = []
    
    for i, link in enumerate(deepest_links):
        print(f"\n--- Przetwarzanie linku {i + 1}/{len(deepest_links)}: {link} ---")
        products_from_category = scrape_category_products(link)
        all_products_data.extend(products_from_category)
        
        sleep(1)
        
        if i >= 3:
            break
        
    with open(RESULTS_PRODUCTSLINKS_DIR, 'w', encoding='utf-8') as f:
        json.dump(all_products_data, f, indent=4, ensure_ascii=False)    
            
if __name__ == "__main__":
    main()