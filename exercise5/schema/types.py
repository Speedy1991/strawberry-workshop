from typing import List, TYPE_CHECKING, Union

import strawberry

from core.schema.enums import QualityEnum
from core.type_helpers import MyInfo
from core.utils import sid

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


@strawberry.type
class SocialClubType:
    instance: strawberry.Private["SocialClub"]

    @strawberry.field()
    def id(self, info: MyInfo) -> strawberry.ID:
        return self.instance.id

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
    def people(self, info: MyInfo) -> List["PersonInterface"]:
        members_and_guests = [
            *self.instance.member_set.all(),
            *self.instance.guest_set.all(),
        ]
        return [PersonInterface.from_obj(mag) for mag in members_and_guests]

    @strawberry.field()
    def products(self, info: MyInfo) -> List["ProductType"]:
        return [
            ProductType.from_obj(product) for product in self.instance.product_set.all()
        ]


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
            quality=product.quality,
            social_club=SocialClubType(instance=product.social_club),
        )


# 📜 https://strawberry.rocks/docs/types/interfaces#interfaces
@strawberry.interface
class PersonInterface:
    id: strawberry.ID
    # 🛠️Add all fields in common
    # 🛠️first_name: str
    # 🛠️last_name: str
    # 🛠️social_club: SocialClubType

    @classmethod
    def from_obj(cls, obj: Union["Member", "Guest"]) -> "PersonInterface":
        # Avoid a potential circular dependency; python is optimizing this while runtime
        from core.models import Member, Guest

        # 🛠️Prepare a kwarg dict with all fields in common
        kwargs = dict()
        if isinstance(obj, Member):
            return MemberType(**kwargs, age=obj.age)  # inject the 'difference'
        if isinstance(obj, Guest):
            return GuestType(**kwargs, rating=obj.rating)  # inject the 'difference'
        raise NotImplementedError


@strawberry.type
class MemberType(PersonInterface):
    pass  # 🛠️age: int


@strawberry.type
class GuestType(PersonInterface):
    pass  # 🛠️rating: int


# 📜https://strawberry.rocks/docs/types/interfaces#implementing-interfaces -> Tip
# It is always nice to offer all possible interface types
# 🛠️Add all possible InterfaceClasses
possible_types = []
