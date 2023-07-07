#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Python script that takes in a URL,\
sends a request to the URL and displays \
the body of the response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    """Don't execute if imported"""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8', 'replace'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
