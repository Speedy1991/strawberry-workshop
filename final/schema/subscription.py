import asyncio
from datetime import datetime
from typing import AsyncGenerator

import strawberry
from django.utils import timezone
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

    @strawberry.subscription
    async def current_time(self, info: Info) -> AsyncGenerator[datetime, None]:
        try:
            while True:
                yield timezone.now()
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
