from typing import Optional

import strawberry
from django.db import transaction
from dataclasses import asdict

from core.models import Product
from core.schema.enums import QualityEnum
from core.type_helpers import MyInfo
from core.utils import asdict_factory
from .types import ProductType


@strawberry.input
class ProductInput:
    name: str
    social_club_id: strawberry.ID
    price: int
    quality: QualityEnum


@strawberry.type
class Mutation:
    @strawberry.mutation
    @transaction.atomic
    def create_or_update_product(
        self, info: MyInfo, inp: ProductInput, pk: Optional[strawberry.ID] = None
    ) -> ProductType:
        if pk:
            product = Product.objects.get(id=pk)
        else:
            product = Product()
        # This is a nice trick if your input type is a subset of your model
        for k, v in asdict(inp, dict_factory=asdict_factory).items():
            setattr(product, k, v)
        product.save()
        return ProductType.from_obj(product)
