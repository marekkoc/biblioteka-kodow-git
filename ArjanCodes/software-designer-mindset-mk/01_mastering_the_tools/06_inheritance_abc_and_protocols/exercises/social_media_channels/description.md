# 1. Social media channels

You just landed a job at "SocialOverlord", a company developing a SaaS product allowing you to write and schedule posts to a variety of social networks.

The whole backend is written in Python (yay!), but unfortunately, the person you're replacing didn't know classes exist (ehrm...) and so they used tuples to represent all the data in the system (not so yay...). Here's a code example:

```python
# each social channel has a type
# and the current number of followers
SocialChannel = tuple[str, int]

# each post has a message and the timestamp when it should be posted
Post = tuple[str, int]

def post_a_message(channel: SocialChannel, message: str) -> None:
    type, _ = channel
    if type == "youtube":
        post_to_youtube(channel, message)
    elif type == "facebook":
        post_to_facebook(channel, message)
    elif type == "twitter":
        post_to_twitter(channel, message)

def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post
        for channel in channels:
            if timestamp <= time():
                post_a_message(channel, message)
```

## a) From tuples to classes

Refactor this code so that it uses classes instead of tuples to represent social channels and posts. As a starting point, use the code download for this exercise.

Compatible Python Versions: 3.9+