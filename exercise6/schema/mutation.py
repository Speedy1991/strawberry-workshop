from typing import Optional

import strawberry
from django.db import transaction
from dataclasses import asdict
from strawberry import Info

from core.models import Product
from core.schema.enums import QualityEnum
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
    async def create_or_update_product(self, info: Info, inp: ProductInput, pk: Optional[strawberry.ID] = None) -> ProductType:
        if pk:
            # DOCS: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#django.db.models.query.QuerySet.aget
            # TODO 1: We need to access the db in an async context
            product = Product.objects.get(id=pk)
        else:
            product = Product()
        for k, v in asdict(inp, dict_factory=asdict_factory).items():
            setattr(product, k, v)
        # DOCS: https://docs.djangoproject.com/en/5.1/ref/models/instances/#django.db.models.Model.asave
        # TODO 2: We need to save the obj in an async context
        product.save()
        # HINT: I already make this async for you :)
        return await ProductType.async_from_obj(info, product)
