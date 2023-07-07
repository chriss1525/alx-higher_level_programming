#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" script that takes your GitHub credentials (username and password) \
and uses the GitHub API to display your id"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    try:
        username = argv[1]
        password = argv[2]

        r = requests.get(url, auth=(username, password))
        if r.status_code == 400:
            print("None")
        print(r.json().get('id'))
    except:
        print("None")
    
