#!/bin/bash
docker-compose -p prestashop -f docker-compose.yml up -d
./restore.sh