#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user' with the letter as a parameter.
"""
import requests
import requests.exceptions
import sys


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, {'q': f"{letter}"})
    try:
        data = r.json()
        if len(data) > 0:
            id = data.get('id')
            name = data.get('name')
            print(f"[{id}]: {name}")
        else:
            print('No result')
    except ValueError as e:
        print('Not a valid JSON')
