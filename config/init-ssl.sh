#!/bin/bash

DB_CONTAINER="prestashop-db"
DB_NAME="prestashop"
DB_USER="root"
DB_PASS="prestashop"

if [ "$(docker ps -q -f name=$DB_CONTAINER)" ]; then
    echo "Kontener znaleziony."
else
    echo "BŁĄD: Kontener $DB_CONTAINER nie jest uruchomiony."
    exit 1
fi

SQL_COMMAND="
    UPDATE ps_configuration SET value = 1 WHERE name = 'PS_SSL_ENABLED';
    UPDATE ps_configuration SET value = 1 WHERE name = 'PS_SSL_ENABLED_EVERYWHERE';
    FLUSH PRIVILEGES;
"

docker exec -i $DB_CONTAINER mysql -u $DB_USER -p$DB_PASS $DB_NAME <<< "$SQL_COMMAND"

if [ $? -eq 0 ]; then
    echo "Konfiguracja SSL pomyślnie ustawiona w bazie danych."
else
    echo "BŁĄD: Wystąpił problem podczas wykonywania polecenia SQL."
fi
