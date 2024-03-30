#!/usr/bin/python3
"""
Takes your Github credentials and uses the
Github API to display your id.
"""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    url = f'https://api.github.com/users/{username}'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    r = requests.get(url, headers=headers)
    try:
        data = r.json()
        if len(data) > 0:
            print(data.get('id'))
            exit(0)
    except ValueError as e:
        pass
    print(None)
