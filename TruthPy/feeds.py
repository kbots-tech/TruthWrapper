from TruthPy.urls import FEED_URL
from TruthPy.utils import request_json
from TruthPy.posts import Post

class Feed:
    def __init__(self, token):
        self.token = token
        self.feed = []
        self.next = None
        self.prev = None

    async def get_feed(self):
        response = await request_json(
            FEED_URL,
            method="GET",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        self.feed = await self.post_array(response['feed'])
        self.next = response['next']
        self.prev = response['prev']
        return self.feed

    async def get_next(self):
        response = await request_json(
            self.next,
            method="GET",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        self.feed = await self.post_array(response['feed'])
        self.next = response['next']
        self.prev = response['prev']
        return self.feed

    async def get_prev(self):
        response = await request_json(
            self.prev,
            method="GET",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        
        self.feed = await self.post_array(response['feed'])
        self.next = response['next']
        self.prev = response['prev']
        return self.feed


    async def post_array(self, posts):
        post_array = []
        for post in posts:
            post_array.append(Post(post['id'], post['created_at'], post['in_reply_to_id'], post['url'], post['replies_count'], post['favourites_count'], post['content']))
        return post_array

         
