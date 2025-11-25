#!/bin/bash
docker exec prestashop-db mysqldump --default-character-set=utf8mb4 -u root -pprestashop prestashop > prestashop.sql
docker exec prestashop bash -lc "tar -C /var/www/html --exclude='**default**' -czf - img" > img.tar.gz
docker exec prestashop tar -C /var/www/html/modules -czf - ps_cashondelivery > cod_module.tar.gz