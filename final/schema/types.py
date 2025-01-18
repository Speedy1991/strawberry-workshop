import asyncio
from typing import List, TYPE_CHECKING, Union

import strawberry
from strawberry import Info

from core.schema.enums import QualityEnum
from core.utils import sta

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


@strawberry.type
class SocialClubType:
    instance: strawberry.Private["SocialClub"]

    @strawberry.field
    async def id(self, info: Info) -> strawberry.ID:
        return self.instance.id

    @strawberry.field
    async def name(self, info: Info) -> str:
        return self.instance.name

    @strawberry.field
    async def street(self, info: Info) -> str:
        return self.instance.street

    @strawberry.field
    async def zip(self, info: Info) -> str:
        return self.instance.zip

    @strawberry.field
    async def persons(self, info: Info) -> List["PersonInterface"]:
        members_and_guests = [*await sta(self.instance.member_set.all()), *await sta(self.instance.guest_set.all())]
        return await asyncio.gather(*[PersonInterface.async_from_obj(mag) for mag in members_and_guests])

    @strawberry.field
    async def products(self, info: Info) -> List["ProductType"]:
        products = await sta(self.instance.product_set.all())
        return await asyncio.gather(*[ProductType.async_from_obj(product) for product in products])


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    social_club: SocialClubType

    @classmethod
    async def async_from_obj(cls, product: "Product") -> "ProductType":
        return ProductType(
            id=product.id,
            name=product.name,
            price=product.price,
            quality=product.quality,
            social_club=SocialClubType(instance=product.social_club)
        )


@strawberry.interface
class PersonInterface:
    id: strawberry.ID
    first_name: str
    last_name: str
    social_club: SocialClubType

    @classmethod
    async def async_from_obj(cls, obj: Union["Member", "Guest"]) -> "PersonInterface":
        from core.models import Member, Guest
        kwargs = dict(id=obj.id, first_name=obj.first_name, last_name=obj.last_name, social_club=SocialClubType(instance=obj.social_club))
        if isinstance(obj, Member):
            return MemberType(**kwargs, age=obj.age)
        if isinstance(obj, Guest):
            return GuestType(**kwargs, rating=obj.rating)
        raise NotImplementedError


@strawberry.type
class MemberType(PersonInterface):
    age: int


@strawberry.type
class GuestType(PersonInterface):
    rating: int


possible_types = [MemberType, GuestType]
