#!/bin/bash
# task 8 - cURL a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @- "$1" < "$2"
