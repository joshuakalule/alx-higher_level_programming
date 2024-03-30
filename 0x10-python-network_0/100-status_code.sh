#!/bin/bash
# task 7 - Only status code
curl -sI "$1" | awk 'NR==1 {print $2}' 
