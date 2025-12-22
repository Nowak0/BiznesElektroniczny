#!/bin/bash
set -euo pipefail

BACKUP_DIR="backup"

mkdir -p "$BACKUP_DIR"

rm -f \
  "$BACKUP_DIR/prestashop.sql" \
  "$BACKUP_DIR/img.tar.gz" \
  "$BACKUP_DIR/cod_module.tar.gz" \
  "$BACKUP_DIR/slider_module.tar.gz"

docker exec prestashop-db mysqldump --default-character-set=utf8mb4 -u root -pprestashop prestashop > "$BACKUP_DIR/prestashop.sql"

docker exec prestashop bash -lc "tar -C /var/www/html --exclude='**default**' -czf - img" > "$BACKUP_DIR/img.tar.gz"

docker exec prestashop tar -C /var/www/html/modules -czf - ps_cashondelivery > "$BACKUP_DIR/cod_module.tar.gz"
docker exec prestashop tar -C /var/www/html/modules -czf - ps_imageslider > "$BACKUP_DIR/slider_module.tar.gz"