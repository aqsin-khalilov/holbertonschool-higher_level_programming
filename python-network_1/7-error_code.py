#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints 'Error code:' followed by the value of the status code.
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

    # Check if the status code indicates an error (>= 400)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        # If successful, print the body of the response
        print(response.text)
