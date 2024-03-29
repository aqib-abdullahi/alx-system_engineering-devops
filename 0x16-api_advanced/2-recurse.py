#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing titles 
of all hot articles forva subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)
    payload = {'after': after, 'limit': '100'}
    user_agent = {'User-Agent': 'Python/requests'}
    res = requests.get(api_uri, headers=user_agent,
                       params=payload, allow_redirects=False)
    if res.status_code == 200:
        res = res.json()
        hot_posts = res.get('data').get('children')
        after = res.get('data').get('after')
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
