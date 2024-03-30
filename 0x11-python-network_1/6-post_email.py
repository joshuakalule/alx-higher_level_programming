#!/usr/bin/python3
"""
Script takes in URL and email address,
sends POST request to the passed URL with email as a parameter,
then displays the body of the response.
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
