#!/bin/bash
cat backup/prestashop.sql | docker exec -i db1 mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop
cat backup/img.tar.gz | docker exec -i presta1 tar xzf - -C /var/www/html
docker exec presta1 chown -R www-data:www-data /var/www/html/img
cat backup/menu_module.tar.gz | docker exec -i presta1 tar xzf - -C /var/www/html/modules
docker exec presta1 chown -R www-data:www-data /var/www/html/modules/ps_mainmenu
cat backup/slider_module.tar.gz | docker exec -i presta1 tar xzf - -C /var/www/html/modules
docker exec presta1 chown -R www-data:www-data /var/www/html/modules/ps_imageslider