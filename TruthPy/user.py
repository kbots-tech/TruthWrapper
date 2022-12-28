from TruthPy.utils import request_json
from TruthPy.posts import Post
from TruthPy.feeds import Feed
from TruthPy.urls import *


class User:
    def __init__(self):
        self.token = None
        self.client_id = "9X1Fdd-pxNsAgEDNi_SfhJWi8T-vLuV2WVzKIbkTCw4"
        self.client_secret = "ozF8jzI4968oTKFkEnsBC-UbLPCdrSv0MkXGQu2o_-M"
        self.feed = None

    async def login(self, username, password):
        response = await request_json(
            LOGIN_URL,
            body={"grant_type": "password", "scope": "read write follow push", "client_id": self.client_id,
                  "client_secret": self.client_secret, "username": username, "password": password},
            method="POST",
        )
        self.token = response["access_token"]
        self.feed = Feed(self.token)
        return response

    async def post(self, text, in_reply_to_id=None, quote_id=None, media_ids=None, sensitive=False, spoiler_text="",):
        body = {"status": text, "in_reply_to_id": in_reply_to_id, "quote_id": quote_id, "media_ids": media_ids, "sensitive": sensitive,
                "spoiler_text": spoiler_text, "visibility": "public", "content_type": "text/plain", "poll": None, "scheduled_at": None, "to": []}

        response = await request_json(
            POST_URL,
            body=body,
            method="POST",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        return response
