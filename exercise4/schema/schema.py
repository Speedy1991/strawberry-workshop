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
)
