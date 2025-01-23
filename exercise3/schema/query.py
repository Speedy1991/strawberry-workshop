from datetime import datetime
from typing import List

import strawberry
from django.utils import timezone
from strawberry import Info

from core.models import SocialClub, Product
from .types import SocialClubType, ProductType


@strawberry.type
class Query:

    @strawberry.field
    def social_clubs(self, info: Info) -> List[SocialClubType]:
        return [SocialClubType(instance=sc) for sc in SocialClub.objects.prefetch_related('member_set', 'guest_set', 'product_set')]

    @strawberry.field
    def products(self, info: Info) -> List[ProductType]:
        return [ProductType.from_obj(product) for product in Product.objects.select_related('social_club')]

    @strawberry.field
    def current_date_time(self, info: Info) -> datetime:
        return timezone.now()