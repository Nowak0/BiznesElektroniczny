type prestashop.sql | docker exec -i prestashop-db mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop
type img.tar.gz | docker exec -i prestashop-app tar xzf - -C /
docker exec prestashop-app chown -R www-data:www-data /var/www/html/img