# Background
This is a wrapper for the far Right Truth Social website API. It is built on the AIO HTTP module and designed to do research into the patterns of social media on the site and allow more integration like many competing sites.

# Basic Usage

## Implementation
The first step is to import the object and initialize your user. This takes in your truth email and password. Something of note passwords are sent in plaintext even on the truth site with no hashing to be seen.
```py
from TruthPy import User, Post, Feed


async def main():
    user = User()
    await user.login("email", "password")
```
## Make Post
Posting is made easy with the user object all you need to do is put their message using `user.post`

```py
await user.post("This was definitely not sent with python")
```

## Get Feed
Getting the feed is handled via the Users `feed` object. This object has three functions `get_feed`, `get_next` and `get_previous` these all return an array of `Post` objects which can also be accesed via `user.feed`

```py
current_feed = await user.feed.get_feed()
next_feed = await user.feed.get_next()
previous_feed = await user.feed.get_prev()
```

## Use Post Objects
Post objects have multiple datapoints that can be accesed along with the `.reply` function. This allows you to directly reply to a post rather than get ID and do it manually.

### List of Post Items
1. id: The post ID used to reply
2. created_at: Date and Time the post was made
3. reply_to: parent post id (may be none)
4. url: If you want to view this in browser
5.  replies: number of replies
6.  likes: number of likes
7.  content: Post content, this is formatted to markdown from the default HTML


## TODO
1. Get Posts via ID 
2. Get Post replies
3. Tasks related to other users, eg: follow, view followers etc.
