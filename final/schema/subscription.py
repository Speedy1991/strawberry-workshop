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
