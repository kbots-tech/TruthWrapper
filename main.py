from TruthPy import User


async def main():
    user = User()
    await user.login("truth@kbots.tech", "X8103561x")

    post = await user.post("Hello World!, This is a test post from TruthPy")

    feed = await user.feed.get_feed()

    for post in feed:
        print(post.id)




if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
