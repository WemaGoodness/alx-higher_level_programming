#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response,
handling HTTP errors.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print("Error code: {}".format(errh.response.status_code))
