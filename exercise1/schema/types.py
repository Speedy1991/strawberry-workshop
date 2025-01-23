import strawberry


# 📜 https://strawberry.rocks/docs/types/scalars

@strawberry.type
class SocialClubType:
    id: strawberry.ID
    name: str
    # 🛠️ add a field to resolve the street (String)
    # 🛠️ add a field to resolve the zip (String)


@strawberry.type
class ProductType:
    id: strawberry.ID
    # 🛠️name (String)
    # 🛠️price (Int)
    # 🛠️quality  # 💡There is already a prepared Enum type in core.schema.enums


@strawberry.type
class MemberType:
    id: strawberry.ID
    first_name: str
    last_name: str
    # 🛠️age (Int)


@strawberry.type
class GuestType:
    id: strawberry.ID
    first_name: str
    last_name: str
    # 🛠️rating (Int)
