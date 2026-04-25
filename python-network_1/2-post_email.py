#!/usr/bin/python3
"""
This script takes a URL and an email address as arguments,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response decoded in UTF-8.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent as a dictionary
    values = {'email': email}

    # Encode the data into a format suitable for a URL (URL-encoded)
    # Then convert the string into bytes (required for POST requests)
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # Create the request object
    req = urllib.request.Request(url, data)

    # Adding the required header to bypass the intranet firewall
    req.add_header('cfclearance', 'true')

    # Send the POST request and handle the response
    with urllib.request.urlopen(req) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')
        print(body)
