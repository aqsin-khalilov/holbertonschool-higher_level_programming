#!/usr/bin/python3
"""
This script fetches a specific URL using the requests package
and displays the body of the response with specific formatting.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    # Custom headers to bypass the intranet firewall
    headers = {'cfclearance': 'true'}
    # Sending the GET request
    response = requests.get(url, headers=headers)
    # Getting the text content of the response
    content = response.text

    print("Body response:")
    # requests automatically decodes the response into a string
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
