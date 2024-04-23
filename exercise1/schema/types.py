import strawberry


# DOCS: https://strawberry.rocks/docs/types/scalars

@strawberry.type
class SocialClubType:
    id: strawberry.ID
    name: str
    # TODO 1: add a field to resolve the street (String)
    # TODO 2: add a field to resolve the zip (String)


@strawberry.type
class ProductType:
    id: strawberry.ID
    # TODO 3: name (String)
    # TODO 4: price (Int)
    # TODO 5: quality  # HINT There is already a prepared Enum type in core.schema.enums


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    # TODO 6: age (Int)


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    # TODO 7: rating (Int)
