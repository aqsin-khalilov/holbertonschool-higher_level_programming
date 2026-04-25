#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter 'q'.
It handles the JSON response from the server.
"""
import requests
import sys


if __name__ == "__main__":
    # Check if an argument was provided, otherwise set q to an empty string
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}
    # Custom headers to bypass the intranet firewall
    headers = {'cfclearance': 'true'}

    try:
        # Sending the POST request
        response = requests.post(url, data=payload, headers=headers)
        # Try to parse the response as JSON
        json_data = response.json()

        if not json_data:
            # If JSON is an empty dictionary
            print("No result")
        else:
            # If JSON contains user data, display [id] name
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))

    except ValueError:
        # If response.json() fails because the content is not valid JSON
        print("Not a valid JSON")
