import asyncio
from typing import AsyncGenerator

import strawberry
from strawberry import Info

from core.utils import RedisSingleTone
from .types import SocialClubType


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, info: Info, target: int = 100) -> AsyncGenerator[int, None]:
        try:
            for i in range(target):
                yield i
                await asyncio.sleep(2)
        except asyncio.CancelledError:
            pass

    # 🛠️Write a subscription and return each second the current time

    # 🛠️Use redis for pubsub and yield the messages
    # 💡Use some helper methods from the RedisSingleTone
    # 📜https://redis-py.readthedocs.io/en/stable/advanced_features.html#publish-subscribe
    @strawberry.subscription
    async def message(self, info: Info) -> str:
        pubsub = RedisSingleTone.subscribe('message')
        await asyncio.sleep(5)
        message = 'Hello'
        yield message

    # 🛠️Write a subscription to yield a social club as soon as it is created or changed
    @strawberry.subscription
    async def social_club(self, info: Info) -> SocialClubType:
        pubsub = RedisSingleTone.subscribe('social_club_create_update')
        raise NotImplementedError

    # ❓What about dataloaders in subscriptions?