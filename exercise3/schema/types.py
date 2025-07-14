from typing import List, TYPE_CHECKING

import strawberry

from core.schema.enums import QualityEnum
from core.type_helpers import MyInfo
from core.utils import sid

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


@strawberry.type
class SocialClubType:
    # 📜https://strawberry.rocks/docs/types/private
    instance: strawberry.Private["SocialClub"]

    @strawberry.field()
    def id(self, info: MyInfo) -> strawberry.ID:
        return self.instance.id

    @strawberry.field()
    def members(self, info: MyInfo) -> List["MemberType"]:
        return [
            MemberType.from_obj(member) for member in self.instance.member_set.all()
        ]

    @strawberry.field()
    def name(self, info: MyInfo) -> str:
        return self.instance.name

    @strawberry.field()
    def street(self, info: MyInfo) -> str:
        return self.instance.street

    @strawberry.field()
    def zip(self, info: MyInfo) -> str:
        return self.instance.zip

    @strawberry.field()
    def guests(self, info: MyInfo) -> List["GuestType"]:
        return [GuestType.from_obj(guest) for guest in self.instance.guest_set.all()]

    # Restore the old behaviour
    # 🛠️write a field resolver for products

    # ❓ Do you know some pro/cons for more boilerplate in types but less logic in queries?

    # Check out FieldExtensions - this is not used in this tutorial, but a very interesting pattern to move logic to the resolver level
    # ❓ Any ideas what this could be useful for?
    # 📜https://strawberry.rocks/docs/guides/field-extensions#field-extensions


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
            id=sid(product.id),
            name=product.name,
            price=product.price,
            quality=QualityEnum(product.quality),
            social_club=SocialClubType(instance=product.social_club),
        )


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, member: "Member") -> "MemberType":
        pass  # 🛠️return a MemberType
        # 💡: Care with social club - it must be a type not a model instance


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, guest: "Guest") -> "GuestType":
        pass  # 🛠️return a GuestType
        # 💡Care with social club - it must be a type not a model instance
        # 💡This copy/paste gets annoying - doesn't it? ;)
