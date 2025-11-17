#!/bin/bash
set -e

cd themes/osiema/_dev

if [ ! -d "node_modules" ]; then
  npm install
fi

npm run watch