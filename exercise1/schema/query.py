from typing import List

import strawberry

from core.models import SocialClub, Product
from core.type_helpers import MyInfo
from .types import SocialClubType, ProductType


@strawberry.type
class Query:
    @strawberry.field()
    def social_clubs(self, info: MyInfo) -> List[SocialClubType]:
        return [
            SocialClubType(
                id=sc.id,
                name=sc.name,
                # street=sc.street,  # 🛠️uncomment this as soon as you finished your types
                # zip=sc.zip  # 🛠️uncomment this as soon as you finished your types
            )
            for sc in SocialClub.objects.all()
        ]

    @strawberry.field()
    def products(self, info: MyInfo) -> List[ProductType]:
        return [
            ProductType(
                id=product.id,
                # name=product.name,  # 🛠️uncomment this as soon as you finished your types
                # price=product.price,  # 🛠️uncomment this as soon as you finished your types
                # quality=product.quality  # 🛠️uncomment this as soon as you finished your types
            )
            for product in Product.objects.all()
        ]

    # 📜https://strawberry.rocks/docs/types/scalars#scalars
    # 💡you can use datetime or django.utils.timezone
    # 🛠️Add a field current_date_time and return the current datetime

    # 🛠️If you have time left: Extend this query with Member
    # 🛠️If you have time left: Extend this query with Guest
