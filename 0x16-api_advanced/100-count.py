#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords."""

import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Queries the Reddit API, parses the title of all hot articles,
       and prints a sorted count of given keywords."""
    if counts is None:
        counts = {}
    if after is None:
        headers = {'User-Agent': 'Agent 007'}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        headers = {'User-Agent': 'Agent 007', 'after': after}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get('data', {})
    after = data.get('after')
    children = data.get('children', [])
    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            if re.search(fr'\b{re.escape(word)}\b', title):
                counts[word] = counts.get(word, 0) + 1
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
