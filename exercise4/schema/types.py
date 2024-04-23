from typing import List, TYPE_CHECKING

import strawberry
from strawberry import Info

from core.schema.enums import QualityEnum
from core.utils import UpperCaseExtension

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


# DOCS https://strawberry.rocks/docs/types/private

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

    # TODO 2: Add arguments to the field
    # DOCS: https://strawberry.rocks/docs/general/queries#arguments
    @strawberry.field
    def members(self, info: Info) -> List["MemberType"]:
        starts_with = None # TODO 2.1: remove this line
        qs = self.instance.member_set.all()
        if starts_with is not None:
            # QUESTION/DJANGO: Filtering will destroy our prefetch - is there a performance workaround? Is there a tradeoff?
            qs = qs.filter(first_name__istartswith=starts_with)
        return [MemberType.from_obj(member) for member in qs]

    @strawberry.field
    def guests(self, info: Info) -> List["GuestType"]:
        return [GuestType.from_obj(guest) for guest in self.instance.guest_set.all()]

    @strawberry.field
    def products(self, info: Info) -> List["ProductType"]:
        return [ProductType.from_obj(product) for product in self.instance.product_set.all()]

    @strawberry.field
    def name_uppercase(self, info: Info) -> str:
        return self.instance.name.upper()

    @strawberry.field(extensions=[UpperCaseExtension()])
    def name_uppercase_ext(self, info: Info) -> str:
        return self.instance.name


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
                social_club=SocialClubType(instance=product.social_club)  # QUESTION: Could this lead to an N+1 problem with the current query definition? Is there a workaround?
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
        return MemberType(
            id=member.id,
            first_name=member.first_name,
            last_name=member.last_name,
            age=member.age,
            social_club=SocialClubType(instance=member.social_club)
        )


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
    social_club: SocialClubType

    @classmethod
    def from_obj(cls, guest: "Guest") -> "GuestType":
        return GuestType(
            id=guest.id,
            first_name=guest.first_name,
            last_name=guest.last_name,
            rating=guest.rating,
            social_club=SocialClubType(instance=guest.social_club)
        )
