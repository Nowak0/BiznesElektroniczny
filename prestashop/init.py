import json
import random
import re

import requests

api_url = "http://localhost:8080/api"
api_key = "QSP3GTBTPDJ7MJR9KYN2TSS8KB2V28MY"


def extract_id_from_xml(xml_text):
    match = re.search(r"<id[^>]*><!\[CDATA\[(\d+)\]\]></id>", xml_text)
    if match:
        return int(match.group(1))

    raise ValueError("Nie znaleziono ID w odpowiedzi API:\n" + xml_text)


def extract_stock_available_id(xml_text):
    pattern = r'stock_availables/(\d+)'  # szuka "stock_availables/<id>"
    match = re.search(pattern, xml_text)
    if match:
        return match.group(1)

    raise ValueError("Nie znaleziono ID w odpowiedzi API:\n" + xml_text)


def create_category(name, parent_id=2):
    slug = (
        name.lower()
        .replace(" ", "-")
        .replace("ą", "a").replace("ć", "c").replace("ę", "e")
        .replace("ł", "l").replace("ń", "n").replace("ó", "o")
        .replace("ś", "s").replace("ź", "z").replace("ż", "z")
    )

    xml = f"""
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
      <category>
        <id><![CDATA[]]></id>
        <id_parent><![CDATA[{parent_id}]]></id_parent>
        <active><![CDATA[1]]></active>

        <is_root_category><![CDATA[0]]></is_root_category>

        <name>
          <language id="2"><![CDATA[{name}]]></language>
        </name>

        <link_rewrite>
          <language id="2"><![CDATA[{slug}]]></language>
        </link_rewrite>

        <description>
          <language id="2"><![CDATA[]]></language>
        </description>

      </category>
    </prestashop>
    """

    response = requests.post(
        f"{api_url}/categories",
        data=xml.encode('utf-8'),
        headers={'Content-Type': 'application/xml'},
        auth=(api_key, '')
    )

    if response.status_code in (200, 201):
        cat_id = extract_id_from_xml(response.text)
        print("Utworzono kategorię:\n", f"- id: {cat_id}\n - name: {name}")
        return cat_id
    else:
        raise Exception(response.text)


def process_category_tree(node, categories, parent_id=2):
    name = node["nazwa"]

    new_cat_id = create_category(name, parent_id)
    categories[name] = new_cat_id

    print(f"✔ Utworzono kategorię: {name} (ID: {new_cat_id}, parent: {parent_id})")

    for child in node.get("podkategorie", []):
        process_category_tree(child, categories, new_cat_id)


def create_product(name, price, description, description_short, categories):
    slug = name.lower().replace(" ", "-")

    categories_xml = "\n".join(
        f"""
            <category>
                <id><![CDATA[{cid}]]></id>
            </category>
            """ for cid in categories
    )

    xml = f"""
            <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
              <product>
                <id><![CDATA[]]></id>
                <name>
                  <language id="2"><![CDATA[{name}]]></language>
                </name>
                <price><![CDATA[{price}]]></price>
                <active><![CDATA[1]]></active>
            
                <description>
                  <language id="2"><![CDATA[{description}]]></language>
                </description>
                
                <description_short>
                  <language id="2"><![CDATA[{description_short}]]></language>
                </description_short>
            
                <link_rewrite>
                  <language id="2"><![CDATA[{slug}]]></language>
                </link_rewrite>
                
                <id_category_default><![CDATA[{categories[0]}]]></id_category_default>
                <associations>
                  <categories>
                    {categories_xml}
                  </categories>
                </associations>
                
                <state><![CDATA[1]]></state>
                <available_for_order><![CDATA[1]]></available_for_order>
                <show_price><![CDATA[1]]></show_price>
            
              </product>
            </prestashop>
            """

    response = requests.post(
        f"{api_url}/products",
        data=xml.encode("utf-8"),
        headers={"Content-Type": "application/xml"},
        auth=(api_key, "")
    )

    return extract_id_from_xml(str(response.content)), extract_stock_available_id(str(response.content))


def update_stock(stock_id, product_id, quantity):
    xml = f"""
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
      <stock_available>
        <id><![CDATA[{stock_id}]]></id>

        <id_product><![CDATA[{product_id}]]></id_product>
        <id_product_attribute><![CDATA[0]]></id_product_attribute>

        <id_shop><![CDATA[1]]></id_shop>
        <id_shop_group><![CDATA[0]]></id_shop_group>

        <quantity><![CDATA[{quantity}]]></quantity>

        <depends_on_stock><![CDATA[0]]></depends_on_stock>
        <out_of_stock><![CDATA[2]]></out_of_stock>

        <location><![CDATA[]]></location>
      </stock_available>
    </prestashop>
    """

    response = requests.put(
        f"{api_url}/stock_availables/{stock_id}",
        data=xml.encode('utf-8'),
        headers={"Content-Type": "application/xml"},
        auth=(api_key, "")
    )

    return response.status_code, response.text


def process_products(product_list, categories_dict):
    for p in product_list:
        name = p["name"]
        price = p["price"]
        description = p.get("szczegoly_html", "")
        description_short = p.get("opis_html", "")
        categories = p.get("kategorie", [])
        cat_ids = []

        for cat in categories:
            cat_ids.append(categories_dict[cat])

        product_id, stock_id = create_product(name, price, description, description_short, cat_ids)

        update_stock(stock_id, product_id, random.randint(1,10))

        print(f"Utworzono produkt:\n", f"- name: {name}")


