#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""script that takes in repository name and owner name \
and list 10 commits (from the most recent to oldest)"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
