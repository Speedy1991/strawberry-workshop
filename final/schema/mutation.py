from typing import Optional

import strawberry
from dataclasses import asdict

from core.models import Product, SocialClub
from core.schema.enums import QualityEnum
from core.type_helpers import MyInfo
from core.utils import asdict_factory
from final.schema.types import ProductType, SocialClubType


@strawberry.input
class ProductInput:
    name: str
    social_club_id: strawberry.ID
    price: int
    quality: QualityEnum


@strawberry.input
class SocialClubInput:
    name: str
    street: str


@strawberry.type
class Mutation:
    @strawberry.mutation()
    async def create_or_update_product(
        self, info: MyInfo, inp: ProductInput, pk: Optional[strawberry.ID] = None
    ) -> ProductType:
        if pk:
            product = await Product.objects.aget(id=pk)
        else:
            product = Product()
        for k, v in asdict(inp, dict_factory=asdict_factory).items():
            setattr(product, k, v)
        await product.asave()
        return await ProductType.async_from_obj(info, product)

    @strawberry.mutation()
    async def create_or_update_social_club(
        self, info: MyInfo, inp: SocialClubInput, pk: Optional[strawberry.ID] = None
    ) -> SocialClubType:
        if pk:
            social_club = await SocialClub.objects.aget(id=pk)
        else:
            social_club = SocialClub()
        for k, v in asdict(inp, dict_factory=asdict_factory).items():
            setattr(social_club, k, v)
        await social_club.asave()
        return SocialClubType(instance=social_club)
