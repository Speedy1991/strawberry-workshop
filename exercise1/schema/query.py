from typing import List

import strawberry
from strawberry import Info

from core.models import SocialClub, Product
from exercise1.schema.types import SocialClubType, ProductType


@strawberry.type
class Query:

    @strawberry.field
    def social_clubs(self, info: Info) -> List[SocialClubType]:
        return [SocialClubType(
            id=sc.id,
            name=sc.name,
            # street=sc.street,  # TODO 8: uncomment this as soon as you finished your types
            # zip=sc.zip  # TODO 8: uncomment this as soon as you finished your types
        ) for sc in SocialClub.objects.all()]

    @strawberry.field
    def products(self, info: Info) -> List[ProductType]:
        return [ProductType(
            id=product.id,
            # name=product.name,  # TODO 8: uncomment this as soon as you finished your types
            # price=product.price,  # TODO 8: uncomment this as soon as you finished your types
            # quality=product.quality  # TODO 8: uncomment this as soon as you finished your types
        ) for product in Product.objects.all()]

    # TODO 9: If you have time left: Extend this query with Member
    # TODO 10: If you have time left: Extend this query with Guest

    # TODO 11: Add a field current_date_time and return the current datetime
    # HINT: you can use datetime or django.utils.timezone
