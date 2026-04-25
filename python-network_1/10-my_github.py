#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's ID.
It uses Basic Authentication and custom headers for the firewall.
"""
import requests
import sys


if __name__ == "__main__":
    # Get username and token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API endpoint
    url = "https://api.github.com/user"

    # Custom headers to bypass the intranet firewall
    headers = {'cfclearance': 'true'}

    # Sending GET request with Basic Authentication and headers
    response = requests.get(url, auth=(username, token), headers=headers)

    try:
        # Parse the response as JSON
        json_data = response.json()
        # Get the 'id' field
        print(json_data.get('id'))
    except ValueError:
        # If the response is not valid JSON
        print("None")
