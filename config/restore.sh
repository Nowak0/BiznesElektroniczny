#!/bin/bash
cat prestashop.sql | docker exec -i prestashop-db mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop
cat img.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html
docker exec prestashop chown -R www-data:www-data /var/www/html/img
cat cod_module.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/modules
docker exec prestashop chown -R www-data:www-data /var/www/html/modules/ps_cashondelivery