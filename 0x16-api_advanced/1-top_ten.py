#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
       the first 10 hot posts listed for a given subreddit."""
    headers = {'User-Agent': 'Aget 007'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'limit': 10}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params=parameters
    )
    if response.status_code == 200:
        for post in response.json().get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        print(None)
