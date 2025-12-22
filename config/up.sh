#!/bin/bash
docker-compose up --build -d
./init-ssl.sh
./restore.sh