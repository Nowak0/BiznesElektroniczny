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


def process_category_tree(node, parent_id=2):
    name = node["nazwa"]

    new_cat_id = create_category(name, parent_id)

    print(f"✔ Utworzono kategorię: {name} (ID: {new_cat_id}, parent: {parent_id})")

    for child in node.get("podkategorie", []):
        process_category_tree(child, new_cat_id)

def create_product(name, price, description, category_id):

    slug = name.lower().replace(" ", "-")

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

    <link_rewrite>
      <language id="2"><![CDATA[{slug}]]></language>
    </link_rewrite>

    <id_category_default><![CDATA[{category_id}]]></id_category_default>

    <associations>
      <categories>
        <category>
          <id><![CDATA[{category_id}]]></id>
        </category>
      </categories>
    </associations>

  </product>
</prestashop>
"""

    response = requests.post(
        f"{api_url}/products",
        data=xml.encode("utf-8"),
        headers={"Content-Type": "application/xml"},
        auth=(api_key, "")
    )

    print(response.text)
    return extract_id_from_xml(response.text)



if __name__ == "__main__":
    # create_category("super kategoria")
    create_product("super produkt", 23.33, """<div class="tabs">
		
							<h3>Opis</h3>	
				
				 <div class="product-description"><p>Breyer Stablemates 6958 - Appaloosa</p>
<p>Breyer Stablemate (1:32) 6958 - Appaloosa</p>
<p>Wymiary figurki około:&nbsp;</p>
<p>Konie malowane są ręcznie z dbałością o szczegóły, poszczególne egzemplarze mogą się od siebie nieznacznie różnić.</p>
<p>Zabawka przeznaczona dla dzieci powyżej 4 lat.</p>
<p>Wszystkie zabawki&nbsp;posiadają certyfikat CE - Znak ten jest wyznacznikiem wysokiej jakości produktów.<br>Zabawki z tym znakiem są bezpieczne, nie zawierają szkodliwych dla zdrowia barwników i materiałów.</p></div>
				
						
			
						<h3>Szczegóły produktu</h3>
			
			   <div>
  
          <div class="product-manufacturer">
                  <label class="label">Marka</label>
          <span>
            <a href="https://monocerus.pl/brand/4-breyer-stablemates">Breyer Stablemates</a>
          </span>
              </div>
          

  
          <div class="product-quantities">
        <label class="label">W magazynie</label>
        <span data-stock="11" data-allow-oosp="0">11 Przedmioty</span>
      </div>
      

  
      

  
    <div class="product-out-of-stock">
      
    </div>
  

  
      

    
      

  
          <div class="product-condition">
        <label class="label">Stan: </label>
        <link href="https://schema.org/NewCondition">
        <span>Nowość</span>
      </div>
      
</div>			
			
				
						
			                <h3>Bezpieczeństwo produktu</h3>
				<p></p><div class="x13gpsr x13gpsr-shop-1 x13gpsr--displayProductExtraContent">
        <p class="x13gpsr__list">
  <strong class="x13gpsr__item x13gpsr__title">Producent</strong>
  <span class="x13gpsr__item">    Reeves International, Inc.</span>
  <span class="x13gpsr__item">Industrial Road 14</span>
  <span class="x13gpsr__item">NJ 07440
    Pequannock</span>
  <span class="x13gpsr__item">Stany Zjednoczone</span>
    <span class="x13gpsr__item"><a href="mailto:info@reevesintl.com">info@reevesintl.com</a></span>
    </p>

  <div class="x13gpsr__extraNote">
    <p><picture><source srcset="https://monocerus.pl/img/cms/ce-128.webp" type="image/webp"><img src="https://monocerus.pl/img/cms/ce-128.png" alt="" width="83" height="50"></picture><picture><source srcset="https://monocerus.pl/img/cms/ukca.webp" type="image/webp"><img src="https://monocerus.pl/img/cms/ukca.png" alt="" width="50" height="50"></picture><picture><source srcset="https://monocerus.pl/img/cms/0-3-128.webp" type="image/webp"><img src="https://monocerus.pl/img/cms/0-3-128.png" width="50" height="50"></picture><img src="https://monocerus.pl/img/cms/4+.png" alt="" width="50" height="50"></p>
<p>wyjaśnienie oznaczeń na produkcie:&nbsp;<a href="https://monocerus.pl/content/6-oznaczenia-na-produktach">https://monocerus.pl/content/6-oznaczenia-na-produktach</a></p>
  </div>

    <p class="x13gpsr__list">
  <strong class="x13gpsr__item x13gpsr__title">Osoba odpowiedzialna</strong>
  <span class="x13gpsr__item">Beppe</span>
  <span class="x13gpsr__item">Obrońców Poczty Gdańskiej 95</span>
  <span class="x13gpsr__item">42-400
    Zawiercie</span>
  <span class="x13gpsr__item">Polska</span>
    <span class="x13gpsr__item"><a href="mailto:bok@beppe.pl">bok@beppe.pl</a></span>
    </p>


    <div class="x13gpsr__informations">
        
    </div>
</div><p></p>
			              </div>""", 4)
    # with open("../scraper/results/categories.json") as f:
    #     data = json.load(f)
    #     for node in data:
    #         process_category_tree(node)
