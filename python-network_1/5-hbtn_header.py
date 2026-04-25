#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.
It uses the requests and sys packages.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]
    # Custom headers to bypass the intranet firewall
    headers = {'cfclearance': 'true'}

    # Sending the GET request
    response = requests.get(url, headers=headers)

    # Accessing the headers dictionary of the response
    # We use .get() to safely access the key
    request_id = response.headers.get('X-Request-Id')

    # Print the result
    print(request_id)
