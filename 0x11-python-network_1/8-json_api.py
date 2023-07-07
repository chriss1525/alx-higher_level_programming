#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""script that takes in a letter\
and sends a POST request to http://0.0.0.0:5000/search_user\
with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        r_dict = r.json()
        if r_dict:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
