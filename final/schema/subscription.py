import asyncio
from datetime import datetime
from typing import AsyncGenerator

import strawberry
from django.utils import timezone

from core.dataloaders import inject_dataloaders
from core.models import SocialClub
from core.type_helpers import MyInfo
from core.utils import RedisSingleTone
from .types import SocialClubType


@strawberry.type
class Subscription:
    @strawberry.subscription()
    async def count(self, info: MyInfo, target: int = 100) -> AsyncGenerator[int, None]:
        try:
            for i in range(target):
                yield i
                await asyncio.sleep(2)
        except asyncio.CancelledError:
            pass

    @strawberry.subscription()
    async def current_time(self, info: MyInfo) -> AsyncGenerator[datetime, None]:
        try:
            while True:
                yield timezone.now()
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass

    @strawberry.subscription()
    async def message(self, info: MyInfo) -> AsyncGenerator[str, None]:
        pubsub = RedisSingleTone.subscribe("message")
        try:
            while True:
                message = pubsub.get_message()
                if message:
                    data = RedisSingleTone.get_data(message)
                    yield data
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
        finally:
            pubsub.unsubscribe()
            pubsub.reset()

    @strawberry.subscription()
    async def social_club(self, info: MyInfo) -> AsyncGenerator[SocialClubType, None]:
        pubsub = RedisSingleTone.subscribe("social_club_create_update")
        try:
            while True:
                message = pubsub.get_message()
                if message:
                    social_club_id = RedisSingleTone.get_data(message)
                    social_club = await SocialClub.objects.filter(
                        id=social_club_id
                    ).afirst()
                    if social_club:
                        inject_dataloaders(info.context)
                        yield SocialClubType(instance=social_club)
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
        finally:
            pubsub.unsubscribe()
            pubsub.reset()
