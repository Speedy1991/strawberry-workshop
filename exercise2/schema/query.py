from datetime import datetime
from typing import List

import strawberry
from django.utils import timezone
from strawberry import Info

from core.models import SocialClub, Product
from exercise2.schema.types import SocialClubType, MemberType, GuestType, ProductType


@strawberry.type
class Query:

    @strawberry.field
    def social_clubs(self, info: Info) -> List[SocialClubType]:
        # We will refactor this soon...
        return [SocialClubType(
            id=sc.id,
            name=sc.name,
            street=sc.street,
            zip=sc.zip,
            products=[ProductType(
                id=product.id,
                name=product.name,
                price=product.price,
                quality=product.quality,
                social_club=sc
            ) for product in sc.product_set.all()],
            guests=[GuestType(
                id=guest.id,
                first_name=guest.first_name,
                last_name=guest.last_name,
                rating=guest.rating,
                social_club=sc
            ) for guest in sc.guest_set.all()],
            members=[MemberType(
                id=member.id,
                first_name=member.first_name,
                last_name=member.last_name,
                age=member.age,
                social_club=sc
            ) for member in sc.member_set.all()]
        ) for sc in SocialClub.objects.prefetch_related('member_set', 'guest_set', 'product_set')]
        # QUESTION: what would happen if we remove the prefetch related?

    @strawberry.field
    def products(self, info: Info) -> List[ProductType]:
        return [ProductType(
            id=product.id,
            name=product.name,
            price=product.price,
            quality=product.quality,
            social_club=product.social_club
        ) for product in Product.objects.select_related('social_club')]

    @strawberry.field
    def current_date_time(self, info: Info) -> datetime:
        return timezone.now()
