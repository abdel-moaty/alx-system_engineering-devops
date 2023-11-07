#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles
       of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 25, "after": after}
    headers = {"User-Agent": "Agent 007"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    else:
        return None
