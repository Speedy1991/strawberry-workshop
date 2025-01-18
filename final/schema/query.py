import asyncio
from datetime import datetime
from typing import List, Optional

import strawberry
from django.db.models import Count
from django.utils import timezone
from strawberry import Info

from core.models import SocialClub, Product
from final.schema.types import (SocialClubType, ProductType)


@strawberry.type
class Query:

    @strawberry.field
    async def social_club(self, info: Info, pk: strawberry.ID) -> SocialClubType:
        instance = await SocialClub.objects.aget(pk=pk)
        return SocialClubType(instance=instance)

    @strawberry.field
    async def social_clubs(self, info: Info, min_member_count: Optional[int] = None) -> List[SocialClubType]:
        qs = SocialClub.objects.all()
        if min_member_count is not None:
            qs = qs.annotate(member_count=Count('member')).filter(member_count__gte=min_member_count)
        return [SocialClubType(instance=sc) for sc in qs]

    @strawberry.field
    async def products(self, info: Info) -> List[ProductType]:
        return await asyncio.gather(*[ProductType.async_from_obj(product) for product in Product.objects.select_related('social_club')])

    @strawberry.field
    async def current_date_time(self, info: Info) -> datetime:
        return timezone.now()
