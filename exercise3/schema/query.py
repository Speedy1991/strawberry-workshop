from datetime import datetime
from typing import List

import strawberry
from django.utils import timezone

from core.models import SocialClub, Product
from core.type_helpers import MyInfo
from .types import SocialClubType, ProductType


@strawberry.type
class Query:
    @strawberry.field()
    def social_clubs(self, info: MyInfo) -> List[SocialClubType]:
        return [
            SocialClubType(instance=sc)
            for sc in SocialClub.objects.prefetch_related(
                "member_set", "guest_set", "product_set"
            )
        ]

    @strawberry.field()
    def products(self, info: MyInfo) -> List[ProductType]:
        return [
            ProductType.from_obj(product)
            for product in Product.objects.select_related("social_club")
        ]

    @strawberry.field()
    def current_date_time(self, info: MyInfo) -> datetime:
        return timezone.now()
