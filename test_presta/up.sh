#!/bin/bash
docker-compose -p prestashop-test -f docker-compose.test.yml up -d
./restore.sh