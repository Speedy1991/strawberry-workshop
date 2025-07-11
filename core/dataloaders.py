from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from strawberry.dataloader import DataLoader

from core.models import SocialClub, Product, Person, Member, Guest

from core.utils import sta

if TYPE_CHECKING:
    from core.type_helpers import MyContext


async def _get_objs(Clazz, id_list):
    objects = Clazz.objects.filter(id__in=id_list)
    object_dict = {getattr(obj, "id"): obj for obj in await sta(objects.all())}
    # always returns the same amount of data as requested, even we have None values
    return [object_dict.get(obj_id) for obj_id in id_list]


async def social_club_loader(keys: list[int]) -> list[SocialClub | None]:
    return await _get_objs(SocialClub, keys)


async def product_loader(keys: list[int]) -> list[Product | None]:
    return await _get_objs(Product, keys)


async def person_loader(keys: list[int]) -> list[Person | None]:
    return await _get_objs(Person, keys)


async def member_loader(keys: list[int]) -> list[Member | None]:
    return await _get_objs(Member, keys)


async def guest_loader(keys: list[int]) -> list[Guest | None]:
    return await _get_objs(Guest, keys)


@dataclass
class DataLoaders:
    social_club_loader: DataLoader[int, Optional[SocialClub]]
    product_loader: DataLoader[int, Optional[Product]]
    person_loader: DataLoader[int, Optional[Person]]
    member_loader: DataLoader[int, Optional[Member]]
    guest_loader: DataLoader[int, Optional[Guest]]

    def __init__(self):
        self.social_club_loader = DataLoader(load_fn=social_club_loader)
        self.product_loader = DataLoader(load_fn=product_loader)
        self.person_loader = DataLoader(load_fn=person_loader)
        self.member_loader = DataLoader(load_fn=member_loader)
        self.guest_loader = DataLoader(load_fn=guest_loader)


def inject_dataloaders(ctx: "MyContext"):
    ctx.loaders = DataLoaders()
