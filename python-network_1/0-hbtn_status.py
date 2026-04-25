#!/usr/bin/python3
"""
This script fetches a specific URL using the urllib package
and displays the body of the response with specific formatting.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    
    # Create a request object to add custom headers
    req = urllib.request.Request(url)
    
    # Adding the required header to bypass the intranet firewall
    req.add_header('cfclearance', 'true')

    # Using 'with' statement to ensure the resource is closed automatically
    with urllib.request.urlopen(req) as response:
        content = response.read()
        
        print("Body response:")
        # Display the type of the content (bytes)
        print("\t- type: {}".format(type(content)))
        # Display the raw content
        print("\t- content: {}".format(content))
        # Display the content decoded into utf-8 string
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
