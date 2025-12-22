$ErrorActionPreference = "Stop"

# Katalog na backup (na hoście)
$backupDir = Join-Path (Get-Location) "backup"

# Uruchom wszystko w CMD (ważne dla binarnego przekierowania >)
cmd /c "if not exist backup mkdir backup"
cmd /c "del /q backup\prestashop.sql backup\img.tar.gz backup\cod_module.tar.gz backup\slider_module.tar.gz 2>nul"

cmd /c "docker exec -i prestashop-db mysqldump --default-character-set=utf8mb4 -u root -pprestashop prestashop > .\backup\prestashop.sql"
cmd /c 'docker exec -i prestashop bash -lc "tar -C /var/www/html --exclude=*default* -czf - img" > .\backup\img.tar.gz'
cmd /c "docker exec -i prestashop tar -C /var/www/html/modules -czf - ps_cashondelivery > .\backup\cod_module.tar.gz"
cmd /c "docker exec -i prestashop tar -C /var/www/html/modules -czf - ps_imageslider > .\backup\slider_module.tar.gz"