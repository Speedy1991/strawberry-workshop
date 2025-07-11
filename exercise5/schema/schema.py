import strawberry
from strawberry.extensions import (
    QueryDepthLimiter,
    MaxAliasesLimiter,
    ParserCache,
    ValidationCache,
    MaskErrors,
)

from .query import Query
from .mutation import Mutation
from .types import possible_types  # noqa

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        QueryDepthLimiter(max_depth=3),
        MaxAliasesLimiter(max_alias_count=15),
        ParserCache(),
        ValidationCache(),
        MaskErrors(),
    ],
    # 🛠️expose possible types
    # 📜https://strawberry.rocks/docs/types/interfaces#implementing-interfaces
    # types=possible_types
)
