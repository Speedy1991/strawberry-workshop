import strawberry

from core.schema.enums import QualityEnum


# 📜 https://strawberry.rocks/docs/general/schema-basics#object-types

@strawberry.type
class SocialClubType:
    id: strawberry.ID
    name: str
    street: str
    zip: str
    # 🛠️members - care for a forward declaration [List of MemberType's]
    # 🛠️guests - care for a forward declaration [List of GuestType's]
    # 🛠️products - care for a forward declaration [List of ProductType's]


@strawberry.type
class ProductType:
    id: strawberry.ID
    name: str
    price: int
    quality: QualityEnum
    # 🛠️social_club (SocialClubType)
    # ❓uh oh - this could go evilly wrong in future...
    # 💡Maybe we should use one or more schema extensions? https://strawberry.rocks/docs/extensions


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    age: int
    # 🛠️social_club (SocialClubType)


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    rating: int
    # 🛠️social_club (SocialClubType)
