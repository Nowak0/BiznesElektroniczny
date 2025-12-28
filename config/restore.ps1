# restore-prestashop.ps1
# Najprostsza wersja: wszystko leci przez CMD, bez zmiennych.

cmd /c "type backup\prestashop.sql | docker exec -i prestashop-db mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop"

cmd /c "type backup\img.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html"
cmd /c "docker exec prestashop chown -R www-data:www-data /var/www/html/img"

cmd /c "type backup\menu_module.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/modules"
cmd /c "docker exec prestashop chown -R www-data:www-data /var/www/html/modules/ps_mainmenu"

cmd /c "type backup\slider_module.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/modules"
cmd /c "docker exec prestashop chown -R www-data:www-data /var/www/html/modules/ps_imageslider"