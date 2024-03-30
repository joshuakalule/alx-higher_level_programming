#!/usr/bin/python3
"""Fetch the last 10 commits of a user."""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    r = requests.get(url, headers=headers)
    try:
        data = r.json()
        if len(data) > 0:
            for i, value in enumerate(data):
                if i > 10:
                    break
                sha = value.get('sha')
                author_name = value.get('commit').get('author').get('name')
                print(f"{sha}: {author_name}")
            exit(0)
    except ValueError as e:
        pass
    print(None)