def main():
    # categories = {}
    categories = {'1,5 mm': 151, '3 mm': 152, 'APOXIE': 155, 'Afryka': 203, 'Akcesoria': 141, 'Akcesoria Breyer': 58,
                  'Akcesoria i lalki': 56, 'Ameryka Południowa': 208, 'Ameryka Północna': 207, 'Antarktyda': 206,
                  'Artist Resin': 35, 'Australia': 205, 'Azja': 202, 'Breyer': 39, 'Bullyland': 117, 'Classics': 45,
                  'CollectA': 68, 'Dekoracje': 161, 'Dinozaury': 164, 'Dom i zagroda': 79, 'Długopisy': 160,
                  'Europa': 204, 'Fantasy': 114, 'Fantazyjne': 88, 'Fantazyjne i dekory': 63, 'Figurki żywiczne': 62,
                  'Flamingi': 184, 'Gabloty z replikami': 90, 'Gady': 172, 'Gadżety': 158, 'Gryzonie': 188,
                  'Jaszczurki': 175, 'Jednorożce': 38, 'Jednorożec Pummel': 118, 'Jeźdźcy': 133, 'Kaczkowate': 180,
                  'Kalendarze adwentowe': 209, 'Konie': 111, 'Konie i kuce': 163, 'Konie skala 1:12': 82,
                  'Kontynenty': 201, 'Kotowate': 189, 'Krokodyle': 176, 'Kubki': 159, 'Kuce i konie': 78, 'Kury': 183,
                  'Kącik artysty': 145, 'Lalki': 47, 'Lalki Breyer': 57, 'Ludzie i akcesoria': 122,
                  'Materiał pikowany': 157, 'Metry': 149, 'Mini Whinnies': 53, 'Mięczaki': 199,
                  'Modele do malowania': 154, 'Modele koni': 51, 'Modele koni Isabell Werth': 139, 'Modele koni MW': 54,
                  'Modele specjalne': 166, 'Mojo': 110, 'Naczelne': 190, 'Niedźwiedziowate': 191, 'Nieloty lądowe': 181,
                  'Nieloty wodne': 179, 'Nowości 2017': 77, 'Nowości 2018': 76, 'Nowości 2019': 75, 'Nowości 2020': 74,
                  'Nowości 2021': 73, 'Nowości 2022': 72, 'Nowości 2023': 71, 'Nowości 2024': 70, 'Nowości 2025': 69,
                  'OUTLET': 67, 'Outlet': 162, 'Owady': 84, 'Papo': 130, 'Pawie': 182, 'Podstawki': 138,
                  'Podstawki do modeli': 144, 'Prehistoryczne': 81, 'Przeszkody': 142, 'Psowate': 192,
                  'Psy i koty': 128, 'Ptaki': 177, 'Płazy': 171, 'Rio Rondo': 156, 'Rolki': 148, 'Rośliny': 89,
                  'Ryby': 168, 'Safari Ltd': 124, 'Schleich': 94, 'Schleich - Harry Potter™': 99,
                  'Schleich - Ludzie i akcesoria': 96, 'Schleich - Nowości 2020': 106, 'Schleich - Nowości 2021': 105,
                  'Schleich - Nowości 2022': 104, 'Schleich - Nowości 2023': 103, 'Schleich - Nowości 2024': 102,
                  'Schleich - Nowości 2025': 101, 'Schleich - gospodarstwo i dom': 97, 'Schleich - konie i kuce': 95,
                  'Schleich - zwierzęta dzikie': 98, 'Schleich Exclusive': 100, 'Seria Deluxe': 87,
                  'Serie zakończone': 37, 'Sokoły': 185, 'Southlands Replicas': 109, 'Sowy': 178, 'Ssaki': 187,
                  'Stablemates': 50, 'Stajnie': 60, 'Stawonogi': 200, 'Stekowce': 193, 'Stojaki i wieszaki': 143,
                  'Sznurek / Linka 1 mm': 146, 'Słodkowodne': 169, 'Słonowodne': 170, 'Torbacze': 195,
                  'Traditional': 40, 'Trąbowce': 198, 'WIA': 136, 'Wodne': 86, 'Wołowate': 196, 'Wróblowate': 186,
                  'Wstążki rypsowe': 147, 'Wstążki satynowe': 150, 'Wycofane Breyer': 64, 'Wycofane Bullyland': 123,
                  'Wycofane CollectA': 91, 'Wycofane Mojo': 115, 'Wycofane Safari Ltd.': 129, 'Wycofane Schleich': 108,
                  'Wycofane WIA': 140, 'Węże': 174, 'Zajęczaki': 197, 'Zestawy': 92, 'Zestawy Breyer': 59,
                  'Zestawy MW': 55, 'Zestawy kreatywne': 61, 'Zwierzęta': 167, 'Zwierzęta domowe': 134,
                  'Zwierzęta dzikie': 132, 'a.manufaktura': 36, 'sznurek 2 mm': 153, 'Świat Bayala': 107,
                  'Świat fantastyczny': 135, 'Świniowate': 194, 'Żółwie': 173}
    # with open("../scraper/results/categories.json") as f:
    #     data = json.load(f)
    #     for node in data:
    #         process_category_tree(node, categories)

    with open("../scraper/results/products_links.json") as f:
        data = json.load(f)
        process_products(data, categories)


def delete_product(id):
    requests.delete(
        f"{api_url}/products/{id}",
        auth=(api_key, "")
    )


if __name__ == "__main__":
    main()
    # create_product("test", 12.2, "opis", "krótki opis", 2)
    # for i in range(38,55):
    #     delete_product(i)

