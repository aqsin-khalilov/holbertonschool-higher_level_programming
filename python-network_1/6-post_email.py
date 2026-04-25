#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request
to the URL with the email as a parameter, and displays the body
of the response.
"""
import requests
import sys


if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # The payload to be sent in the POST request
    payload = {'email': email}

    # Custom headers to bypass the intranet firewall
    headers = {'cfclearance': 'true'}

    # Sending the POST request with the data
    response = requests.post(url, data=payload, headers=headers)

    # Display the body of the response
    print(response.text)
