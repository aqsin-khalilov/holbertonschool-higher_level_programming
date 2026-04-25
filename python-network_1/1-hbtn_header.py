#!/usr/bin/python3
"""
This script takes a URL as an argument, sends a request to it,
and displays the value of the 'X-Request-Id' variable found
in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Create a request object
    req = urllib.request.Request(url)

    # Adding the required header to bypass the intranet firewall
    req.add_header('cfclearance', 'true')

    # Send the request and use 'with' to handle the response
    with urllib.request.urlopen(req) as response:
        # Access the headers of the response
        headers = response.info()

        # Use get to fetch the specific header value to avoid exceptions
        request_id = headers.get('X-Request-Id')

        # Print the value
        print(request_id)
