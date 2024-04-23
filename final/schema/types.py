from typing import List, TYPE_CHECKING, Union

import strawberry
from strawberry import Info

from core.schema.enums import QualityEnum

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


@strawberry.type
class SocialClubType:
    instance: strawberry.Private["SocialClub"]

    @strawberry.field
    def id(self, info: Info) -> strawberry.ID:
        return self.instance.id

    @strawberry.field
    def name(self, info: Info) -> str:
        return self.instance.name

    @strawberry.field
    def street(self, info: Info) -> str:
        return self.instance.street

    @strawberry.field
    def zip(self, info: Info) -> str:
        return self.instance.zip

    @strawberry.field
    def persons(self, info: Info) -> List["PersonInterface"]:
        members_and_guests = [*self.instance.member_set.all(), *self.instance.guest_set.all()]
        return [PersonInterface.from_obj(mag) for mag in members_and_guests]

    @strawberry.field
    def products(self, info: Info) -> List["ProductType"]:
        return [ProductType.from_obj(product) for product in self.instance.product_set.all()]


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, product: "Product") -> "ProductType":
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
    def from_obj(cls, obj: Union["Member", "Guest"]) -> "PersonInterface":
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
