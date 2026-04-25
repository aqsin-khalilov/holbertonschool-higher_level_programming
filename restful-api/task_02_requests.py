#!/usr/bin/python3
"""
Module to fetch data from an API and process it into different formats.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        # Parse fetched data into a JSON object
        posts = response.json()

        # Iterate and print titles
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts and saves them into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure the data into a list of dictionaries
        # We only need id, title, and body
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Using csv module to write into posts.csv
        filename = "posts.csv"
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            # Write the header and the rows
            writer.writeheader()
            writer.writerows(structured_data)
