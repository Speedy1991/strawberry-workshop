from strawberry.dataloader import DataLoader

from core.models import SocialClub, Product, Person, Member, Guest
from core.utils import sta
from strawberry.http.typevars import Context


async def _get_objs(Clazz,id_list):
    objects = Clazz.objects.filter(id__in=id_list)
    object_dict = {getattr(obj, 'id'): obj for obj in await sta(objects.all())}
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


def inject_dataloaders(ctx: Context):
    setattr(ctx, 'social_club_loader', DataLoader(load_fn=social_club_loader))
    setattr(ctx, 'product_loader', DataLoader(load_fn=product_loader))
    setattr(ctx, 'person_loader', DataLoader(load_fn=person_loader))
    setattr(ctx, 'member_loader', DataLoader(load_fn=member_loader))
    setattr(ctx, 'guest_loader', DataLoader(load_fn=guest_loader))
