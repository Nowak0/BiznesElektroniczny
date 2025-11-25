type prestashop.sql | docker exec -i prestashop-db mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop
type img.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/img
docker exec prestashop chown -R www-data:www-data /var/www/html/img/p
type cod_module.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/modules
docker exec prestashop chown -R www-data:www-data /var/www/html/modules/ps_cashondelivery