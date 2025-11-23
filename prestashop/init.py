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

    if response.status_code not in (200, 201):
        return -1,-1, response.content

    return extract_id_from_xml(str(response.content)), extract_stock_available_id(str(response.content)), response.content


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
    errors = 0
    successes = 0
    for p in product_list:
        name = p["name"]
        price = p["price"]
        description = p.get("szczegoly_html", "")
        description_short = p.get("opis_html", "")
        categories = p.get("kategorie", [])
        cat_ids = []

        for cat in categories:
            cat_ids.append(categories_dict[cat])

        product_id, stock_id, response = create_product(name, price, description, description_short, cat_ids)

        if product_id != -1:
            update_stock(stock_id, product_id, random.randint(1,10))
            successes += 1
        else:
            print(f"=======PRODUKT NAME: {name}=======")
            print(response)

            errors += 1
        # print(f"Utworzono produkt:\n", f"- name: {name}")
    print(f"dodano: {successes}\n errory: {errors}")

def main():
    categories = {}

    with open("../scraper/results/categories.json") as f:
        data = json.load(f)
        for node in data:
            process_category_tree(node, categories)

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
    # for i in range(55,61):
    #     delete_product(i)

