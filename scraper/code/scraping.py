import os
import requests
import json
from bs4 import BeautifulSoup
from time import sleep

MAIN_URL = "https://monocerus.pl/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTOS_DIR = os.path.join(BASE_DIR, '..', 'photos')
RESULTS_CATEGORIES_DIR = os.path.join(BASE_DIR, '..', 'results', 'categories.json')
RESULTS_PRODUCTSLINKS_DIR = os.path.join(BASE_DIR, '..', 'results', 'products_links.json')
RESULTS_PRODUCT_DETAILED_DIR = os.path.join(BASE_DIR, '..', 'results', 'product_detail.json')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_categories():
    
    results = []
    
    categories = {
        'category': None,
        'subcategories': []
    }

    print(f'Pobieranie ze strony: {MAIN_URL}')
    
    try:
        response = requests.get(MAIN_URL, headers=header, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        main_menu = soup.find('ul', class_="category-sub-menu")
        if not main_menu:
            print(f"Błąd: Nie znaleziono elementu za pomocą selektora. Sprawdź poprawność selektora.")
            return []
        
        all_main_lis = main_menu.select('li[data-depth="0"]')
    
        for li in all_main_lis:
            
            main_link = li.select_one('a:not([class])')
            if main_link:
                results.append({
                    'Poziom': 0,
                    'Typ': 'Kategoria Główna',
                    'Nazwa': main_link.get_text(strip=True),
                    'Link': main_link.get('href')
                })

            # B. Podkategorie (<a> z klasą 'category-sub-link') wewnątrz bieżącego <li>
            sub_category_links = li.select('a.category-sub-link')
            
            for sub_link in sub_category_links:
                parent_li = sub_link.find_parent('li')
                depth = parent_li.get('data-depth') if parent_li else 'N/A'
                
                results.append({
                    'Poziom': int(depth) if str(depth).isdigit() else depth,
                    'Typ': 'Podkategoria',
                    'Nazwa': sub_link.get_text(strip=True),
                    'Link': sub_link.get('href')
                })
                    
        return results
                                
    except Exception as e:
        print(f'Błąd: {e}')
        
    finally:
        sleep(1)
       
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
            # Znajdujemy wszystkie <li> na dowolnym poziomie (1, 2, ...)
            all_sub_lis = sub_menu_ul.find_all('li', recursive=False)
            
            # Funkcja pomocnicza do rekurencyjnego przetwarzania podkategorii
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
       
def main():
    kategorie = build_categories() 
        
    with open(RESULTS_CATEGORIES_DIR, 'w', encoding='utf-8') as f:
        json.dump(kategorie, f, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    main()