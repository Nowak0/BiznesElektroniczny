#!/bin/bash
set -euo pipefail

DB_CONTAINER="prestashop-db"
PS_CONTAINER="prestashop"
DB_NAME="prestashop"
DB_USER="root"
DB_PASS="prestashop"
DOMAIN="localhost"
PHYSICAL_URI="/"

docker-compose up -d --build

echo "[1/6] Import bazy danych..."
cat backup/prestashop.sql | docker exec -i "$DB_CONTAINER" mysql --default-character-set=utf8mb4 -u"$DB_USER" -p"$DB_PASS" "$DB_NAME"

echo "[2/6] Restore img..."
cat backup/img.tar.gz | docker exec -i "$PS_CONTAINER" tar xzf - -C /var/www/html
docker exec "$PS_CONTAINER" chown -R www-data:www-data /var/www/html/img

echo "[3/6] Restore module ps_cashondelivery..."
cat backup/cod_module.tar.gz | docker exec -i "$PS_CONTAINER" tar xzf - -C /var/www/html/modules
docker exec "$PS_CONTAINER" chown -R www-data:www-data /var/www/html/modules/ps_cashondelivery

echo "[4/6] Restore module ps_imageslider..."
cat backup/slider_module.tar.gz | docker exec -i "$PS_CONTAINER" tar xzf - -C /var/www/html/modules
docker exec "$PS_CONTAINER" chown -R www-data:www-data /var/www/html/modules/ps_imageslider

echo "[5/6] Post-restore FIX: domena/SSL (żeby nie było redirect loop)..."
docker exec -i "$DB_CONTAINER" mysql -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" <<SQL
-- Wymuszenie SSL w konfiguracji
UPDATE ${DB_NAME}.ps_configuration SET value = 1 WHERE name = 'PS_SSL_ENABLED';
UPDATE ${DB_NAME}.ps_configuration SET value = 1 WHERE name = 'PS_SSL_ENABLED_EVERYWHERE';

-- Najważniejsze: shop_url musi odpowiadać hostowi, na który wchodzi kolega
UPDATE ${DB_NAME}.ps_shop_url
SET domain = '${DOMAIN}',
    domain_ssl = '${DOMAIN}',
    physical_uri = '${PHYSICAL_URI}',
    virtual_uri = ''
WHERE main = 1;

-- Czasem pomaga też ujednolicenie tych kluczy (zależy od wersji/instalacji)
UPDATE ${DB_NAME}.ps_configuration SET value='${DOMAIN}' WHERE name IN ('PS_SHOP_DOMAIN','PS_SHOP_DOMAIN_SSL');
UPDATE ${DB_NAME}.ps_configuration SET value='${PHYSICAL_URI}' WHERE name='PS_SHOP_URI';
SQL

echo "[6/6] Czyszczenie cache PrestaShop..."
docker exec "$PS_CONTAINER" rm -rf /var/www/html/var/cache/*

echo "OK: Restore + fix zakończony."