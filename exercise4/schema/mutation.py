from typing import Optional

import strawberry
from django.db import transaction
from strawberry import Info

from core.models import Product
from .types import ProductType


# ❓What is the advantage of using an input type vs method arguments?
@strawberry.input
class ProductInput:
    pk: Optional[strawberry.ID] = None
    name: str
    social_club_id: strawberry.ID
    # 🛠️price
    # 🛠️quality

# ❓Lookup the UNSET type on the strawberry docs. What could it be useful for? What is the difference between None and UNSET?


@strawberry.type
class Mutation:

    @strawberry.mutation
    @transaction.atomic
    def create_or_update_product(self, info: Info, inp: ProductInput) -> ProductType:
        if inp.pk:
            product = Product.objects.get(id=inp.pk)
        else:
            product = Product()

        product.name = inp.name
        product.social_club_id = product.social_club_id
        # 🛠️price
        # 🛠️quality
        # 💡care with quality, you need to access the Enum.value
        # ❓can we optimize this boilerplate?
        product.save()

        return ProductType.from_obj(product)

