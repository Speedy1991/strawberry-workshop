import asyncio
from typing import AsyncGenerator

import strawberry
from strawberry import Info


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

    # TODO 1: Write a subscription and return each second the current time

    # HINT:
    # This subscriptions are not really useful. We need something like fanout/pubsub.
    # Introducing pubsub in this workshop will fill another 2 hours, so I'll give you an idea how it works:
    # In your subscription you listen to your pubsub, e.g.:
    # pubsub = redis.pubsub()
    # channel = pubsub.subscribe(key_you_want_to_listen_to)
    # while True:
    #  await asyncio.sleep(1)
    #  message = channel.get_message()
    #  if not message:
    #    continue
    #  yield DataType(**message)
    #
    # Anywhere in your code you can call `redis.publish(key_you_want_to_listen_to, payload)` and all subscribers will receive this payload as message
    # Care: Redis should be a SingleTon per worker!!
