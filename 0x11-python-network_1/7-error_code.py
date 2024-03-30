#!/usr/bin/python3
"""
Script takes in a URL,
sends a request to the URL and displays the body.
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.status_code)
