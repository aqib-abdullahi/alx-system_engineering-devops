#!/usr/bin/python3
"""Queries Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)
    user_agent = {'User-Agent': 'Python/requests'
    res = requests.get(api_uri, headers=user_agent,
                       allow_redirect=False)
    if res.status_code in [302, 404]:
        return 0

    return res.json().get('data').get('subscribers')
