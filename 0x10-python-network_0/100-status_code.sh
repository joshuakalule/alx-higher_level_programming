#!/bin/bash
# task 7 - Only status code
curl -sw "%{response_code}\n" -o /dev/null "$1" 
