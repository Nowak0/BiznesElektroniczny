import json
import re

import requests

api_url = "http://localhost:8080/api"
api_key = "QSP3GTBTPDJ7MJR9KYN2TSS8KB2V28MY"


def extract_id_from_xml(xml_text):
    match = re.search(r"<id[^>]*><!\[CDATA\[(\d+)\]\]></id>", xml_text)
    if match:
        return int(match.group(1))

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
          <language id="1"><![CDATA[{name}]]></language>
        </name>

        <link_rewrite>
          <language id="1"><![CDATA[{slug}]]></language>
        </link_rewrite>

        <description>
          <language id="1"><![CDATA[]]></language>
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
        raise Exception("Nie udalo sie stworzyc kategorii")


def process_category_tree(node, parent_id=2):
    name = node["nazwa"]

    new_cat_id = create_category(name, parent_id)

    print(f"✔ Utworzono kategorię: {name} (ID: {new_cat_id}, parent: {parent_id})")

    for child in node.get("podkategorie", []):
        process_category_tree(child, new_cat_id)


if __name__ == "__main__":
    with open("../scraper/results/categories.json") as f:
        data = json.load(f)
        for node in data:
            process_category_tree(node)
