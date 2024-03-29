#!/bin/bash
# task 3 - cURL only methods
curl -sI -X "OPTIONS" "$1" | grep '^Allow:' | awk -F': ' '{print $2}'
