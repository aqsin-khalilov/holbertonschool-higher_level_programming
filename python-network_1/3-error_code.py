#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
It manages urllib.error.HTTPError exceptions to print the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Create a request object
    req = urllib.request.Request(url)

    # Adding the required header to bypass the intranet firewall
    req.add_header('cfclearance', 'true')

    try:
        # Try to open the URL and read the response
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Catch HTTP errors (e.g., 401, 404, 500) and print the status code
        print("Error code: {}".format(e.code))
