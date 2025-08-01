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
from .subscription import Subscription
from .types import possible_types

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
    extensions=[
        QueryDepthLimiter(max_depth=3),
        MaxAliasesLimiter(max_alias_count=15),
        ParserCache(),
        ValidationCache(),
        MaskErrors(),
    ],
    types=possible_types,
)
