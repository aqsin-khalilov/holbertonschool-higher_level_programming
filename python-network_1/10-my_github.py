#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's ID.
It uses Basic Authentication to access the information.
"""
import requests
import sys


if __name__ == "__main__":
    # Get username and token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API endpoint for the authenticated user
    url = "https://api.github.com/aqsin-khalilov"

    # Using Basic Authentication with username and token
    # requests.get automatically handles the Auth header when auth is passed
    response = requests.get(url, auth=(username, token))

    try:
        # Parse the response as JSON
        json_data = response.json()
        # Display the 'id' field from the JSON response
        # Using .get() returns None if 'id' is not present (e.g. wrong credentials)
        print(json_data.get('id'))
    except ValueError:
        # In case the response is not a valid JSON
        print("None")
