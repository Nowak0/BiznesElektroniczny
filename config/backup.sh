docker exec prestashop-db mysqldump --default-character-set=utf8mb4 -u root -pprestashop prestashop > prestashop.sql
docker exec prestashop tar czf - /var/www/html/img > img.tar.gz