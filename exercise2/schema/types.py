import strawberry

from core.schema.enums import QualityEnum


# DOCS: https://strawberry.rocks/docs/general/schema-basics#object-types

@strawberry.type
class SocialClubType:
    id: strawberry.ID
    name: str
    street: str
    zip: str
    # TODO 1: members - care for a forward declaration [List of MemberType's]
    # TODO 2: guests - care for a forward declaration [List of GuestType's]
    # TODO 3: products - care for a forward declaration [List of ProductType's]


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    # TODO 4: social_club (SocialClubType)
    # QUESTION: uh oh - this could go evilly wrong in future...
    # HINT: Maybe we should use one or more schema extensions? https://strawberry.rocks/docs/extensions


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int
    # TODO 5: social_club (SocialClubType)


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
    # TODO 6: social_club (SocialClubType)
