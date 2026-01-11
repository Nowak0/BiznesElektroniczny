#!/bin/bash
DB_CONTAINER=$(docker ps --filter "name=admin-mysql_db" --format "{{.Names}}")
DB_NAME="BE_197633"
DB_USER="root"
DB_PASS="student"

cat prestashop.sql | docker exec -i $DB_CONTAINER mysql -u $DB_USER -p$DB_PASS $DB_NAME

SQL_COMMAND="
    UPDATE ps_configuration SET value = 1 WHERE name = 'PS_SSL_ENABLED';
    UPDATE ps_configuration SET value = 1 WHERE name = 'PS_SSL_ENABLED_EVERYWHERE';
    FLUSH PRIVILEGES;
"
docker exec -i $DB_CONTAINER mysql -u $DB_USER -p$DB_PASS $DB_NAME <<< "$SQL_COMMAND"
