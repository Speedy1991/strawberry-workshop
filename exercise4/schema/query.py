from datetime import datetime
from typing import List

import strawberry
from django.db.models import Count
from django.utils import timezone

from core.models import SocialClub, Product
from core.type_helpers import MyInfo
from .types import SocialClubType, ProductType


@strawberry.type
class Query:
    # 🛠️Add arguments to the field
    # 📜https://strawberry.rocks/docs/general/queries#arguments
    @strawberry.field
    def social_clubs(self, info: MyInfo) -> List[SocialClubType]:
        min_member_count = None  # 🛠️ 1.1: Remove this line
        qs = SocialClub.objects.all()
        if min_member_count is not None:
            # ❓Filtering will destroy our prefetch - is there a performance workaround? Is there a tradeoff?
            qs = qs.annotate(member_count=Count("member")).filter(
                member_count__gte=min_member_count
            )
        return [SocialClubType(instance=sc) for sc in qs]

    @strawberry.field
    def products(self, info: MyInfo) -> List[ProductType]:
        return [
            ProductType.from_obj(product)
            for product in Product.objects.select_related("social_club")
        ]

    @strawberry.field
    def current_date_time(self, info: MyInfo) -> datetime:
        return timezone.now()
