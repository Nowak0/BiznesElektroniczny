#!/bin/bash
cat backup/prestashop.sql | docker exec -i db1 mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop