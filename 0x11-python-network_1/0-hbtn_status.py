#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""script that fetches https://intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    """Fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        body_response = response.read()

print('Body response:\n\t- type: {}'.format(type(body_response)))
print('\t- content: {}'.format(body_response))
print('\t- utf8 content: {}'.format(body_response.decode('utf-8')))
