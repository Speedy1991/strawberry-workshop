import strawberry
from strawberry.extensions import (
    QueryDepthLimiter,
    MaxAliasesLimiter,
    ParserCache,
    ValidationCache,
    MaskErrors,
)

from .query import Query

schema = strawberry.Schema(
    query=Query,
    extensions=[
        QueryDepthLimiter(max_depth=3),
        MaxAliasesLimiter(max_alias_count=15),
        ParserCache(),
        ValidationCache(),
        MaskErrors(),
    ],
)
