from typing import List, TYPE_CHECKING

import strawberry
from strawberry import Info

from core.schema.enums import QualityEnum

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


# 📜https://strawberry.rocks/docs/types/private

@strawberry.type
class SocialClubType:
    instance: strawberry.Private["SocialClub"]

    @strawberry.field
    def id(self, info: Info) -> strawberry.ID:
        return self.instance.id

    @strawberry.field
    def members(self, info: Info) -> List["MemberType"]:
        return [MemberType.from_obj(member) for member in self.instance.member_set.all()]

    # Restore the old behaviour
    # 🛠️write a field resolver for name
    # 🛠️write a field resolver for street
    # 🛠️write a field resolver for zip
    # 🛠️write a field resolver for guests
    # 🛠️write a field resolver for products
    # 🛠️Add an extra field name_uppercase to return the name in full uppercase

    # 📜https://strawberry.rocks/docs/guides/field-extensions#field-extensions
    # 🛠️Add an extra field name_uppercase_ext with a FieldExtension to make it uppercase
    # 💡You can find a prepared UpperCaseExtension in core.utils

    # ❓ Do you know some pro/cons for more boilerplate in types but less logic in queries?


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, product: "Product") -> "ProductType":
        pass
        # 🛠️return a ProductType
        # 💡Care with social club - it must be a type not a model instance


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
