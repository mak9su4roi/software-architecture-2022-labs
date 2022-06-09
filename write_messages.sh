#!/bin/bash	

for x in {1..10}; do 
  curl -X 'POST' \
    'http://localhost:8080/facade_service/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d "{\"txt\": \"string-${x}\"}"
done