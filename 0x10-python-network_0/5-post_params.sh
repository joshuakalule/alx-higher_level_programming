#!/bin/bash
#task 5 - cURL POST parameters
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
