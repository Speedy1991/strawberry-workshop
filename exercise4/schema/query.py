from datetime import datetime
from typing import List

import strawberry
from django.db.models import Count
from django.utils import timezone
from strawberry import Info

from core.models import SocialClub, Product
from exercise4.schema.types import (SocialClubType, ProductType)


@strawberry.type
class Query:

    # TODO 1: Add arguments to the field
    # DOCS: https://strawberry.rocks/docs/general/queries#arguments
    @strawberry.field
    def social_clubs(self, info: Info) -> List[SocialClubType]:
        min_member_count = None  # TODO 1.1: Remove this line
        qs = SocialClub.objects.all()
        if min_member_count is not None:
            # QUESTION/DJANGO: Filtering will destroy our prefetch - is there a performance workaround? Is there a tradeoff?
            qs = qs.annotate(member_count=Count('member')).filter(member_count__gte=min_member_count)
        return [SocialClubType(instance=sc) for sc in qs]

    @strawberry.field
    def products(self, info: Info) -> List[ProductType]:
        return [ProductType.from_obj(product) for product in Product.objects.select_related('social_club')]

    @strawberry.field
    def current_date_time(self, info: Info) -> datetime:
        return timezone.now()
