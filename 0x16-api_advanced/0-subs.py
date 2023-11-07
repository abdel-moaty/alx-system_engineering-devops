#!/usr/bin/python3
""""Queries the Reddit API and returns the number of subscribers
for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """"Queries the Reddit API and returns the number of subscribers
        for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Agent 007'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
