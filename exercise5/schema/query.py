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
    def social_club(self, info: MyInfo, pk: strawberry.ID) -> SocialClubType:
        return SocialClubType(instance=SocialClub.objects.get(pk=pk))

    @strawberry.field()
    def social_clubs(
        self, info: MyInfo, min_member_count: Optional[int] = None
    ) -> List[SocialClubType]:
        qs = SocialClub.objects.all()
        if min_member_count is not None:
            qs = qs.annotate(member_count=Count("member")).filter(
                member_count__gte=min_member_count
            )
        return [SocialClubType(instance=sc) for sc in qs]

    @strawberry.field()
    def products(self, info: MyInfo) -> List[ProductType]:
        return [
            ProductType.from_obj(product)
            for product in Product.objects.select_related("social_club")
        ]

    @strawberry.field()
    def current_date_time(self, info: MyInfo) -> datetime:
        return timezone.now()
