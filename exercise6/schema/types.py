import asyncio
from typing import List, TYPE_CHECKING, Union

import strawberry
from core.schema.enums import QualityEnum
from core.type_helpers import MyInfo
from core.utils import sta, sid

if TYPE_CHECKING:
    from core.models import SocialClub, Member, Guest, Product


@strawberry.type
class SocialClubType:
    instance: strawberry.Private["SocialClub"]

    @strawberry.field()
    async def id(self, info: MyInfo) -> strawberry.ID:
        return self.instance.id

    @strawberry.field()
    async def name(self, info: MyInfo) -> str:
        return self.instance.name

    @strawberry.field()
    async def street(self, info: MyInfo) -> str:
        return self.instance.street

    @strawberry.field()
    async def zip(self, info: MyInfo) -> str:
        return self.instance.zip

    @strawberry.field()
    async def people(self, info: MyInfo) -> List["PersonInterface"]:
        # 🛠️Can you write a dataloader for members and guests?
        members = await sta(self.instance.member_set.all())
        guests = await sta(self.instance.guest_set.all())
        people = [*members, *guests]
        return await asyncio.gather(
            *[PersonInterface.async_from_obj(info, person) for person in people]
        )

    @strawberry.field()
    async def products(self, info: MyInfo) -> List["ProductType"]:
        products = await sta(self.instance.product_set.all())
        return await asyncio.gather(
            *[ProductType.async_from_obj(info, product) for product in products]
        )


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    social_club: SocialClubType

    # 💡This is not a "must have async" - but maybe we want to access some async data later? Or gather some ProductType's?
    # 💡It's also nice to have the info object to access the context/request
    @classmethod
    async def async_from_obj(cls, info: MyInfo, product: "Product") -> "ProductType":
        social_club = info.context.loaders.social_club_loader.load(
            product.social_club_id
        )
        return ProductType(
            id=sid(product.id),
            name=product.name,
            price=product.price,
            quality=product.quality,
            social_club=SocialClubType(instance=social_club),
        )


@strawberry.interface
class PersonInterface:
    id: strawberry.ID
    first_name: str
    last_name: str
    social_club: SocialClubType

    @classmethod
    async def async_from_obj(
        cls, info: MyInfo, obj: Union["Member", "Guest"]
    ) -> "PersonInterface":
        from core.models import Member, Guest

        # ❓Why can't we use obj.social_club? Is there a workaround?
        social_club = await info.context.loaders.social_club_loader.load(
            obj.social_club_id
        )
        kwargs = dict(
            id=obj.id,
            first_name=obj.first_name,
            last_name=obj.last_name,
            social_club=SocialClubType(instance=social_club),
        )
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
