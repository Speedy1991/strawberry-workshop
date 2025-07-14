import asyncio
from datetime import datetime
from typing import List, Optional

import strawberry
from django.db.models import Count
from django.utils import timezone

from core.models import SocialClub, Product
from core.type_helpers import MyInfo
from .types import SocialClubType, ProductType


@strawberry.type
class Query:
    @strawberry.field()
    async def social_club(self, info: MyInfo, pk: strawberry.ID) -> SocialClubType:
        instance = await SocialClub.objects.aget(pk=pk)
        return SocialClubType(instance=instance)

    @strawberry.field()
    async def social_clubs(
        self, info: MyInfo, min_member_count: Optional[int] = None
    ) -> List[SocialClubType]:
        qs = SocialClub.objects.all()
        if min_member_count is not None:
            qs = qs.annotate(member_count=Count("member")).filter(
                member_count__gte=min_member_count
            )
        # 🛠️This won't work - executing a query in an async context will make django cry
        # 💡use the `sta` helper from core.utils
        # ❓Why does line 25 work?
        return [SocialClubType(instance=sc) for sc in qs]

    @strawberry.field()
    async def products(self, info: MyInfo) -> List[ProductType]:
        # 🛠️This won't work - executing a query in an async context will make django cry
        # 💡use the `sta` helper from core.utils
        products = Product.objects.all()
        # ❓Gather? Or just return a List comprehension?
        return await asyncio.gather(
            *[ProductType.async_from_obj(info, product) for product in products]
        )

    @strawberry.field()
    async def current_date_time(self, info: MyInfo) -> datetime:
        return timezone.now()
